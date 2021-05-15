number = int(input('Please type a number. ANY will do!: '))
check = int(input('Now, type a number to divide by: '))

print('') # This line is just to divide the blocks of code

module = float(number % 2)
module_4 = float(number % 4)
module_check = float(number % check)


if module > 0:
    print(f'The number ({number}) you typed is an odd number!')
elif module == 0:
    print(f'The number ({number}) you typed is an even number!')
    if module_4 == 0:
        print(f'Also, the number ({number}) is multiple of 4!')
    else:
        print('')
else:
    print('Incorrect, please try again.')

print('') # This line, too, is just to divide the blocks of code

if module_check == 0:
    print(f'Note: {number} divides evenly by {check}!')
else:
    print(f'Note: {number} does NOT divide evenly by {check}')