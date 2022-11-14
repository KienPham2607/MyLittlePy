def swap_case(s):
    k = ''
    for char in s:
        if char.islower():
            k += char.upper()
        else:
            k += char.lower()
    return k    # or return s.swapcase()


s = input()
result = swap_case(s)
print(result)
