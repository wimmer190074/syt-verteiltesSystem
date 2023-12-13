import struct

class Protocoll():
    def __init__(self):
        pass
    def encode_tlv(type, value):
        length = len(value)
        tlv_format = "!B H {}s".format(length)
        tlv_data = struct.pack(tlv_format, type, length, value)
        return tlv_data

    def decode_tlv(data):
        pass