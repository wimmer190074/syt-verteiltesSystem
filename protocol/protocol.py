import struct

class Protocoll():
    def __init__(self):
        print("protocol constructor")

    @staticmethod
    def encode_tlv(type, value):
        length = len(value)
        tlv_format = "!B H {}s".format(length)
        tlv_data = struct.pack(tlv_format, type, length, value.encode())
        return tlv_data

    @staticmethod
    def decode_tlv(data):
        type_length = struct.unpack("!B H", data[:3])
        type_value = data[3:]
        return type_length[0], type_length[1], type_value.decode()

encoded_data = Protocol.encode_tlv(1, "Hello")
print(f"Encoded Data: {encoded_data}")

decoded_type, decoded_length, decoded_value = Protocol.decode_tlv(encoded_data)
print(f"Decoded Type: {decoded_type}")
print(f"Decoded Length: {decoded_length}")
print(f"Decoded Value: {decoded_value}")
