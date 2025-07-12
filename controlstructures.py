#if statement 
#program that checks a positive and negative number

num = int(input('Enter  a num: ')) #type casting...

# print(type(num))

# if num > 0:
#     print(f'{num} is a positive number...')
# elif num  < 0:
#     print('Ne Num')
# else:
#     print('the default')
    

# print('i am outside of if statement')



#python nested if/else statements

if num >= 0:
    if num == 0:
        print('Num is Zero.....')
    if num == 11:
        print(f'{num} you selected a lucky number!!')
    else:
        print(f'{num} is a positive number...')
else:
    print('Num is neg') # default - 
    
    