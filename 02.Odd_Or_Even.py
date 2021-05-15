number = int(input('Please type a number. ANY will do!:\n'))
module = float(number % 2)

if module > 0:
    print(f'The number ({number}) you typed is an odd number!')
elif module == 0:
    print(f'The number ({number}) you typed is an even number!')
else:
    print('Incorrect, please try again.')