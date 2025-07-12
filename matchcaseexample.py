#match case..... switch case 
#welcome message
print('Welcome...... to our GAME!!')
print('Choose from our list - type the exact keywords...')
print('apple, orange')

#Taking user input
fruit = input('Enter a fruit name: ')


#match case to check the fruit and compare the value of 'fruit'
#case are case-sentive
match fruit: 
    case "apple": #1st case
        print('Keeps the doc away!')
    case "Apple": #2nt case
        print('Keeps the doc away!')
    case "orange": #3rd case
        print('Oranges are oranges!!')
    case _: #default case if thers a no match!!!
        print('Not in the list! - Thankyou for playing!!')
        
        


    
    