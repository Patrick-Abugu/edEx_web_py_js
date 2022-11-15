#names of my family members
names = ["Cecilia", "Anayo", "Chijioke", "Juliana", "Chinenye", "Ebere", "Dozie", "Patrick"]
name = input("My name is:")
names.sort()
#print(f"My name is {name} and here are other members of my family:")
#print(f"{names}")

if name in names:
    list.delete(name)
    print(f"My name is {name} and here are other members of my family:")
    print(f"{names}")
print(f"My name is {name} and here are other members of my family:")
print(f"{names}")
#lists are ordered and mutable. they can be added to and removed from.