##THE MOST IMPORTANT TOPICS

#1.ARRAYS
#2.STRINGS
#3.STACK
#4.QUEUE
#5.RECURSION
#6.BINARY SEARCH
#7.DYNAMIC PROGRAMMING
#8.TREES AND GRAPHS

age=25
print(age, type(age))

price =99.99
print(price, type(price))

name ='salai'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

address = None
print(address, type(address))

x=10
x="hai"
x=3.14
print(x)

##python variable scope and python file time
#L>E>G>B
#LOCAL > ENCLOSING > GLOBAL > BUILT-IN

#L
#only calls in that particular function not another function

def order():
    food="tomato rice"
    print("your order is :", food)

order()  
print("food")  

#E
#checkout ku outer la irrukaratha inneruku access panna mudiyum

def card():
    discount=10

    def checkout():
        print("applaying discount :",discount)

        checkout()

card()

#G
#global variable can be accessed by any function in the file
#globl la eathuvenalum use panalam athukula mattum function la use panna mudiyum

user_id="salai123"
def homepage():
    print("welcome:", user_id)
def profile():
        print("welcome to the profile page:",user_id)
homepage()
profile()      

#B
#python inbuild function can be used any where in the file
#bilt in functionum irruku and variablrum global la irruku

print(__file__)

#L local na function la create pandrathu
#E outer la irrukatha athoda inner function la access panna mudiyum
#G ellafunction la use panna mudiyum
#B variable and function ellam use panna mudiyum

#type casting and type checking

#type casting is converting one data type to another data type

x="10"
y='5'
print(type(x))
print(type(y))

#type cheacking is called using type() function to know the data type of a variable

x="10.5"
print(type(float(x)))

#operater and expression

a=10
b=3

#arithematic operaters
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a%b)  #modulus
print(a**b) #exponentiation #10*10*10
print(a // b) #floor division #point ku aprom varatha remove panidum

#comparisn operaters
x=5
y=10
print(x==y)  #equal to
print(x!=y)  #not equal to
print(x>y)   #greater than
print(x<y)   #less than

##logical 
g=True 
v=False
print(g and v)
print (g or v)
print(not g) 

amount = 1200
tax = amount * 0.18
total = amount + tax
print (total)
if total > 1000 :
    discount = total * 0.10
    total -= discount
print(total)


#logical and comparisn operaters using ...
age = 16
student = 'yes'

if  age >= 60 or student=='yes': #and this is a condition block
    print("yes discount")
else:
    print("no discount")  

# INPUT FUNCTION
a = int(input("enter number one :")) #input namba vagura value ellam string ahh mathirum
b= int(input("enter number two :"))   #int nuu podumpothu string ku mathidum

print(a+b)

##string handling and string manipulation

'''string manipulation'''

owner_name ="salaimahaprasad r"

print(owner_name.lower())
print(owner_name.upper())
print(owner_name.capitalize())




mobile="5511111199"# * operation is called  masked number
masked=mobile[:2]# first two number venummuna : munadivaikanum , athey last two number venummuna -2: use pannanum
print(masked)

masked= mobile[:2] +"******"+mobile[-2:]# center number ahh star panni display panrathu

song="mutta BAMAA mutta BAMAA"
artist="dhAnuSh"
# ipo nama renduu use case la irrukara line la first alphabets ahh capitalise pannanum 
# f-strinf na formatted string nu meaning
formatted=f"{song.title()} - {artist.title()}"
print(formatted)

#replace function
location="chennai central"
fixed_location=location.replace(__old:"chennai central",__new:"Thambaram")
print(fixed_location)

#how to take booling id 
message="your booking id is : USB12345. please keep it safe"
booking_id=message.split(":")[1].split(".")[0].split()#last la .split mattum eaduthuta output la bracket varatu
print(booking_id)

#1,salai,19,namakkal intha mari coma potamari vanthuchina athu (delimit) nu solovaga

promo_msg="use zomato100 to get 100rs off on your first order"
# intha line lazomato100 ahh eduthutu print pannanum
if "zomato100" in promo_msg:
    print("offer applied")


feedback="my maths mam is a good teacher"
# Find the position of "mam" in the feedback string like 0123456789 is mam position
print("position is:", feedback.find("mam"))

name="salai ravi"
initials=([word[0].upper() for word in name.split()])
# ithula vara output ahh join pananum naa ("".join) intha concept ahh use pananum
print(initials)


dierty_input="    software    "
clean=dierty_input.strip()
#strip is used to remove extra spaces in the starting and ending of the string
print((clean))



#condition statements
age=30
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
    
    
#Another example
marks=75

if marks>=90:
    print("A grade")    
    
elif marks>=75:
    print("B grade")    
 
elif marks>=60:
    print("C grade")

else:
    print("fail")   
    
    
 #nested if else   
 #orey condition la rendu vela panna mudiyathu apde rendu pananum na nested if else use pannuvom

age = 18
has_licsence = 'yes'  

if age >= 18:
    if has_licsence == 'yes':
        print ("you can drive")
    else:
        print("you cannot deiive without licesnse")     
        
mark =70
attendance = 80

if mark >=60 or attendance >=75: # or condition used for either one condition is true
    print(" eligible for exam")  
else:
    print("not eligible for exam")
    
    
recharge = 200 
data_balance =1.5
 
 
if recharge >=399 or data_balance >=1:
    print("you are eligible for bonous data")
else:
    print("you are eligible")        


correct_pin ='1234'
entered_pin =''

while entered_pin != correct_pin:
    entered_pin = input("enter your correct pin :")
    
print("access granted")    #correct ana pin kedaikuravarikum run aiitey tha irrukum


#break ststement
for i in range(10):
    if i ==5:
        break
    print(i)
    
#continue statement    
n=[10,-3,25,0,-7,8]

for num in n:
    if num <0:
        continue    
    print(num)   
    
count = 5

while count > 0:
    print(f"Countdown:{count}")
    count -= 1 #it will be reducet one by one
    
items = []

while True:
    item = input("add item (type 'done' to finish): ")
    if item.lower() == 'done':
        break
    items.append(item)

print("items in cart:", items) #it will be used for flipcart , supermarket.        
       
    

#FUNCTION means method
#its a block of reusable code
#oru function ahh nama eapde define pananun na (def) nu irukura key word ahh tha use pananum

def great():
    print("hello friends!")
    
    
great()    #ipde tha function ahh call panaum


def great(name):
    print(f"Hello {name},welcome!")
    
great("Salai") # i have a car then the key is used to start the car is called argument
  


##difference between return and print
#print
def add(a,b):
    print(a+b)

result = add(1,3)
print(result)

#return
def add(a,b):
    return(a+b)

result = add(1,3)
print(result)

    
def add(*args):
    total=0
    for num in args:
        total += num
    return total
print(add(1,2,3))    



##keyword arguments
def create_profile(**kwargs):
    print("User profile")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
        create_profile(name="salai",age=25,job="software developer")
        
#output:          
##User profile
#name :salai >key:value
#age :25    
#job :software developer


#a=[1,6.0,"salai"]
#1 is integervalue
#6.0 is float value
#"salai" is string value


#LISTS
#creating list for different apps
playlist =["song1", "song2", "song3", "song4", "song5"]
favourite_food =["biryani", "chicken", "mutton","fish"]
recent_locations =["chennai", "bangalore", "hyderabad", "japan"]

print("spotify playlist:", playlist)
print("Zomato foods:",favourite_food)
print("uber locations:",recent_locations)



#list methods 
playlist =["song1", "song2", "song3", "song4", "song5"]
print("spotify playlist:",playlist)


playlist.append("song6") #append eapovum last la tha add agum
print("after append",playlist)

playlist.insert(1,"song2.2")#position 0,1,2,3 are there
print("after_insert",playlist)

playlist.remove("song3")
print("after removing",playlist)#same ithulayee remove ku bathilahh pop potom naa last la irrukuratha del panidum




#list slicing
playlist =["song1", "song2", "song3", "song4", "song5"]

print("top 2 songs", playlist[0:2])



#list iteration it is mutable
favourite_food =["biryani", "chicken", "mutton","fish"]
print("Zomato foods:",favourite_food)

for food in favourite_food:
    print("all food", food)


recent_location =["home","airport","work","gym"] #beyond the location o 1s 2s that type of list 
for i,location in enumerate(recent_location):
    print(f"location {i}:{location}")
    
    
    #TUPLES
    #order ahh maintain pannum and "it is imutable"
    trip_summary=("ubergo","chennai","airport","450.00","completed")
#print(trip_summary)

#print(trip_summary[2])

for item in trip_summary:
    print(item) #ithu loop mari order ah irrukum
    #print(len(trip_summary)) ipde(length) kudutha eathena irrukunu kaminkum

    #set namba use panunpothu common ahh irrukurathathaa tha once print pannum
    uber_cities=["chennai","bangalore","chennai","delhi","bangalore"]

unique_cities=set(uber_cities)
print(unique_cities)



#union intersection and difference

uber_cities1={"chennai","munbai","bangalore"}
uber_cities2={"bangalore","delhi","hyd"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities1.difference(uber_cities2))
#same ithayee namba add panikaalam 
uber_cities1.add("karur")
print(uber_cities1)    
    
    
    
my_set={1,2,3}

my_set.remove(3)
my_set.add(33)
print(my_set)  


#dictionary ku square bracket podanum  


#dictionary

trip={
    "trip_id":"UB12345", #keys and values
    "pickup":"chennai central",
    "drop":"airport",
    "fare":430.75,
    "driver":"ravi",
    "status":"completed",
    "trip_id":"UB12345"
    
    }
print(trip["pickup"])#ithuku name tha lookup
print(trip.get("pickup"))
print(trip.get("airport"))
print(trip.keys())
print(trip.values())


for key,value in trip.items():
    print(key,":",value)
    
    
    
trip.update({"car_model":"SUZUKI"})
print(trip)

trip.update({"car_model":"abc"})
print(trip) #ithula irrukanu paakum apde illa na athuveyy add panikum athuku peru tha #(upsert)
    
for k,v in trip.items():
    print(k,":",v)   #used to control the latest which means : last ahh eatha update pandraamoo atha tha eaduthukum    
    
    

#intha topic oops keela varum
# class and object

    
# OOP example: class and object
class Student:
    def say_hello(self):
        print("Hi, i'm a student!")

s1 = Student()
s1.say_hello()



class MathTool:
    
    def square(self, n):
        return n*n
    
    
    def cube(self, n):
        return n*n*n 
 #this is constructor   
tool = MathTool()
print(tool.square(4))  # Output: 16



# inheritance in important to test
# 1.Re use the code
# 2.parent child relationship is called inheritance

class dad:   #parent
    def house(self):
        print("i am from dad class")
        
        
class son(dad):  #child
    def factory(self):
        print("i am from factory class")    
        
s=son()
s.house()#re use the code from parent class            
s.factory()   #single level inheritance     



#if and if else , elif
if (10>5): # (:) means intha sectence correct ahh irruntha next sentence poogum
    print("True")
    
a=9 
if a==10:
    print('equal')
elif a==9:
    print('a is 9')
else:
    print('Not equal')      
    
    
    
class app1: #parent child
    def v1 (self):
        print("orders")   
        

class app_1(app1): #child class
    def v2(self):
        print("refund")      
        
a=app_1()
a.v1()
a.v2()   # parent class not completeted




# Access specifier and acceser modifier
#public , private and protected

#public na ellam access panna mudiyum
#protected na _ onu mattum irrukum 
#private na __ onu mattum irrukum


#Mode file handeling
#'r' Read only (file must exist)
#'w' write only (over writes or creates)
#'a' Append only (adds to end of life)
#'r+' Read + write (file must exist)
#'w+' Write + read (overwrites or creates)
#'a+' Append + read (creates if not exists)
#'rb' Read binary
#'wb' Write binary
#'ab' Append binary




file = open("notes.txt", "w")
file.write("welcome to python File Handling!\n")
file.write("This is a new file.\n")
file.close()

#run panum pothu notes.txt nu onu create agum. athula "welcome to python File Handling!" and "This is a new file." nu rendu line ezhuthum.            
    

    
    
# variable decaraction in python
#camel 
'someName' 
#second letter ahh uppercase la vachirukarathutha camel case

#pacsal
'SalaiMahaPrasad' #3nu words first letter ahh uppercase la vachirukarathutha pascal case

#snake
'my_variable_name' #specefic ahh underscore use panni variable name declare panrathu snake case    
    
    
# Datatypes
a="salai"
print(type(a))  #a la kuduthu irrukarathu enna value nu pakurathuku namba intha type use panuvom  
    
 #float
 #decimal point  eg: 3.14
 
 #list

a=[1,2,3,4,5] 
print(type(a)) #list la irukura value enna type nu pakurathuku intha type use panuvom
# square bracket la irrukuruthu tha list

#tuple
a=1,2,3,4,5
print(type(a)) # square bracket illahhma kudutha athu tuple


#set 
a={1,2,3}
print(type(a)) #ipde kudutha thu set bracket


#dictionary
a={"pen":5,"pencil":10,"eraser":3}
print(type(a))   
    

#Exception handeling in python
print("welcome to Zomato!")
number_of_items = int(input("How many items ?"))
total_price = 200 * number_of_items
average_price = total_price/number_of_items
print("Average price per item:", average_price)
    
    


# encripted DESCRIPTED is not understand
    
    # HIGHERER ORDER FUNCTION
    # Takes another function as an srguement or
    # Returns a function as its output.
    
    #used to make code more flexible, reusable, and dynamic. 
    
def build_email(username,provider):
    if provider =="gmail":
        return f"{username}@gmail.com"
    elif provider == "ymail":
        return f"{username}@ymail.com"
    elif provider == "hotmail":
        return f"{username}@hotmail.com"
    else:
        return f"{username}@example.com"

print(build_email("salai","gmail"))
print(build_email("sabari","ymail"))
print(build_email("vishnu","hotmail"))
print(build_email("prasad","unknown"))



# lamda function 

add= lambda a,b: a+b
print(add(1,2))    
    
square = lambda x: x**x
print(square(4))

# 1. lambda map
# 2. lambda filter
# 3.lambda reduce
fruits = ["apple","Banana","Mango"]
result = list(map(lambda fruit: fruit.upper(), fruits))
print(result)

nums = [1,2,3,4,5]
even = list(filter(lambda x: x%2==0, nums))
print(even)   


from ast import pattern
from copyreg import pickle
from functools import reduce
import os
import zipfile #this condition will be used
nums = [1,2,3,4,5]
total =  reduce(lambda a,b : a+b, nums)
print(total) 



from functools import reduce

nums = [10,3,55,34,22]
maxi=reduce(lambda a,b: a if a>b else b, nums)
print(maxi)


from functools import reduce

prices = [100,200, 300, 1700, 1500]
expesive = list(filter(lambda x: x > 1000, prices))
total = reduce(lambda a,b:a+b , expesive)
print(total)


#closure
def outer(msg):
    def inner():
        return f"Message is :{msg}"
    return inner

say_hai =outer("Vanakam da mapla")
print(say_hai())
    
    
#partially applied function
#ipo rendu argument kuduka vendiya ideathula onu kudutha pothum


def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)  


print(calculate_price(1000,0.18))  
print(calculate_price(500,0.18))


#partially applied function
#ipo rendu argument kuduka vendiya ideathula onu kudutha pothum


from functools import partial

#step 1 Define the original function
def calculate_price(base_price,tax_rate):
    return base_price * (1 + tax_rate)

#step 2 Create a partially applied function with gst
price_with_gst = partial(calculate_price,tax_rate=0.18)


#step 3 no use it without passing tax_rate again
print(price_with_gst(1000))   # 1180.0
print(price_with_gst(500))   # 590.0
        
# OOPS : OBJECT ORIENTED PROGRAMMING
#ENCAPLUSATION 
#INHERITANCE
#POLUMORPHISM
#ABSTRACTION    
 
#OOPS: CLASS AND OBJECT
     
class customer:
    bank_name="abcd bank"
   
c1 = customer()
print(c1.bank_name)#customer class la irukura bank name ahh c1 object la access panrathu        
    
c2 = customer()   
print(c2.bank_name) #customer class la irukura bank name ahh c2 object la access panrathu 
    
 #methods(function)
def greet(self):
     print("hai and welcome to abcd bank")
     
c1 = customer()
c1.greet()

c2 = customer()
c2.greet() #customer class la irukura great method ahh c2 object la access panrathu    
    
    
        
class Customer:
    bank_name = "HDFC Bank"
    
    def __init__(self, name , age, initial_amount):
        self.name = name
        self.age = age
        self.balance = initial_amount
        
    def deposit(self, amount):
        self.balance += amount
        print(f"deposit of ${amount} is scussesfull. Updated balance is ${self.balance}")  
        
c1 =Customer("John", 31, 5000)
c2 =Customer("Anna", 40, 7000)

c1.deposit(300)
c2.deposit(100000)          
        
    
class Engine:
    def __init__(self):
        self.power = 100
        
    def start(self):
        print("engine Starts")    
    
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def move(self):
        self.engine.start()
        print("Car is Moving")   

c = Car()
c.move()        
    
    
country = "India"

if country == "India":
    print("IN")    
elif country == "United states":
    print("USA")
elif country =="japan":
    print("jp")
    
#while loop is working on condition
#for loop is working on range
#if na oruthadavaa 
#while na thirumba thirunba 
    
a= [1,2,3,4,5]

index = 0

while index<len(a):
    print(a[index])
    index +=1    
    
    
    
class Students:
    School_name = "ABCD School"
    
    def __init__(self, name, age): #init is a automatically created abject constructor, self refers to the current object
        self.name = name
        self.age = age
        
    def display(self): #specefic object 
        print(f"name:{self.name},{self.age}")
        
    @classmethod
    def get_school_name(cls):# class method means works with specefic, cla refers to the class itself, not the object
        return cls.School_name
    
    @staticmethod
    def is_adult(age):#it does not use self or class, like normal function palced inside the class
        return age >= 18

x = Students("john", 31)
x.display()
print(Students.get_school_name())

print(x.is_adult(x.age))
print(Students.is_adult(31))
    
    
class Engine:
    def __init__(self):
        self.power = 100
        
    def start(self):
        print("engine Starts")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def move(self):
        self.engine.start()
        print("Car is Moving")
        
c = Car()


class Outer:
    def __init__(self):
        self.x =10
        
    class Inner:
        def __init__(self):
            self.y = 20
            
        def display(self):
            print("inner Class")
            
        def display(self):
            print("Outer Class")
            
out =outer()
in_ =out.Inner()



#encaplusation

class Car:
    _price = 5000
    
    def display_price(self):
        print(F"{self.__price} is the cost of the car")
        
    
c1 =Car()
print(c1._price)


sum = 0
for i in range(1,6):
    sum +=i
    if i<5:
        print(i, end="+")
    else:
        print(i, end="=")    
print(sum)

    
    
# inheritance

"single level inheritance"
"multiple level inheritance"
"muliti level inheritane" '>' "parent intermediatory child"
"hierarchical inheritance"

# inheritance

class A:
    def A(self):
        print("I am A")#parent
        
class B:
    def B(self):
        print("I am B")#child
 
class C:#c(a,b)
    def C(self): 
        print("I am C")#child        
        
#obj=B()
#bj.B()

obj = C()
obj.A()
obj.B()
obj.C()


# CONSTRUCTORS
class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class child(Parent):#super
    def __init__(self, name, age, school):
        Parent.__init__(self, name, age)
        self.school = school
        
obj = child("John", 31, "ABCD")
print(obj.name)
print(obj.age)
print(obj.school)


# polymorphism
#Method resolution order
#c3 algorithm
#DFS- depth first search
#LTR- left ot right
#BFS- breath first search


#poly- Overloading and overriding

def f1():
    print("ONE")
    
def f1():
    print("TWO")
    
def f1():
    print("THREE")
    

f1()    



#poly- Overloading and overriding

def f1(x, y=None,z=None):
    if y and z:
        print(x * y * z)
    elif y:
        print(x + y)
    else:
        print(x)

f1(10)
f1(10, 20)
f1(10, 20, 30)


#duck typing
def add_number(a, b):
    return a + b

print(add_number(10, 20))
print(add_number("Hello ", "World"))#after hello we give the (gap)    
    
    
#Errors and Exceptions 
try:
    print("Hello")
    print(10/0)
    
except:
    print("Error occurs")
else:
    print("No Error occurs")
finally:
    print("This block runs irrespective")
    
    
    
class InvalidNumber(Exception):
    pass


x = int(input("Enter a number between and 10:"))
if 0<= x <=10:
    print("Correct Value")
else:
    raise InvalidNumber(f"{x} is not in the range of 0 and 10")


number = int(input("enter the number: "))
z = int(input("Enter the divisor (z): "))

remainder = number % z
print("This remainder is:", remainder)


# Get two numbers from the user
num1 = float(input("Enter the first number: "))# number nu vantha float tha kudukamum 
num2 = float(input("Enter the second number: "))

# Calculate the average
average = (num1 + num2) / 2 #avg means divide pananum

# Display the result
print("The average is:", average) 


##file handling & threads
#open(filename, mode)
#mode:
#r(Default): Read
#w: Write 
#x: create

with("DOES_NOT_EXIST2.txt","w") as f:
    f.write("\nThis is form the APPEND mode") # a new file will be created if it does not exist, and the content will be appended to the file if it already exists.
    

#pickle
#pickle is consists of tho
#load() and dump() methods


#serilisation: dump()
results = {'a':1, 'b':2, 'c':3}#pickle takes a data converts the into (bytes)
with open('pickle.bin', 'wb') as f: # 'wb' mode for writing in binary format. like xt,st (t) is txt file
    pickle.dump(results, f)# Serialize and write the dictionary to the file
    f.close
    
# De-Serilations: load()
with open('pickle.bin', 'rb') as f:# pickle is like a note pad
    print(f.tell())
    x = pickle.lead(f)
    print(f.tell())
    
print(x)
print(type(x))
    
    
#zipfile , built in module is called zip module

with zipfile.ZipFile("python_course.zip", "w") as archive: # w means read mode
    archive.write("does_not_Exist.txt")
    archive.write("does_not_Exist2.txt")
    archive.write("Trail.txt")  # once we run it will create a zip file called python_course.zip and add the specified files to it. If the files do not exist, it will raise an error.

with zipfile.ZipFile("python_course.zip", "r") as archive:# r means read mode      
          
import os    
os.mkdir("course")#it will make a directory and it will create a folder called course in the current working directory. If the folder already exists, it will raise an error.
os.rmdir('course')#it will delete the folder called course from the current working directory. If the folder does not exist, it will raise an error.   
print(os.getcwd())#it will print the current working directory. It will return the absolute path of the current working directory as a string. If you want to change the current working directory, you can use os.chdir(path) method, where path is the new directory you want to set as the current working directory.    
os.chdir("course")#it will change the current working directory to the folder called course. If the folder does not exist, it will raise an error.
print(os.path.exists("course"))#it will check if the folder called course exists in the current working directory. It will return True if the folder exists, and False if it does not exist.
print(os.listdir())#it will list all the files and folders in the current working directory. It will return a list of strings, where each string is the name of a file or folder in the current working directory. If the current working directory is empty, it will return an empty list.    
    
    
    

#Regular, Regular Expresion , inbuilt modele is called re
import re
text= "hai iam salaimahaprasad"
pattern="a"

#find all()
x=re.findall(pattern, text)
print(x)

#search()
x=re.search(pattern, text)
print(x)
print(x.span())#index   range ahh found pannum means a to a ku irrukura range ah find pannum
print(x.string())#mela kudutha <text> print ahhgum
print(x.group())#namba enna letter search pana kuduthom ohh (a) antha letter print ahhgum


#split()
x=re.split(pattern, text, 2)#split na <text> la ipo 2 kuduthom na (hai , iam) eaduthkum athula (a) mattum rm panudum aprom split pani kamikum 
print(x)


#substitute()
x=re.sub(pattern, "***", text, 2)# (a) irrukura eaduthula (*)star print ahhgum athutha sub.
print(x)

######
 
import re 
text = "hello iam salaimahaprasad"
pattern = 'a','a.*$',"hello$"#intha string kudukumpothu string la end ahhnamattum tha print ahhgym illa na print ahhgathu

x=re.findall(pattern, text)
print(x)#ithu la (a)+beside letter print ahhum
    
    
import re
txt = "hello salai I am a python dveloper"
pattern =r\"ba"   ##r is a rare string and a is check txt statement and b is a begining word , D put all letter will seperate show

x= re.findall(pattern, txt)
print(x)

if x:
    print("There is a match")
else:
    print("it is not match")
    


#multi threading

# it could be 
# 1.(multipl task) to run the multiple task
#1. threads . share the same memory space
# 2.process . independent unit of exceution and don't share the resources with the other process


#1.1 use of thread

#concurrent execution 
#parallel processing
# network communication
#user interface
#background tasks
#asynchronous programming
#multi threading

#import threading

def my_function(arg1, arg2):
    print("Running my function with args:", arg1, arg2)
    
#create a thread
t=threading.Thread(target=my_function, args=(1,2))


#starting the thread
t.start()

print("main Thread running")

#wait for the thread 
t.join()
print("Thread has complete")


#Thread class methods
#1. start()
#2. join([time])
#3. is_alive()
#4. getName()
#5. setName()
#6. daemon
#7. set Deamon(bool true) non deman theread(bool false)
#8. ident
#9. exit()
#10.raiseExe(exe)

#multitasking using multiole thread in python

import threading
import time

def task1():
    print("task 1 started")
    time.sleep(5)
    print("task 1 completed")
    
def task2():
    print("task 2 completed")
    time.sleep(3)
    print("task 2 completed")

t1= threading.thread(target=task1)
t2= threading.thread(target=task2)

t1.start()
t2.start()

#wait for both thread
t1.join()
t2.join()

print("All tasks completed")

#####
from concurrent.features import threadpoolexecution
import time

def task1():
    print("task 1 started")
    time.sleep(5)
    print("task 1 completed")
    return "task1"
    
def task2():
    print("task 2 completed")
    time.sleep(3)
    print("task 2 completed")
    return "task 2"

#Creating a thread pool with 2 worker thread
with threadpoolexecution(max_workers=2) as executer:
    task1_future = executer.submit(task1)
    task2_future = executer.submit(task2)
    
# wait for both task
task1_result = task1_future.result()
task2_result = task2_future.result()
print("All tasks completed")

# Thread Synchronisation (lock and Semaphore)
#lock : only one thread can acess a shared resources at a time
#semaphone: a limited number of threads to access a resourse at the same time.
            #(multiple threads based on premits)
            

# same ithey tha (semaphone) mattum change panuna pothum
import threading
import time

lock = threading.lock()

def task1():
    #Acquire a lock
    lock.acquire()
    print("Task 1 started")
    time.sleep(5)
    print("Task 1 completed")
    #release the lock
    lock.release()

def task2():
    #Acquire a lock
    lock.acquire()
    print("Task 2 started")
    time.sleep(5)
    print("Task 2 completed")
    #Release the lock
    lock.release()
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

#wait for both thread
t1.join()
t2.join()

print("All tasks completed")# limit the number no thread can access

## deadlocks
#dead lock is a situation two are more processor or threads are forever
# eg processor P1 kitta Resourse R1 irruku. athuku R2 venum.
# eg processor p2 kitta Resource R1 irruku. athuku R1 venum.

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def task1():
    lock1.acquire()
    print('Task 1 acequired Lock1')
    
    lock2.acquire()
    print('Task 1 acequired Lock2')
    
    time.sleep(5)
    print('Task 1 completed')
    
    lock2.release()
    lock1.release()
    
    
def task2():
    lock2.acquire()
    print('Task 2 acquired Lock2')
    
    lock1.acquire()
    print('Task 2 acquired Lock2')
    
    print('Task 2 started')
    time.sleep(3)
    print('Task 2 completed')
    
    lock1.release()
    lock2.release()
    
    
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

#Avoiding Deadlocks
#1.consisti order
#2.limit threads
#3.timeouts
#4.semaphones
#5.ModalTransientResponse
#6.message pasing
#7.deadlock detections



#Communication between threads

#thread communication
import threading

#condition variable
condition = threading.Condition()

def my_thread():
    with condition:
        print('Thread waiting for signal')
        condition.wait()
        print('Thread received signal')
        
t=threading.Thread(target=my_thread)
t.start()


t.join()

with condition:
    print('sending signal')
    condition.notify()

t.join()







