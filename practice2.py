'''thisdict =	{
  "Name": "Rahul",
  "college name": "maharhi markandeshwar(deemed to be univesity)",
  "course": "BCA",
  "roll no.": 1322275,
  "section":"D"
}
print(thisdict)
#print only first word which is name.
x = thisdict["Name"]
print(x)

#print only second word which is college.
y=thisdict["college name"]
print(y)

#this is use only change word one into another.
thisdict["course"] = "BTECH"
print(thisdict)

#this is the use only add the new event in program.
thisdict.update({"color": "red"})
print(thisdict)

#this is used only delete any element in dictionay using pop method.
thisdict.pop("section")
print(thisdict)'''

#this is the use of nested loop in dictionary
myfamily = {
  "grocery" : {
    "name" : "rice",
    "name1" : "wheat",
    "year" : 2024
  },
  "electronics" : {
    "name" : "fan",
    "name1" :"air conditionar",
    "year" : 2024
  },
  "protein" : {
    "name" : "milk",
    "name1" : "horlicks",
    "year" : 2024
  }
}

print(myfamily)

