#next line
strl1 = "this is a string. \n we are creating it in python"
print(strl1)

#concatenation
str1 = "vishakha"
str2 = "salvi"
finalstring = str1 + str2
print(finalstring)

#length ofstr
string = "vishakha"
len1 = len(string)
print(len1)

#indexing
print(string[5])

#slicing
print(string[1:4])#ish
print(string[1:]) #ishakha
print(string[:8])#vishakha

#endwith (function)
string1 = "hello my name is vishakha salvi"
print(string1.endswith("lvi")) #returns true

#capitalize(function) capitalize 1 character
string2 = "i stay in virar"  #returns i as I
print(string2.capitalize())
print(str) #will return the original string
#string2 = string2.capitalize  now it will store the modified string in string2 
#print(string2)

#replace function
string3 = "i am studing python"
print(string3.replace("am","'m"))

#find(function)
string4= "vidyavardhini's college of engineering and technology"
print(string4.find("college"))

#count(function)
string4 = "hello"
print(string4.count("ll"))

#practice ques 1 wap to input users first name and print its length
##name = input("enter your name :")
#print("length is ",len(name))

#prac ques 2 to find occurence of $ in a string
string5 = "salary is $200 , $600"
print(string5.count("$"))

#conditional statements:
#age = 21
#if (age >= 18):
  #  print("can  vote and apply for licence")

#elif statement: it will check the if stmt if it is false then only it will check elif stmt otherwise if it is true then it will not check and print the if stmt
light = "green"
if (light=="red"):
    print("stop")
elif (light == "green"):
 print("go")
elif (light=="yellow"):
    print("look")
    

#if-elif-else stmt:

light = "orange"
if (light=="red"):
    print("stop")
elif (light == "green"):
 print("go")
elif (light=="yellow"):
    print("look")
else:
    print("light is broken")


#if-else stmt:

age = 14
if(age >= 18):
    print("can vote")
else:
    print("cannot vote")

#conditional-stmts
marks = 90
if (marks >= 90):
    print("Your grade is A")
elif(marks >= 80 and marks < 90):
    print("Your grade is B")
elif(marks >=70 and marks < 80 ):
    print("Your grade is C")
else:
    print("grade is D")

#nesting
age = 55
if (age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
         print("can drive")
else:
    print("cannot drive")

# practice ques to check if a number entered by the user is odd or even
#num=  int(input("enter a number:"))
#if (num % 2 == 0):
  #  print("number is even")
#else:
 #   print("number is odd")

#practice ques to find greates of 3 number entered by user
#num1 = int (input("enter 1 number"))
#num2= int (input("enter 2 number"))
#num3 = int (input("enter 3 number"))

#if (num1 >= num2 and num1>= num3 ):
#    print("num 1 is greatest")
#elif(num2 > num3):
#    print("num2 is greatest")  
#else:
 #   print("num 3 is greatest")

#practice ques if a number is multiple of 7 or not

number = 49
if (number % 7 == 0):
 print("it is multiple of 7")
else:
    print("it is not a multiple of 7")


