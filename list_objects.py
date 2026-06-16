#list-creating list objects

#1.creating empty[] list

l=[]
print(l)
print(type(l))

print("\n\n")
l=list()
print(l)
print(type(l))
print(len(l))
print("\n")
#l=list{}
print(l)
print(type(l))
print(len(l))
print("\n")

#2.creating list object using known elements

l=[1,2,3,"suchi","bhavi",0.9,False,"&",]
print(l)
print(type(l))
print(len(l))
print("\n")
l=[{1,2,3,"suchi","bhavi",0.9,False,"&"},]
print(l)
print(type(l))
print(len(l))
print("\n")

#3.creating list object using dynamic data

l=eval(input("enter list:"))#we do not skip eval,eval is mandatory
print(l)
print(type(l))
print(len(l))
print("\n")

#4.creating list object using split

l="a b c 176 3+0j "
x=l.split()
print(x)
print("\n")
l="a b c bhavya suchi 3+0j 0.003 "
x=l.split(" ",3)
print(x)
print(type(x))
print(len(x))
print("\n")


#5.creating list object using list()

l="123" 
b=list(l)
print(b)
print(type(b))
print("\n")
l="sucharitha" 
b=list(l)
print(b)
print(type(b))


print("___________________________retrieve/accessing____________________")

#1.indexing

x=["suchi",3,0.6,"data",True]
print(x[3])
print(x[-1])
print("\n")

#2.slicing

list=["suchi",3,0.6,"data","True"]
print(list[-1][::-1])
print(type(list))
print("\n")

#3.count

l=["suchi",1,2,30,"True",2,7,30,30,"suchi","bhavi"]
print(l.count(30))
print(type(l))
print("\n")

print("______________________update______________________________")

#1.append

l=[1,2,34,5]
l.append(30)
print(l)
print("\n")

#2.extend

l=[1,2,34,5]
l.extend([30,40])
print(l)
print(type(l))
print("\n")

l=[1,2,34,5]
l.extend(range(10))
print(l)
print(type(l))
print("\n")

l=[1,2,3]
l1="2899"
l.extend(l1)
print(l)
print(type(l))
print("\n")

#3.insert

l=[1,2,3]
l.insert(0,9)
print(l)
print(type(l))
print("\n")

#4.reverse

l=[1,2,4]
l1=[3,5,6]
l.extend(l1)
print(l)
l.reverse()
print(l)
print("\n")

#5.sort

l=[8,9,0,11,2,5,3]
print(l[0:4])
l.sort()
print(l)

print("____________________delete___________________")

#1.remove

l=[1,4,5,8,0]
l.remove(0)
print(l)
print("\n")


#2.pop

l=[1,4,5,8,0]
l.pop()
print(l)
print("\n")

#3.clear

l=[1,4,5,8,0]
l.clear()
print(l)
print("\n")






