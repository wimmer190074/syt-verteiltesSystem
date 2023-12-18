"""Decode and Encode from and to the protocol"""

import struct

class Protocol():
    """Class to Decode, Encode and convert the text type to the correct value"""
    def __init__(self):
        print("protocol constructor")

    @staticmethod
    def encode_tlv(itype, value):
        """Takes type(int) and value(str) and encodes it."""
        length = len(value)
        tlv_format = f"!B H {length}s"
        tlv_data = struct.pack(tlv_format, itype, length, value.encode())
        return tlv_data

    @staticmethod
    def decode_tlv(data):
        """Takes encoded data and decodes it."""
        type_length = struct.unpack("!B H", data[:3])
        type_value = data[3:]
        return type_length[0], type_length[1], type_value.decode()

    def checktype(self, itype):
        """Takes the entered type(str), checks if the entry is valid and converts it to int"""
        if itype == "Request":
            itype = 1
            return int(itype)
        elif itype == "Grant":
            itype = 2
            return int(itype)
        elif itype == "Deny":
            itype = 3
            return int(itype)
        elif itype == "Keep_Alive":
            itype = 4
            return int(itype)
        elif itype == "Still_Alive":
            itype = 5
            return int(itype)
        else:
            raise ValueError("Unknown Type")
