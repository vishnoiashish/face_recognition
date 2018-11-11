data=[4,5,2,6,7,777,2,4,6,7,2,3,5,6,8,89,9,9,9,0,8,7,66,65,44,33,2,2,222,22,345,678,2,334,55,567,334,45,67,89,90]
target=222

#Linear Search by iteration
import time

def linear_search(data,target):
    for i in data:
        if i==target:
            print ("target found : %s", target , "")
            print("target found : with string %s" %target)
            print("target {} found : as {} at index {}".format(target,i,data.index(i)))

def linear_search_1(data,target):
    for i in range(len(data)):
        if data[i]==target:
            print ("target found : %s", target , "")
            print("target found : with string %s" %target)
            print("target {} found : at index {} as {}".format(target,i,data[i]))


start_time = time.clock()
print(start_time)
linear_search(data,222)
linear_search_1(data,345)
print(time.clock())
print("--- %s seconds ---" % round(time.clock() - start_time,8))




#Linear Search by Recursion
#Not possible beacause there is only one loop
