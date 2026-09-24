a = "abba"
mid = int(len(a)/2)
f = a[mid:]
l = a[:mid]
if(f==l[::-1]):
    print(a + " is palindrome")
else:
    print(a + " is not palindrome")    