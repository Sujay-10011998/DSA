def container_with_most_water(arr):
    n = len(arr)
    max_cont = 0
    best_st = 0
    best_end = 0

    for st in range(n):
        for end in range(st + 1, n):
            h = min(arr[st], arr[end])
            w = end - st
            cur_cont = h * w

            if cur_cont > max_cont:
                max_cont = cur_cont
                best_st = st
                best_end = end

    return best_st, best_end, max_cont


e = [5, 5, 8, 9, 1, 0]
res = container_with_most_water(e)
print("st,end & max amount are: ", res)