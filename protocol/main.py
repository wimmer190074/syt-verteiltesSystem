"""This is a sample implementation of the protocol"""

from protocol import Protocol

pr = Protocol()

def main():
    """Uses the readin() function to read in the type & message 
       and encodes and decodes it for presentation purposes."""
    itype, imessage = readin()
    encoded_data = pr.encode_tlv(itype, imessage)
    print(f"Encoded Data: {encoded_data}")

    decoded_type, decoded_length, decoded_value = pr.decode_tlv(encoded_data)
    print(f"Decoded Type: {decoded_type}")
    print(f"Decoded Length: {decoded_length}")
    print(f"Decoded Value: {decoded_value}")

def readin():
    """Reads in the Type and the Message 
       and uses the checktype function to convert and check the type."""
    acceptedtype = False
    while not acceptedtype:
        itype = input("Enter your Type (Request, Grant, Deny, Keep_Alive, Still_Alive): ")
        try:
            itype = pr.checktype(itype)
            acceptedtype = True
        except ValueError as ve:
            print(ve)
            acceptedtype = False
    message = input("Please enter your message: ")
    return itype, message

main()
