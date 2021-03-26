import string as str
string = "This is the way things are."
print(str.capwords(string, ' '))

def to_title_case(string):
    return " ".join(w.capitalize() for w in string.split())
