def merge_intervals(arr):
    merged_arr = []
    arr.sort()

    for i in arr:
        if not merged_arr or merged_arr[-1][1] < i[0]:
            merged_arr.append(i)
        else:
            merged_arr[-1][1] = max(i[1], merged_arr[-1][1])

    return merged_arr


a = [[1, 3], [2, 6], [8, 10], [11, 12]]

res = merge_intervals(a)
print(f"Merge intervals are: {res}")