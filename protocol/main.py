from protocol import Protocol


def main():
    Protocol()

    encoded_data = Protocol.encode_tlv(1, "Hello")
    print(f"Encoded Data: {encoded_data}")

    decoded_type, decoded_length, decoded_value = Protocol.decode_tlv(encoded_data)
    print(f"Decoded Type: {decoded_type}")
    print(f"Decoded Length: {decoded_length}")
    print(f"Decoded Value: {decoded_value}")

main()