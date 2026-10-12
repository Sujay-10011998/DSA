def maximum_subarray(arr):

    max_sum = 0

    for st in range(len(arr)):
        cur_sum = 0
        for end in range(st, len(arr)):
            # for i in range(st, end+1):
            #     print(arr[i], end="")
            # print(" ", end="")

            cur_sum += arr[end]
            max_sum = max(max_sum, cur_sum)

        # print("")
    return max_sum
arr = [1,-2,3,4,-5]
print(maximum_subarray(arr))