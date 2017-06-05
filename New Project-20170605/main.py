numbers = []
number = input("Please enter a positive number: ")
if number == -1:
    print '\n.....Oops, you entered -1, ceasing the number entering process...\n'
    
elif number <-1:
    print '\n.....You just entered a negative number, please try again...\n'
    
else:
    numbers.append(number)
    while (number > 0):
        number = input('\n.Please enter another positive number: ')
        
        if number == -1: 
            print "\n.....-1 is not acceptable, ceasing the number entering process...\n"
            howMany = len(numbers)
            largest = sorted(numbers, reverse=True)[0]
            smallest = sorted(numbers, reverse=True)[howMany-1]
            print '\n->The total of ', howMany, 'numbers entered.\n', '\n->Largest number entered is: ', largest, "\n", '\n->Smallest number entered is: ', smallest, "\n"
            break
        elif number <-1:
            print '\n.....You just entered a negative number\n'
            number = input("Please enter a positive number: ")
        else:
            numbers.append(number)
            print numbers
