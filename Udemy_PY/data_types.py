float_inf=float('inf')
print(type(float_inf))


complex_num=2+3j
print(type(complex_num))

List=[1,True,"ML"]  # Values can be changed
print(type(List))

Tuple=(1,True,"ML")  # Values cannot be changed
print(type(Tuple))

Set=set([1,3,2,2,4,5,6,4])  # There will not be any duplicates
print(Set)

Dictionary={'a':'A', 2:'AA',True:1, False:0}
print(Dictionary)


x=1
if x==1:
 print("x == 1")
 print("x is a bad bitch")
elif x==2:
    print("x == 2")
else:
    x==0
    print("x == 0")
    