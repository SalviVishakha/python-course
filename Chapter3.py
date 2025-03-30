#List 
# list uses [] brackets
#a built in data type that store set of values. it can store elements of different types
marks = [52,56,89,74]
print(len(marks))  #length of list
print(type(marks))
print(marks[0])

#store different data types
student = ["rahul" , 21, "virar"]
print(student)
student[2] = "saphale"
print(student)

#STRINGS ARE IMMUTABLE IN PYTHON
#LIST ARE MUTABLE IN PYTHON


# list slicing
list1 =[58, 59 ,87, 45,75]
print(list1[1:4])
print(list1[:4])
print(list1[1:])

#list method
#1 append method : add one element add the end of the list
list1.append(78)
print(list1)

#2 sort method : sorts in ascending order
print(list1.sort())
print(list1)

#3 descending order : 
print(list1.sort(reverse = True))
print(list1)

list2 = ["lily" , "rose" , "hibiscus" , "tulsi"]
print(list2.sort(reverse = True))
print(list2)
print(list2.sort())
print(list2)

#reverse method : it reverse the element in original list
print(list2.reverse())
print(list2)

#insert method : insert element at any index
list2.insert(1,"mogra")
print(list2)

#remove method :to remove the first  occurence of elements
list3 = [ 4, 5,5, 6, 9]
list3.pop(4)
print(list3)

#Tuples : built in data types  to create immutable sequences of values
Tuples = (54,58,89)
print(type(Tuples))
print(Tuples[2])

Tuples = ()
print(Tuples)
print(type(Tuples))

Tuples= (1,)
print(Tuples)
print(type(Tuples)) #it will consider as tuple

Tuples = (1)
print(Tuples)
print(type(Tuples)) #it will consider as integer

#slicing in tuple
Tuples = (1,2,3,4)
print(Tuples[1:3])

#methods in tuple

#1. index :returns index of first occurences
Tuples = (1, 2, 3, 1 , 1) 
print(Tuples.index(2)) # 2 is the element and it willreturn its index as 1

#2. count : count hte total occurences of the element
print(Tuples.count(1))

#pract to ask the user to enter names of their 3 fav moies and store themin list
#movies = []
#mov1 = input("enter movie no 1 : ")
#mov2= input("enter movie no 2 : ")
#mov3 = input("enter movie no 3 : ")
#movies.append(mov1)
#movies.append(mov2)
#movies.append(mov3)
#print(movies)

#pract to check if a list contains a palindrome of elements
palindr = [ 1, 2, 1]
palindr1 = [ 1, 2, 3 ]
copy_palindr= palindr.copy()
copy_palindr.reverse()
if (copy_palindr  == palindr ):
    print("palindrome")
else:
    print("not palindrome")

#to count the no  of students with "A" grade in the  tuple
grades = ("C" , "D", "A", "A", "B", "B" , "A")
print(grades.count("A"))

#store the above values in a list and sort them from "A to D"

grades = ["C" , "D", "A", "A", "B", "B" , "A"]
print(grades.sort())
print(grades)