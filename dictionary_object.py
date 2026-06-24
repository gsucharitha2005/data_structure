# DICTIONARY DATA STRUCTURE
print("\n===============CREATING dictionary==============\n")
print("\n___________ create empty dictionary object____________\n")
a={}
print(a)
print(type(a))

print("\n")
d={}
d[100]="suchi"
d[200]="learn"
d[300]="python"
print(d)
print(type(d))

print("\n")
print("len of dict")
tup={}
tup[(1,2,4)]=8
tup[(4,2,1)]=10
tup[(1,2)]=12
sum=0
for k in tup:
	sum +=tup[k]
print(len(tup)+sum)

print("\n===============RETRIVE dictionary=================\n")
#we can read the dictonary using "key".
d={"suchi":(1,2,3),"master":(4,5,6)}
print(d["suchi"])
print(type(d))


print("\n===============UPDATE dictionary=================\n")
#adding key value pair
da={"suchi":"girl","madhu":"boy","bhavi":"girl"}
da["chaitu"]="boy"
da["sar"]="500"
print(da)
print(type(da))

print("\n replacing new value\n")
dic={100:"soap",200:"sugar",300:"oil"}
dic[100]="maida"
print(dic)
print(type(dic))

print("\n===============DELETE dictionary=================\n")
print("\n_________1.delete one key-value____________\n")
st={123:"suchi",124:"python",125:"intern"}
del st[123]
print(st)

print("\n_________2.delete complete dict object____________\n")
s={123:"suchi",124:"python",125:"intern"}
del s

print("\n_________3.clear____________\n")
d={"suchi":(1,2,3),"master":(4,5,6)}
d.clear()
print(d)
print("\n_________4.pop______________\n")
dm={1:"aa",2:"bb",3:"cc",4:"dd"}
dm.pop(4)
print(dm)
print(type(dm))
print("\n-------pop item---------- ")
dm={1:"aa",2:"bb",3:"cc",4:"dd"}
print(dm.popitem())

print("\n===============GET dictionary=================\n")
print("\n____get keys from dictionary______\n")
data={100:"suchi",200:"uma",300:"madhu"}
print(data.keys())
print("\n____get values from dictionary______\n")
data={"pen":10,"book":30,"box":50}
print(data.values())

print("\n===============setdefault() dictionary=================\n")
d={1:'a',2:'b',3:'c',4:'d'}
d.setdefault(1,'s')
d.setdefault(0,'m')
print(d)





