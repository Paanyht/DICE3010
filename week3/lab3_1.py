def sums():
   
  # Initialize a variable called first_sum and store the sum of 
  # 2 and 2
  first_sum = 2 + 2
  # Store to first_sum the value of first_sum times 10
  first_sum = first_sum * 10
  #Initialize a variable called secret and assign it the value 
  # of first_sum plus 2
  secret = first_sum + 2
  return secret

def string_manip(first_name):

   # : Initialize a variable called name and assign it the 
   # parameter.
    name = first_name
   # : Use builtin string functions and slices to replace None with 
   # the appropriate manipulation of your name. I've done the first one.
   all_caps = name.upper()
   all_lowercase = name.lower()
   first_five_letters = name[:5]
   last_two_letters = name[-2:]

   return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   #  Use the input() function to prompt the user for their name.
   # Then assign the value to a variable called name and print a greeting.
   # I have started it for you, but you need to modify the input and 
   # print functions.
   # Hint: to get the test to pass, the greeting should be "Hello, input name"
   fname = input('what\'s your name?')
   print('Hello, ' + fname+"!")

def temp_calculator():

   #  Write code that prompts the user for a temperature in degrees
   # celsius and prints the equivalent temperature in degrees fahrenheit.
   # The formula is C = (F - 32) * (5/9). 
   c = float(input('what is the temperature?'))
   print(c*(9/5)+32)
   

def equitable_bill_splitter():
   
   # Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   
   # propmts the user how many people are paying?and saves the result in the people variable
   people = int(input("How many people are paying? "))
   #initilazies the variable the salaries to an empty array
   salaries = []
   # sets the variable total to zero
   total = 0
   
   # loop through the number of people
   for i in range(people):
      #prompts the user for salary of person i and saves the result in variable sal
      sal = int(input("What is the salary of person {}?".format(i+1)))
      #add salary to total variable
      total += sal
      #add the new salary to salaries array
      salaries.append(sal)
   
   #prompt the user how much is the bill?and saves the result in variable total
   total_bill = int(input("How much is the bill? "))
   
   #loop thorugh the salaries
   for j in range(len(salaries)):
      #prints how much of the bill person j needs to pay (rounded to two decimal places) based on their salary
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))
