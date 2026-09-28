from collections import Counter

def freq_counter(arr):
    f = Counter(arr)
    return f

u = list(map(int, input("Enter arr elements separated by space: ").split()))
l = freq_counter(u)

if l:
    print("Count of frequency of elements: ", l)