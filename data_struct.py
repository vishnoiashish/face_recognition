list1 = [123, 'xyz', 'zara', 'abc']
list2 = [456, 700, 200]
print ("Max value element : ", str(list1))
print ("Max value element : ", max(list2))
list3=[]
for i in list1:
    list3.append(str(i))
print ("Max value element list 3 : ", max(list3))

list4a = ['456', '700', '200','1','100','111','2']
print ("Max value str element list 4a : ", max(list4a))
#print ("Max value int element : ", max(int(list4a)))
list3a=[]
for i in list4a:
    print("print",int(i))
    list3a.append(str(i))
print ("Max value element in 3a : ", max(list3a))
list4a = ['1','100','111','2']
print ("Max value str element list 4a : ", max(list4a))
lis = ['1','100','111','2','7000']
print("lis_max",max(lis))
print("lis_max",max(lis, key=lambda x:int(x)))

for i in range(len(list2)):
    print(i, list2[i])
#!/usr/bin/python

str1 = "this is really a string example....wow!!!";
print ("Max character: " + max(str1))

str2 = "this is a string example....wow!!!";
print ("Max character: " + max(str2))

tuple1, tuple2 = ('123', 'xyz', 'zara1', 'abc'), (456, 700, 2000)
print ("Max value element : ", max(tuple1))
print("Max value element : ", max(tuple2))

stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
print("len of dict:", len(stats))
max_value_list=[]
for i in stats:
    #print ("stats[i]", stats[i])
    max_value_list.append(stats[i])
print("max_dict_val: ",max(max_value_list))

JI=['Hi!'] * 4

print ("ji", JI)

#!/usr/bin/python

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))

xj = ["AJK","exit","Down","World","HappyASD"]
#print(ord(xj[0]))
print("x max",max(xj))
print("x max",max(str(xj)))
print("x max1",max(xj, key=len))
print("x max1 str:",max(xj, key=lambda x: str(x)))
LO=[]
sum=lambda x: x + x
for x in range(10):
    LO.append(sum(x))
print("LO",LO)
listkl=[]
guju=lambda i: len(i)
for i in xj:
    listkl.append(guju(i))
print("listkl",listkl) # problem
print("x max1 int:",max(xj, key=lambda x: len(x))) # problem if we replace len with int
for s in xj:
    print(s, "=ascii:", "".join(str(ord(k)) for k in s))
print("x max1 int ord:",max(xj, key=lambda x: "".join(str(ord(k)) for k in x))) # problem if we replace len with int

s = 'hi'
for i in s:
    print ("i is ::", i)
    print(ord(i))
print("".join(str(ord(k)) for k in s))



