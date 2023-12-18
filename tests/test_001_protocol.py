"""Tests the protocol."""

import struct
import pytest
from protocol import Protocol

class TestProtocol:
    """Protocol Test class"""
    @classmethod
    def setup_class(cls):
        """Tests class setup."""
        cls.protocol_instance = Protocol()

    def test_encode_tlv(self):
        """Tests encoder."""
        itype = 1
        value = "Hello, World!"
        encoded_data = self.protocol_instance.encode_tlv(itype, value)
        decoded_data = struct.unpack("!B H 13s", encoded_data)
        assert decoded_data[0] == itype
        assert decoded_data[1] == len(value)
        assert decoded_data[2].decode() == value

    def test_decode_tlv(self):
        """Tests decoder."""
        itype = 1
        value = "Hello, World!"
        encoded_data = struct.pack(f"!B H {len(value)}s", itype, len(value), value.encode())
        decoded_data = self.protocol_instance.decode_tlv(encoded_data)
        assert decoded_data == (itype, len(value), value)

    def test_checktype_valid(self):
        """Tests checktype."""
        valid_types = ["Request", "Grant", "Deny", "Keep_Alive", "Still_Alive"]
        for itype_str in valid_types:
            assert self.protocol_instance.checktype(itype_str) in [1, 2, 3, 4, 5]

    def test_checktype_invalid(self):
        """Tests Checktype."""
        invalid_type = "InvalidType"
        with pytest.raises(ValueError, match="Unknown Type"):
            self.protocol_instance.checktype(invalid_type)
