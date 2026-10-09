
def merge_sorted_array(arr1, arr2):
    sort_1 = sorted(arr1)
    sort_2 = sorted(arr2)

    sort_3 = []
    i = 0
    j = 0

    while i < len(sort_1) and j < len(sort_2):
        if sort_1[i] <= sort_2[j]:
            sort_3.append(sort_1[i])
            i += 1
        else:
            sort_3.append(sort_2[j])
            j += 1


    return sort_3


array1 = list(map(int, input("Enter 1st array elements separated by space: ").split()))

array2 = list(map(int, input("Enter 1st array elements separated by space: ").split()))

res = merge_sorted_array(array1, array2)
if res:
    print(f"merged sorted array: {res}")





#when the arrays are not sorted

    # if arr1 != sorted(arr1):
    #     for i in range(len(arr1)):
    #         if arr1[i] > arr1[i+1]:
    #             arr1[i+1] = arr1[i]
    #             sort_1 = arr1

    # if arr2 != sorted(arr2):
    #     for i in range(len(arr2)):
    #         if arr2[i] > arr2[i+1]:
    #             arr2[i+1] = arr2[i]
    #             sort_2 = arr2