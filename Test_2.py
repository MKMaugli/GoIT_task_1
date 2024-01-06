button_map = {
    ".": "1",
    ",": "1",
    "?": "1",
    "!": "1",
    ":": "1",
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "8",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9",
    " ": "0",
}

def sequence_buttons(string):
    if not isinstance(string, str):
        raise TypeError("string must be a string")

    result = ""
    for char in string:
        for key, value in button_map.items():
            if char == key:
                result += value
                break
    return result
