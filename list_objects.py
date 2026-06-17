#list-creating list objects

print("______1.creating empty[] list_____")

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

print("_______2.creating list object using known elements_______")

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

print("_______3.creating list object using dynamic data______")

l=eval(input("enter list:"))#we do not skip eval,eval is mandatory
print(l)
print(type(l))
print(len(l))
print("\n")

print("_______4.creating list object using split_______")

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


print("_____5.creating list object using list()_____")

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

print("______1.indexing______")

x=["suchi",3,0.6,"data",True]
print(x[3])
print(x[-1])
print("\n")

print("________2.slicing______")

list=["suchi",3,0.6,"data","True"]
print(list[-1][::-1])
print(type(list))
print("\n")

print("______3.count______")

l=["suchi",1,2,30,"True",2,7,30,30,"suchi","bhavi"]
print(l.count(30))
print(type(l))
print("\n")

print("______________________update______________________________")

print("______1.append________")

l=[1,2,34,5]
l.append(30)
print(l)
print("\n")

print("________2.extend________")

l=[1,2,34,5]
l.extend([90,78])
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

print("_______3.insert_________")

l=[1,2,3]
l.insert(0,9)
print(l)
print(type(l))
print("\n")

print("___________4.reverse_______")

l=[1,2,4]
l1=[3,5,6]
l.extend(l1)
print(l)
l.reverse()
print(l)
print("\n")

print("___________5.sort_________")

l=[8,9,0,11,2,5,3]
print(l[0:4])
l.sort()
print(l)


print("________________________concatination______________________")
#concatination
l=[10,20,2]
l1=[20,30,40]
l2=l+l1
print(l2)
print("\n")

print("________________________repetition________________________")
#repetition
l=[1,2,3]
b=l*3
print(b)


print("____________________delete___________________")

print("_____1.remove_____")

l=[1,4,5,8,0]
l.remove(0)
print(l)
print("\n")


print("___2.pop_____")

l=[1,4,5,8,0]
l.pop()
print(l)
print("\n")

print("_____3.clear___")

l=[1,4,5,8,0]
l.clear()
print(l)
print("\n")
print("======copy methods========")
print("____1. aliasing_____")
l=[10,20,30,40]
l1=l
print(l)
print(l1)
l1[3]=23
print(l1)
print(l)

print("\n")
print("_____2.cloning________")
print("===A.slicing======")
l1=[10,20,30,40]
l2=l1[0:3]
print(l1)
print(l2)
l2[2]=23
print(l1)
print(l2)
print("\n")

print("_______3.copy_________")
l1=[10,20,30,40]
l2=l1.copy()
print(l1)
print(l2)
l2[3]=23
print(l1)
print(l2)
print("\n")

print("______nested list_____")
list=[10,90,8,4,87,6,54,67,[22,"suchi",[65,88]]]
print(list[3])
print(list[-1][1])
print(list[-1][2][1])

print("\n___________maximum_________\n")
s=[100,200,300,667,345,876]
print(max(s))


print("\n___________minimum_________\n")
num=[34,99,45,77,91,46,0.4]
print(min(num))








