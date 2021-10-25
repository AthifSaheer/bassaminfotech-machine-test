# ------------ Quesion 001 ------------
var1= 10
var2 = 90
var1, var2 = var2, var1

# ------------ Quesion 002 ------------
def count_substring(string, substring):
    return string.count(substring)

input_str = 'EveninGMorninG'
sub_str = 'inG'
count_substring(input_str, sub_str)

# ------------ Quesion 003 ------------
def convert_string_case(string):
    new_str = ""
    for i in string:
        if i.islower():
            new_str += i.upper()
        else:
            new_str += i.lower()
    return new_str
    
strng = "Hello"
convert_string_case(strng)