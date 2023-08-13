def mysplit(strng):
    strng = strng.strip()
    new_string = strng.split()

    return new_string


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
