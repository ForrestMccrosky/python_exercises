# PLEASE NOTICE ALL FUNCTION HAVE APPROPRIATE DOCSTRINGS EXPLAINING THERE PURPOSE AS WELL AS NECCESSARY INPUT 
print('Exercise 1')
# defining the function is_two with the input stringnum
def is_two(stringnum):
    """
    This function will take and input and return true if the input matches the number
    or string "2"
    """
    # checking to see if stringnum is equal to the string or integer 2
    if stringnum == "2" or stringnum == 2:
        # returning true if true 
        return True
    else:
        # otherwise returning false
        return False
# calling function with inputs in a print statement so it will have output in the terminal
print(is_two(2))
print(is_two(3))


print('---------------------------------------------------------------')

print('Exercise 2')
# defining the function is_vowel with a string for input
def is_vowel(string):
    """
    This function returns whether the passed string into the function is a vowel or not
    with the boolean value true or false
    """
    # checking to see if any characters are vowels and because i don't also want to type the capitalized 
    # version I am using .lower()
    if string.lower() in ('a','e','i','o','u'):
        return True
    else:
        return False
print(is_vowel('u'))
print(is_vowel('x'))

print('---------------------------------------------------------------')

print('Exercise 3')
# defininf function is_consonant with a string for input
def is_consonant(string):
    """
        This function returns whether the passed string into the function is a consonant or not
    with the boolean value true or false
    """
    # calling the is_vowel function from above to determine if the single character inputted is a vowel 
    # assigning it equal to a boolean value
    if is_vowel(string) == True:
        # returning false because the question wants the output to be false if the string is a consonant
        return False
    else:
        # otherwise return true because the only other outcome is a vowel
        return True
print(is_consonant('x'))
print(is_consonant('u'))


print('---------------------------------------------------------------')

print('Exercise 4')

def kappa(string):
    """
    This function takes a string and returns it with a capitalized first letter if the string's first letter
    is a consonant 
    """
    # checking to see if the first letter in the string is a consonant by using range 0 and calling the is_consonant function
    if is_consonant(string[0]) == True:
        # capitalizing the first letter of the string if it is a consonant 
        return string.capitalize()
    else:
        # otherwise not capitalizing the first letter if it is a vowel
        return string
print(kappa('something'))
print(kappa('uppercut'))

print('---------------------------------------------------------------')

print('Exercise 5')

def calculate_tip(percent, bill):
    """
    This function takes a percentage as a decimal and multiplies it by a bill total to calculate the amount to tip
    """
    # checking function parameter input to make sure it is a decimal to match the correct percentage format for multiplication
    if percent < 1 and percent > 0:
        # by multiplying the total bill (bill) by percent (tip percentage) this gets the amount that should be tipped.
        return bill * percent

print(calculate_tip(.20, 120))

print('---------------------------------------------------------------')

print('Exercise 6')
# assigning an empty variable that will be able to be edited withing the function
nprice = 0
def apply_discount(oprice, discount):
    """
    This function takes in an original price of an item and the discount for the item and then returns the new price 
    for the item based on the discount
    """
    # checking to make sure the discount is in the correct decimal format for multiplication
    if discount < 1 and discount > 0:
        # by setting nprice equal to the eqaution below we can return the new price within the function
        nprice = oprice - (oprice * discount)
        return nprice

print(apply_discount(120, .20))
    

print('---------------------------------------------------------------')


print('Exercise 7')


def handle_commas(string):
    """
    This function takes an output representing a number with commas and removes the commas.
    """
    # using string = string replace we can replace commas with '' which is an empty slot removing the commas
    string = string.replace(",", "")
    return string

print(handle_commas('2,345,345'))


print('---------------------------------------------------------------')

print('Exercise 8')

def get_letter_grade(grade):
    """
    This function takes in a numerical grade and converts it to the appropriate letter grade.
    """
    # Using a bunch of greater than and less than or equal too operands we can use if and elif statements
    # to determine the correct letter grade associated with the numerical grade
    if 100 >= grade >= 88:
            return 'A'
    elif 87 >= grade >= 80:
            return 'B'
    elif 79 >= grade >= 67:
            return 'C'
    elif 66 >= grade >= 60:
            return 'D'
    elif 59 >= grade >= 0:
            return 'F'
# uses a format string to create nice output with the letter grade 
print(f'Your grade is a(n) {get_letter_grade(78)}')

print('---------------------------------------------------------------')
print('Exercise 9')
# creating a list of lowercase vowels to be called later in a function
vowels = ['a','e','i','o','u']
def remove_vowels(string):
    """
    This function takes in a string as input and removes all of it's vowels
    """
    # using list comprehension to loop through a lowercase string using x (since we only have lowercase vowels in vowels)
    for x in string.lower():
        # if the character at x is a vowel since it is in vowels
        if x in vowels:
            # we replace the vowels with '' (empty space) removing the vowels
            string = string.replace(x,'')
    return string

print(remove_vowels('Hello World Get Rid of my vowels'))

print('---------------------------------------------------------------')

print('Exercise 11')


def cumulative_list(nlist):
    """
    This function takes a list of numbers and returns a new list of their cummulative sums starting with the first number and
    adding each successive number
    """
    # assinging a new empty list to be used to create the new cumulative list to be returned at the end of the function
    new_list = []
    # assinging a length variable that will used to reference indexes
    length = len(nlist)
    # creating a new list using the sum function 
    # also uses slicing to acces the elements from the start to the index + 1 element
    # and list comprehension is used to loop through the inputed string using x
    new_list = [sum(nlist[0:x:1]) for x in range(0, length +1)]
    # returning the new list at index of 1 and so on because the new list is the correctly summed/cumulative list
    return new_list[1:]
numbers = [1,1,1]
print(cumulative_list(numbers))

numbers2 = [1,2,3,4]
print(cumulative_list(numbers2))

print('---------------------------------------------------------------')

print('Exercise 10')
# Creating a function that removes all alphanumeric characters except spaces
def remove_special(string):
    """
    This function removes all special characters from a string except for spaces
    """
    new_string = ''
    for x in string:
        # Checking to see if the character at x is alphanumeric or a space
        if x.isalnum() or x == ' ' or x == '.':
            #forming a new string with each x (character) that is not an alphanumeric character but retaining all spaces
            new_string += x
            # returning the newly edited string
    return new_string

print(remove_special(' HEllo #WORLD this is now a file name'))


def normalize_name(string):
    """
    This function removes all special characters using the remove_special function and normalizes strings into 
    a viable python name. By deleting leading spaces and replacing non leading spaces with '_''s
    """
    # Making sure all enter inputed is converted to lower case
    for x in string.lower():
        # Calling the above function to remove special characters but not spaces
        string = remove_special(string)
        # making sure alll characters are lowercased
        string = string.lower()
        # strip deletes leading and exiting white spaces
        string = string.strip()
        # Replaces internal spaces with _'s
        string = string.replace(' ', '_')
        # returning the new python normalized string
        return string

print(normalize_name(' HEllo #WORLD this is now a file name'))