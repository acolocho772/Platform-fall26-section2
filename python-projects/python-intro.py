print("Hello World!")

# this is a comment

'''
this is for a lot of comments
used often to describe function
'''

# this is a comment
# describing a function
# here is the input

x = 100
print(x)
x=5.5
print(x)
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
z=x/y
print(z)
#casting integer
z=int(z)
print(z)

result=x//y #this is floor division (chopps off any decimal points)
print(result)

min_val=min(10,2)
print(min_val)

#raising number to a power (both lines are the same thing)
raised=pow(2,4)
print(raised)
raised=2**4

#simple if statement
if x<0:
    print("x is less than 0")
    print("another line of code")

if (x<0) or y<0:
    print("at least one less than 0")


if x<0:
    print("less than 0")
elif x>0:
    print("greater than 0")
else:
    print(0)


#class 8_27_26

lst=[1,2,3,4,5]
for i, val in enumerate(lst):
    print(i, val)

for val in lst:
    print(val)


#python loop exercises for class
#Write a for loop to print all numbers from 1 to 20 that are divisible by 3.
for number in range(1, 21):
    if number % 3 == 0:
        print(number)


#while loop that calculates the sum of all even numbers between 1 and 50
count = 2
even_sum = 0
while count <= 50:
    if count % 2 == 0:
        even_sum += count
    count += 1
print(even_sum)

#You are given a list of numbers: 
# print numbers greater than 5
numbers = [5, 8, 2, 15, 10, 3, 7]
for number in numbers:
    if number > 5:
        print(number)

def hello(name="Bob"):
    print("hello",name)
hello("Bob")


#function swap example
def swap(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
lst=[0,3,8,4,5] 
swap(lst) 
print(lst) 


full_name="Amos Colocho"
first_name=full_name.split()[0]
last_name=full_name.split()[1]
print(first_name, last_name)

#class 9_1_26
values = [34,27,95,18,36,21,64,50,77]
even_values=[x for x in values if x % 2 == 0]
print(even_values)

aset=set()
#difference between a set and a list is that a set does not allow duplicates
aset={1,2,3,4,5}
print(aset)
aset.add(40)
print(aset)
# print(aset[0])  # This will raise a TypeError because sets are unordered and don't support indexing

fav_foods={"kathleen": 'pizza', 
           "amos": 'tacos', 
           "james": 'burgers'}
food=fav_foods['amos']
print(food)

if 'bob' in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob']='ice cream'
print(fav_foods)

for name, fav_food in fav_foods.items():
    print(name, fav_food)
