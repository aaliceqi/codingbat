def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    """
    word = ""
    for char in range(len(str)):
        word += str[:char+1]
    return word

print(string_splosion('Code') )
print(string_splosion('abc') )
print(string_splosion('ab'))
