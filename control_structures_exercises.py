week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print('What day of the week is it?')
is_monday = input()
if is_monday == 'monday':
    print('Correct it is monday')
else:
    print('Incorrect it is actually monday')


print('-------------------------------------------------------------------')

print("What day of the week is it now?")
what_day = input()
if what_day == ('saturday' or 'sunday'):
    print('That means it is the weekend')
else:
    print('It is almost the weekend')

print('-------------------------------------------------------------------')
print('How many hours did you work this week?')
hours_worked = int(input())
print('What is your hourly pay rate?')
pay_rate = int(input())
paycheck_weekly = hours_worked * pay_rate
if hours_worked > 40:
    print('Nice your paycheck this week is')
    print((40 * pay_rate) + ((hours_worked - 40) * (pay_rate * 1.5)))
else:
    print('Nice your paycheck this week is')
    print(paycheck_weekly)

print('-------------------------------------------------------------------')

i = 5
while i <= 15:
    print(i)
    i += 1
print('-------------------------------------------------------------------')
i = 0 
while i <= 100:
    print(i)
    i += 2

print('-------------------------------------------------------------------')

i = 100
while i >= -10:
    print(i)
    i -=5

print('-------------------------------------------------------------------')

i = 2 
while i <1000000:
    print(i)
    i **= 2

print('-------------------------------------------------------------------')

i = 100
while i >= 5:
    print(i)
    i -=5

print('-------------------------------------------------------------------')

print("Please input a number from 1-10")
number = int(input())
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(f'{number} x {i} = {number * i}')

print('-------------------------------------------------------------------')

for i in range(1,10):
   
    for x in range(i):
        print(i, end = '')
    print() 

print('-------------------------------------------------------------------')
print('Please enter an odd number between 1 and 50')
skip = int(input())
print()
print(f'Number to skip is: {skip}')
for n in range(50):
    if n == skip:
        print(f'Yikes! Skipping number: {n}')
    
    elif n % 2 == 0:
        continue
    print(f'here is an odd number: {n}')

print('-------------------------------------------------------------------')

print("Please enter a positive integer")
num = int(input())
print()
counter = num + 1
for i in range(counter):
    print(i)

print('-------------------------------------------------------------------')

print('Please enter a positive integer')
i = int(input())
print()
while i >= 1:
    print(i)
    i -= 1 

print('-------------------------------------------------------------------')

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue 
    elif i % 3 == 0:
        print('fizz')
        continue
    elif i % 5 == 0:
        print('buzz')
        continue
    print(i)

print('-------------------------------------------------------------------')

num = int(input('What number would you like to go up to: '))
counter = num +1
print()
for i in range(1, counter):
    print(i, i ** 2, i ** 3)
cont = input('Would you like to continue (y/n): ')
while cont == 'y':
    num += 1
    print(num, num ** 2, num ** 3)
    cont = input('Would you like to continue (y/n): ')

print('-------------------------------------------------------------------')

grade = int(input('Please enter a numerical whole number grade: '))
if 100 >= grade >= 88:
    print(f'Your grade of {grade} is an A')
elif 87 >= grade >= 80:
     print(f'Your grade of {grade} is a B')
elif 79 >= grade >= 67:
     print(f'Your grade of {grade} is a C')
elif 66 >= grade >= 60:
     print(f'Your grade of {grade} is a D')
elif 59 >= grade >= 0:
     print(f'Your grade of {grade} is an F')

print('-------------------------------------------------------------------')

books_read = [
    
{'Title': 'Harry Potter and The Goblet of Fire', 
 'Author': "J.K. Rowling", 
 "Genre": ["Fantasy", "Suspense", "Mystery"]
},
{'Title': 'Charlie and The Chocolate Factory',
 'Author': 'Roald Dahl',
 'Genre': ['Fantasy', 'Science Fiction', 'Classic']
},
{'Title': 'Alex Rider: Ark Angel',
 'Author': 'Anthony Horowitz',
 'Genre': ['Fiction', 'Suspense-Thriller', 'Mystery']
}
]


for book in books_read:
    [print(key, ': ', book[key]) for key in book]
    print('-------------------------------------------------------')

genres = input('Please select a genre to find similiar titles: ')
matches = []
for book in books_read:
    if book['Genre'].lower() == genres.lower():
        matches.append(book['Title'])
if matches == []:
    print('I couldn\'t find any books in that genre')
else:
    print(f'The {genres} genre you selected includes the following titles:')
    [print(match) for match in matches]




    



