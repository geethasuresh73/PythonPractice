parts=["tires","steering wheel","gear","clutch"]
for i in parts:
    print(i)
parts.append("lights")
print (parts)
parts.append("bulbs")
print (parts)
parts.append("lights")
print (parts)
parts.remove("lights")
print (parts)
parts[1]="axle"
print(parts)
#SET
print("*"*80)
parts=set()
parts.add("lights")
print (parts)
parts.add("bulbs")
print (parts)
parts.add("tires")
print (parts)
parts.add("lights")
print (parts)
parts.remove("lights")
print (parts)
#parts[1]="axle"
print(parts)
# set is un ordered and distinct and elements cannot be changed

#TUPLE

parts=tuple("axle")
print(parts)
#parts.append("s")
# cannot add/remove/changed in tuple
print(parts)

#DICTIONARY
dictonary={"a":"Geetha","b":"Suresh","c":"Arjun"}