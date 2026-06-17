# TUPLE OBJECT
print("\n=====1. TUPLE CREATION=====  \n")
print("\n______by using empty()____________\n")
data=()
print(data)
print(type(data))

print("\n_______by using known elements__________\n")
s=(1,2,3,"suchi","bhavi","chaitu",("data",123))
print(s)
print(type(s))

s=1,2,3,"suchi","bhavi","chaitu",("data",123)
print(s)
print(type(s))

a=10
print(a)
print(type(a))#int

a=10,
print(a)
print(type(a))#tuple

print("\n______by using dynamic data______\n")
names=eval(input("enter tuple:"))
print(names)
print(type(data))

print("\n___by using tuple()______\n")
t="1234"
t1=tuple(t)
print(t)
print(t1)

t=input("enter data:")
t1=tuple(t)
print(t1)

print("\n====2. TUPLE RETRIVE===== \n")

print("\n_____index______\n")
t=1,'kathi',(1,'uma','suchi'),{'making':'parota'}
print(t[3]['making'])
print(t.index('kathi'))

print("\n_____slicing______\n")
t=(1,3,45,56,654,345,"433")
print(t[6:3:-1])
print(t[-1][0])

print("\n_____concatination______\n")
s1=(1,2,3,'sir',"$")
s2="suchi","amma","python"
print(s1+s2)

print("\n_____repetition______\n")
a="cell","data","recharge","movies","shorts"
print(a*2)

print("\n______sorted_________\n")
t=(7,9,0,6,7)
b=sorted(t)
print(b)
print(type(b))
print("\n")
t="suchi","chsitu","bhavi",'uma'
s=sorted(t)
print(s)
print(type(b))
print("\n")

print("\n______maximum_________\n")
x=(955,4556,87,765,65,5443,78)
print(max(x))
print(type(x))

print("\n______minmum_________\n")
s=(100,200,300,400,500)
print(min(s))
print(type(s))