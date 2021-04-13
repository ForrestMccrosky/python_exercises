import function_exercises as fe

print('')
print('BEGGINING OF IMPORT EXERCISES')
print('with imported functions exercise above for function recalls')
print('Exercise 1(a)')

# ^ importing our function exercises and aliasing it as fe for easier referencing 

print(fe.is_vowel('u'))
print(fe.is_vowel('x'))

print('----------------------------------------')

print('Exercise 1(b)')

# using from to import calculate tip from my function exercises
from function_exercises import calculate_tip as ct
# calling the function with it aliased name from above with the correct parameters
print(ct(.20, 120))

print('----------------------------------------')

print('Exercise 1(c)')

# using from to import and aliasing function name as GG
from function_exercises import get_letter_grade as gg
# calling the function with the correct parameters and alias
print(gg(74))

print('----------------------------------------')
print('Exercise 2(a)')
import itertools as it

new_list = (list(it.product('abc', '123')))
print(len(new_list))

print('Exercise 2(b)')

print(len(list(it.combinations('abcd',2))))

print('Exercise 2(c)')

print(len(list(it.permutations('abcd', 2))))

print('----------------------------------------')
print('Exercise 3')
# importing json module and using the load function to open the profiles file
import json
my_dict = json.load(open('profiles.json'))

# Using list comprehension to count the number of users in the list of dictionairies')

print('Total number of users:')
x = 0
for i in my_dict:
    x += 1
print(x)
print('')

# Counting the number of actice users by using the same list comprehension above and delcaring and if statement for the isActive key equaling true

print('Number of active users:')
x = 0 
for i in my_dict:
    if i['isActive'] == True:
        x += 1
print(x)
print('')

# same thing above just set the boolean value == False to return the inactive users
print("Number of inactive users:")
x = 0
for i in my_dict:
    if i['isActive'] == False:
        x += 1 
print(x)
print('')

import function_exercises as fe

total_balance = 0
new_balance = []
for i in my_dict:
    new_balance = fe.handle_commas(i['balance'])
    new_balance = fe.remove_special(i['balance'])
    total_balance += float(new_balance) 
print(f'The total balance of all users is: {total_balance}')

print('')

# By using the list comprehension we performed above to gather the total amount of users. We
# can simply copy the for loop and divide x by the total balance we retrieved from the last block of code using the same variable
balance_average = 0
x = 0
for i in my_dict:
    x += 1
balance_average = total_balance / x
print(f'The average of all the balances is: {balance_average}')

print('')

def string_money_float(string):
    """
    this function takes in a string with a dollar sign and commas and returns a float ready for math
    
    """
    char_to_replace = {'$': '',
                    ',': ''}
    # Iterate over all key-value pairs in dictionary
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        string = string.replace(key, value)
    return float(string)
print('Here is a list of all the balances for easier computing')
all_balance = []
for x in my_dict:
    all_balance.append(string_money_float(x['balance']))
print(all_balance)

lowest_balance = min(all_balance)

from pprint import pprint

low_user = []
for user in my_dict:

    temp_balance = string_money_float(user['balance'])
    if temp_balance == lowest_balance:
        low_user.append(user)
print('Here is the dictionary belonging to the user with the lowest balance')
pprint(low_user)
print('This is their name: ')
pprint(low_user[0]['name'])

print('')

highest_balance = max(all_balance)

from pprint import pprint

high_user = []
for user in my_dict:

    temp_balance = string_money_float(user['balance'])
    if temp_balance == highest_balance:
        high_user.append(user)
print('Here is the dictionary belonging to the user with the highest balance')
pprint(high_user)
print('This is their name:')
pprint(high_user[0]['name'])

print('')

user_fruits = []
for user in my_dict:
    user_fruits.append(user['favoriteFruit'])

print('Here is a list of all the fruit choices from all 19 users')
print(user_fruits)

print('')

from collections import Counter

fruits = Counter(user_fruits)

print('Here is a tuple returned with the counter function from the collections module') 
print('to display the fruit choices and their counts')
print(fruits)

print('')
print('Here is the unpacked fruit containing the most choices at 9')
print(fruits.most_common(1))

print('Since we have a simple list with only three values we can') 
print('also see that the least common fruit is Apples at 4')
        
        





