def switch_average(x):
    """function will check the key in the dictionary created below and will
       return the value in the values part of the dictionary"""
    return{
        'a':"The key is a and this string is the value",
        'b':"The key is b and this other string is the value",

    }.get(x,"The key is not a or b so this is the default value string")

if __name__ == '__main__':
    print(switch_average('c'))
