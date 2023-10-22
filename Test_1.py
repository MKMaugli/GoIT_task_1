message = input("Enter a message: ")        #"Hello my little friends!"
offset = int(input("Введіть зміщення: "))   #37
encoded_message = ""

for ch in message:
    if "a" <= ch <= "z":
        pos_char = ord(ch) - ord('a')
        pos_new = (pos_char + offset) % 26
        encoded_message = encoded_message + chr(pos_new + ord("a"))
    elif "A" <= ch <= 'Z':
        pos_char = ord(ch) - ord('A')
        pos_new = (pos_char + offset) % 26
        encoded_message = encoded_message + chr(pos_new + ord("A"))
    else:
        encoded_message = encoded_message + ch

print(encoded_message)

