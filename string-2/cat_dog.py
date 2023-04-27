def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """

    cat_count = 0
    dog_count = 0

    for char in range(len(str)):
        if str[char:char+3] == "cat":
            cat_count += 1
        if str[char:char+3] == "dog":
            dog_count +=1

    if cat_count == dog_count:
        return True
    else:
        return False
    

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog') )