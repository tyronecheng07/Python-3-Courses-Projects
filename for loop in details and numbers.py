#for loop in details
for i in range(5):
    print("Hello")

#it means do something 5 times
#we can call anything in i
#range of 5 is a list from 0-4
#it has to use: print(list(range5))

#high recommended
for number in range(5):
    print(number)
#better name the i with a good name for better readability

range(20, 41)
#a list of 20 to 40

#sum up the list 1
#we have to define a initial condition in for loop
count = 0

for number in range(1, 4):
    #new count = old count + number
    count = count + number

print(count)

#it will print out the final number


#sum up the list 2
for number in range(1, 4):
    #new count = old count + number
    count = count + number
    print(count)

#it will print out the sum for every loop, like this:
#1
#3
#6


#write a (function) that sums all elements of a list and returns them
def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number

    return count


#function => def a name(a variable):
#end with return

#assert (function) is for us to test a thing that whether will give us an error or not
#example: assert sum_list[1, 2, 3] == 6
#if the code is correct then the outcome shows true

#number
#number ** number => number to the power of number

#even number
# using % as number % 2 => giving us the outcome of 0 remainder



#exercise
# Make sure to un-comment the function line below when you are done.
# Remember to name your function is_even
# WRITE YOUR CODE HERE...
def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

def is_even(number):
  return number % 2 == 0

#this is a condition statement, with == 0, check if equals to 0
#will produces true or false

# DO NOT remove lines below here,
# this is designed to test your code.

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(8) == True
  assert is_even(100) == True
  assert is_even(101) == False
  print("YOUR CODE IS CORRECT!")
  
# test your code by un-commenting the line(s) below
test_is_even()

def string_length(string):
    count = 0
    for letter in string:
        count += 1

    return count

print(string_length(string))

#or

def string_length(string):
    return len(string)



#compare a bigger number
def bigger_guy(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2


def biggest_guy(num1, num2, num3):
  # find bigger guy between num1 and num2
  # find biggest guy between bigger guy and num3
  return bigger_guy(bigger_guy(num1, num2), num3)

#using dictionary in function
def choice_to_number(choice):
  return {'Usain': 1, 'Me': 2, 'Qazi': 3}[choice]
  
def number_to_choice(number):
  return {1: 'Usain', 2: 'Me', 3: 'Qazi'}[number]

#or

def choice_to_number(choice):
	opponent = {'Usain': 1, 'Me': 2, 'Qazi': 3}
	return opponent[choice]

def number_to_choice(number):
    contestant = {1: 'Usain', 2: 'Me', 3: 'Qazi'}
    return contestant[number]

def test_all():
    choice_to_number(choice)
    number_to_choice(number)
return
