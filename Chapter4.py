#Dictionary
# used to store data values in key:value pairs
# they are unordered , mutable and don't allow duplicate keys
stud = {
    "name": "vishakha",
    "roll_no": 72,
    "city" : "virar",
    #we can also add list and tuple in dictionary
    "subject" : ["python" , "C" , "java"],
    "topics":("dict" , "set"),
} 
#to access the values
print(stud["name"])
print(stud["topics"])

#to change the value
stud["name"] = "vishakha salvi"
print(stud)

#Nested dictionary
student = {
   "name" : "rahul"  ,
   "subjects" : {
    "java" : 78,
    "c" : 89,
    "maths" :90
   }
}
#print(student)
#if we want to print only subject dictionary
   #print(student["subjects"]["maths"])

# methods in dictionary
# 1. .keys -- returns all the keys
print(list(student.keys()))  #return in list

# 2. .values -- returns all values
print(list(student.values()))

#3. .items --  returns all key value pairs  as tuples
print(student.items())

#4  .get -- returns the key according the value
#print(student["name"])
#print(student.get("name"))

#5 update-- insert the specified items to the dict
stud = {
    "name" : "sanav",
    "age" : 10,
    "grade" :"A",
}
stud.update({"city" : "mumbai"})
#print(stud)

                        #SET
#set is collection of unordered items. each elements in set must be unique and immutable
#we cannot store list and dictionary in set bcz they are mutable
collection = { 1, 2, 3, 4,5, 5, "vishakha"} #duplicate values are ignored
print(type(collection))
print(len(collection))  #total no of items

#to create empty set
#collection = set() # empty set syntax
#print(type(collection))

#methods
 #1 add : add an element
collection.add((90,90,67))   #tuple
print(collection)

 #2 remove :remove element
collection.remove(5)
print(collection)

#3 clear
#collection.clear()
#print(collection)

#4 pop removes a random value
collection = {" hello" , "good afternoon ", "how are yoou ?", "hello", "world"}
print(collection.pop())
print(collection.pop())

# 5 union : combine both set values and returns new set
set1 ={ 1,2,3}
set2 ={3,4,5}
print(set1.union(set2))
print(set1)
print(set2)

# 6 intersection : combines common values and returns new 
print(set1.intersection(set2))

#practice store following word meaning in python dict
#table : a piece of furniture, list of facts & figures
#cat : a small animal

dict = {
    "table" :["a piece of furniture" , "list offacts and figures"],
    "cat" : "a small animal",
}

print(dict)

#pract 2 you are  given a list of subj for students . assume one classromm is required for 1 subj
#how many classroom are needeed by all stud  :python, java , c++, python , js , java, python ,java , c++,c

set3 = {"python" , "java" , "c++" , "python","java" ,"javascript"
          ,"python" , "java", "c++" , "C"}
print(len(set3))
print(set3)

#pract 3 to enter marks of 3 subj fromthe user and store them in dict start with an empty dict add one by one use subj name as key and mrks as value

marks =  {}
x  = int(input("enter phys marks :"))
marks.update({"phys" : x})

y  = int(input("enter maths marks :"))
marks.update({"maths" : y})

z  = int(input("enter history marks :"))
marks.update({"history" : z})

print(marks)

#figure out a way to store 9  and 9.0 as separate values in set
values = {
    ("float" , 9.0),
    ("int" , 0)
}
print(values)
