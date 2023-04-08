import copy
L1=[1,2,[3,5],4]
#creating a shallow copy
L2=copy.copy(L1)
# In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
# In python, this is implemented using “copy()” function.
# original elements of list

#creating a deep copy
L3=copy.deepcopy(L1)
print("original elements before shallowcopy")
for i in range(len(L1)):
    print(L1[i],end=" ")

print("\r")
L2[2][0]=7
print("original elements after shallowcopy")
for i in range(len(L1)):
    print(L1[i],end=" ")
# In case of deep copy, a copy of object is copied in other object.
# It means that any changes made to a copy of object do not reflect in the original object.
# In python, this is implemented using “deepcopy()” function.
L3[2][0]=8
print("L3 elements after deep copy")
for i in range(len(L3)):
    print(L3[i],end=" ")

print("L1 elements after deepcopy")
for i in range(len(L1)):
    print(L1[i],end=" ")

