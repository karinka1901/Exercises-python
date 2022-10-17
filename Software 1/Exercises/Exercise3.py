#ex1
answer = float(input('Enter the length in cm: '))
size_limit = 42
result = 42 - answer
if answer < size_limit:
    print('The fish is ' + str(result) + ' cm below the size limit ')
    print('Release the fish back!')
if answer >= size_limit:
    print('Good job!')

#ex2
cabin_class = input('Enter the cabin class (A, B or LUX): ')
lux = 'LUX'
a = 'A'
b = 'B'
c = 'C'
if cabin_class == lux:
    print('upper-deck cabin with a balcony.')
elif cabin_class == a:
    print('above the car deck, equipped with a window.')
elif cabin_class == b:
    print('windowless cabin above the car deck.')
elif cabin_class == c:
    print('windowless cabin below the car deck.')
else:
   print('Invalid cabin class')


#ex3
b_gender = input('What is your biological gender(F/M)? ')
h_value = int(input('Enter your hemoglobin value: '))

#female: 117-155
#male: 134 - 167

if b_gender == 'F':
    if h_value >= 117 and h_value <= 155:
        print('Your hemoglobin level is normal')
    if h_value < 117:
        print('Your hemoglobin level is low')
    if h_value > 155:
        print('Your hemoglobin level is high')
if b_gender == 'M':
    if h_value >= 134 and h_value <= 167:
        print('Your hemoglobin level is normal')
    elif h_value < 134:
        print('Your hemoglobin level is low')
    elif h_value > 167:
        print('Your hemoglobin level is high')

#ex 4:
year = int(input('Enter the year: '))
if year % 4 == 0:
    print('The ' + str(year) + ' is a leap year')
elif year % 100 == 0 and year % 400 == 0:
    print('The ' + str(year) + ' is a leap year')
else:
    print('The ' + str(year) + ' is not a leap year')

