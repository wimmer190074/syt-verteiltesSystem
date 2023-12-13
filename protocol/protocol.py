import struct

class Protocol():
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
