#Amos Colocho
#CSC2053-002 HW Assignment 1

#This first function takes a list of numbers and returns the sum of all numbers in the list
def sum_list(numbers):
    """return the sum of all integers in the given list."""
    return sum(numbers)

#this function takes a persons name and favoorite food and returns a message containing both valyes
def greet_user(name, fav_food):
    """return a friendly message using the user's name and thier favorite food."""
    return f"Hello {name}! Your favorite food is {fav_food} how delicious!"

#Test the first function 3 times with different lists.
print(sum_list([1, 2, 3, 4]))
print(sum_list([10, 20, 30]))
print(sum_list([-1, -3, -2, 7]))

#Test the second function 3 times with different data.
print(greet_user("Amos", "Pizza"))
print(greet_user("Kathleen", "Hamburger"))
print(greet_user("Joe", "Sushi"))