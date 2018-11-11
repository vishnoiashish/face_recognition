data=[4,5,2,6,7,777,2,4,6,7,2,3,5,6,8,89,9,9,9,0,8,7,66,65,44,33,2,2,222,22,345,678,2,334,55,567,334,45,67,89,90,91]
target=222

#Linear Search by iteration O(log(n)
import time

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    print(first,last)
    loc=0
    pos = 0
    while first<=last and not found:

        if last/2==0:
            midpoint = (first + last)//2
        else:
            midpoint = (first+last-1)//2
        print (midpoint)
        if alist[midpoint] == item:
            pos = midpoint
            found = True
            if first==0:
                loc=last
            if first!=0:
                loc=first
            print("found item ", item, "@index",loc)
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            if item > alist[midpoint]:
                first = midpoint+1
    print("found data {} @ index {} ".format(item,loc))
    return (pos, found)

binarySearch(data,7)
binarySearch(data,90)
binarySearch(data,91)