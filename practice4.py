print("this is the use of sets in python")

#check element is present in index
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#add element in index
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#add both index in one frame
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#delete element in the index
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#delete element in index using pop method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

#union method and add the element.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

