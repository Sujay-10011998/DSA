from collections import Counter

def count_word_freq(str):
    f = Counter(str)
    return f

j = input("Enter a string: ").split()
p = count_word_freq(j)
if p:
    print(f"Word sequence of the words {j} are {p}")