# message = "Hello my little friends!"    # input("Enter a message: ")
# shift = 37     #int(input("Введіть зміщення: "))
# encoded_message = ""

def shift_char(char, shift):
    if 'a' <= char <= 'z':
        return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    return char

def encode_string(input_string, shift):
    encoded_string = ""
    for char in input_string:
        encoded_string += shift_char(char, shift)
    return encoded_string

input_string = input("Enter a string to encode: ")
shift = int(input("Enter the shift amount: "))
encoded_result = encode_string(input_string, shift)
print("Encoded string:", encoded_result)
