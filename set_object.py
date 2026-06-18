#SET_OBJECT
print("==========================creating set object===============================\n")
s={}
print(s)
print(type(s))# it is a dict

print("\n___________________________1.by using set()_________________________________\n")
s=set()
print(s)
print(type(s))

print("\n__________________________by using known elements______________________________\n")
data={"python","java","sql",'html'}
print(data)
print(type(data))

print("\n_________________by using dynamic data______________\n")
names=eval(input("enter set:"))
print(names)
print(type(names))

print("\n===================update===================================\n")
print("____________________add_________________________")
s={10,20,30}
s.add(20)
print(s)
print(type(s))
print("\n")

s=set()
s.add(10)
s.add(20)
print(s)
print(type(s))
print("____________________update_________________________")
s={20,49,55,0,4,99}
s.update((1,3))#we can update elements in a iterable form only.
print(s)
print(type(s))

print("\n===================delete===================================\n")
print("\n____________________discard_________________________\n")
d={100,20,300,800}
d.discard(400)
print(d)

print("\n____________________pop_________________________\n")
m={10,84,948,8,884}
m.pop()
print(m)

print("\n____________________clear_________________________n")
d={100,84,"jam",'make'}
d.clear()
print(d)
print(type(d))

print("\n================python set operators===================\n")
print("\n____________________union_______________________\n")
f={1,2,34,55,78}
f1={3,2,55,88,9}
print(f.union (f1))
print(f|f1)

print("\n____________________set intersection_______________________\n")
s1={"python","java",2,3,"urls","threads"}
s2={"make",(3,7,8),12,'3','5','6',"urls"}
print(s1.intersection(s2))
print(s1&s2)

print("\n____________________set intersection_update_______________________\n")  
a={1,2,3,4}
b={4,6,89,9}
b.intersection_update(a)
print(b)
print("\n")
a=[1,2,3,4]
b=(2,7,8,8,6)
c={1,2,0,44}
c.intersection_update(a,b)
print(c)
print(type(c))

print("\n____________________set difference_______________________\n")  
s={2,3,4,5}
s1={2,3,9,3,}
print(s.difference(s1)) 
print(s-s1)                                                                                                                                                                                                                          