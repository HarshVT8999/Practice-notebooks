def StockProfit(list):
    #profit = {}
    left = 0
    maxp = 0
    for right in range(1,len(list)):
        if list[left]>list[right]:
            left = right
        prof = list[right]-list[left]
        if prof>maxp:
            maxp = prof
    print(maxp)

StockProfit([7,1,5,3,6,4])