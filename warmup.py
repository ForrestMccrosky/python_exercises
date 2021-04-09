print('Exercise 1')

truck = 'toyota tacoma'

split_truck = truck.split()
truck = {
'make': split_truck[0], 
'model': split_truck[1]
}
print(truck)
print('---------------------------------------')

print('Exercise 2')

truck = 'toyota tacoma'

split_truck = truck.split()
make1 = split_truck[0].capitalize()
model2 = split_truck[1].capitalize()
truck = {
'make': make1, 
'model': model2
}

print(truck)

print('---------------------------------------')

print('Exercise 3')

cars = [
{
'make': 'toyota',
'model': 'tacoma'
},

{
'make': 'hyundai',
'model': 'genesis'
},

{
'make': 'toyota',
'model': 'forerunner'
}
]



for car in cars:
    car['model'] = car['model'].upper()
    
print(cars)
