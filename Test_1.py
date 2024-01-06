def generator_numbers(string=""):
    if string == "":
        return ""        
    s_before = ""
    for s in string[::]:
        if s.isnumeric():
            s_before += s
        else:
            if s_before != "":
                yield s_before
                s_before = ""
    

def sum_profit(string):
    num = generator_numbers(string)
    sum = 0
    for i in num:
        sum += int(i)
    return sum