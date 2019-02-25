print("--------------------1----------------------")
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist)
for x in thislist:
  print("loop:"+x)


print("--------------------2----------------------")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print(len(thislist))
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)
print("--------------------3----------------------")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print("--------------------4turples----------------------")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
#thistuple[1] = "blackcurrant"  # TypeError: 'tuple' object does not support item assignment
for x in thistuple:
  print(x)
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print(len(thistuple))

print("--------------------5set----------------------")
thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)
print("banana" in thisset)
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
print(len(thisset))
thisset.remove("banana")
print(len(thisset))
thisset.discard("banana")
print(len(thisset))
thisset.clear()

print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# del thisset
# print(thisset)
print("--------------------6dictionary----------------------")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["year"])
print("--------")
for x in thisdict:
  print(thisdict[x])
print("--------")
for x in thisdict.values():
  print(x)
print("--------")
for x, y in thisdict.items():
  print(x, y)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
# del thisdict["model"]
# print(thisdict)
thisdict.clear()
print(thisdict)

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
print("--------------------7----------------------")
print("--------------------8----------------------")
print("--------------------9----------------------")
print("--------------------10----------------------")

