def Merge(s1, s2):
    merged = []
    # Find the length of the shorter string
    min_len = min(len(s1), len(s2))
    
    for i in range(min_len):
        merged.append(s1[i])
        merged.append(s2[i])
    
    if len(s1) > min_len:
        merged.extend(s1[min_len:])
    if len(s2) > min_len:
        merged.extend(s2[min_len:])
    
    return ''.join(merged)

string1 = "sjyuamna"
string2 = "uakmrodl"
result = Merge(string1, string2)
print(result)  
