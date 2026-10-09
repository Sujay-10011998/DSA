#RULE:  I can buy any day but after buy I can't sell on that day. I should sell it any day after that day of buying
#RULE:  I have to gain maximum profit



def buy_sell(arr):

    max_profit = 0

    for b in range(len(arr)):
        for s in range(b+1, len(arr)):
            if arr[s]-arr[b] > max_profit:
                max_profit = arr[s]-arr[b]
    return max_profit

arr = [3,8,2,10,4,12]
print(buy_sell(arr))