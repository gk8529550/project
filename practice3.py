print("this is the use of list and their benefites")
#this is accesing element in list.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:4])

#this is method of changing the value in list.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#this is the extend method in list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#this is the adding element in list.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#this is the use of remove or pop element in list.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#this is the use of loop in list.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#this is the use of list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#this is the use of list sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#this is used to add two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


