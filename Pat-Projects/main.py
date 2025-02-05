try:
    user_input = int(input('Enter: '))
except ValueError:
    print('Enter only integer value')
except TypeError:
    print('There is an type error')
else:
    print(user_input)