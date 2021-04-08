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
