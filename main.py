print("Hello world")
print(3+5)
print("How are you?")
print("Shut up!")
import cv2
import math
print(math.gcd(12,69))
a=8
b=6
c=2
print(a+b+c)
print(a*c)
print(b/c)
print(b-c-a)
print(c+3)
print(c)
print(8)
print(type(c))
print("Disha")
d=3.14
print(type(d))
e="12"
e=int(12)
e=float(e)
print(e-2)
#f=Disha
#print(type(f))
#e=float(e)
f=11
f=str(f)
f=float(f)
print(f+1)
g=1.0
#g=str(g)
#g=int(g)
print(g+1)
name="Disha"
print(name[0])
print(name[0:5])
print(name[1:4])
print(name[1:5])
print(len(name))
var=name.lower()
var=name.upper()
print(var)
print("My name is Disha")
print(85.2+56)
print("Hi")
var=name.replace("i","e")
print(var)
var=name.replace("e","i")
print(var)
str1="A friend in need "
str2="is a friend indeed"
print(str1+str2)
name1="Disha"
name2="Deepali"
temp=f"{name1} is very intelligent as compared to {name2}."
print(temp)
'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary
'''

# In front of (.) it will come something {a=(1,2,3)} a
# .remove(str/int/float) means it will remove particular thing in the bracket
# .clear()
# .append(str/int/float) means it will add (str/int/float) at last
# .discard(str/int/float) means it will remove something if presant if not presant it will not show error
# .pop() means it will remove (str/int/float) presant at last
# .insert(2,50) means in this 2 indicates position/place and it will be changed by 50
# .add(str/int/float) similar to append

# 1.List
lst= [61,22,5,8,9,62]
var = type(lst)
var = lst[0:6]
lst[2]=8
var=lst[2]
lst.append(900)
lst.append(0)
var=lst
var=len(lst)
lst.insert(2,50)
lst.remove(8)
lst.pop()
var=lst
var=len(lst)
lst.remove(22)
lst.remove(61)
lst.remove(8)
lst.remove(9)
lst.remove(62)
var=len(lst)
var=lst
print(var)

# 2.Tuple
a=("Disha", "Deepali", "Devendra")
var=a
print(type(a))
a=list(a)
var=a
a[1]="Gudiya"
var.clear()
print(var)

# 3. Sets
s1 = {1,2,3,2,3,6,5,2,1}
s1.add(12)
s1.update([13,40,50,60])
s1.discard(8)
s1.clear()
print(s1)



