numbers = []
number = input("Please enter a positive number: ")
if number == -1:
    print '\n.Oops, you entered -1\n'
    
elif number <-1:
    print '\n.You just entered a negative number\n'
else:
    larger = number
    smaller = number
    count = 1
    
    while (number > 0):
        number = input('\n.Please enter another positive number: ')
        
        if number == -1: 
            print "\n.-1 is not acceptable, ceasing the number entering process...\n"
            howMany = count
            if count == 1:
                print '\n.You havent entered enough numbers to be compared.\n' 
                print '\n.Please enter at least two numbers to get the largest and smallest.\n'
            else:    
                smallest = smaller
                largest = larger
            print '\n.The total of ', howMany, 'numbers entered.\n', '\n.Largest number entered is: ', largest, "\n", '\n.Smallest number entered is: ', smallest, "\n"
            break
        else:
            if larger < number:
               larger = number
               count += 1
            elif smaller > number:
                smaller = number
                count += 1
            else:
                count += 1
                print number, smaller, larger
