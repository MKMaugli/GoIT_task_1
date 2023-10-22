def offset_char(char, offset):
    if 'a' <= char <= 'z':
        return chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
    return char

def encode_string(input_string, offset):
    encoded_string = ""
    for char in input_string:
        encoded_string += offset_char(char, offset)
    return encoded_string

message = input("Enter a string to encode: ")
offset = int(input("Enter the offset amount: "))
encoded_message = encode_string(message, offset)
print("Encoded string:", encoded_message)