from collections import Counter

def count_char_freq(str):
    u = Counter(str)
    return u

l = input("Enter a string: ")
g = count_char_freq(l)

if g:
    print(f"Count of char is the string {l} is: {g}")