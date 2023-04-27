def first_half(str):
    """Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"."""
    length_of_word = int((len(str)/2))
    return str[:length_of_word]

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))