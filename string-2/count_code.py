def count_code(str):
    """
    Return the number of times that the string "code"   appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """

    count = 0
    for char in range(len(str)):
        if str[char:char+2]=='co' and str[char+3] == 'e':
            count += 1
            continue

    return count

print(count_code('aaacodebbb'))
print(count_code('codexxcode') )
print(count_code('cozexxcope'))