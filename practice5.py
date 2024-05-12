print("this is the use of tuple in python")

#here we will discussing about tuple how to work in python program.
#printing only one element in index.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#print element at last.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#print element at the priority basis.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#print element at the numbering form.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#add the element in tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add element using append method.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#add element in index.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#print element alter to another
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#using whie loop in tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#using for loop in tuple
thistuple = ("apple", "banana", "cherry",12344,"heypineapple")
for i in range(len(thistuple)):
  print(thistuple[i])

#add tuple
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuple with 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
