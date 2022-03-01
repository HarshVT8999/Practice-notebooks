#Method 1 - Brute Force

def WaterArea(list):
    maxarea = 0
    for i in range(len(list)):
        for j in range(len(list)-1,i+1,-1):
            if(list[i]<list[j]):
                area = list[i]*(j-i)
            else:
                area = list[j]*(j-i)
            if area>maxarea:
                maxarea = area
    
    print(maxarea)                       # list [1,8,6,2,5,4,8,3,7]

#WaterArea([1,8,6,2,5,4,8,3,7])

#Method 2 - Low Time Complexity

def WaterArea2(height):
    maxarea = 0
    l,r = 0,len(height)-1

    while(l<r):
        area = (r-l)*min(height[l],height[r])
        maxarea = max(maxarea,area)
        if (height[l]<height[r]):
            l += 1
        else:
            r -= 1

    print(maxarea)

WaterArea2([1,8,6,2,5,4,8,3,7])