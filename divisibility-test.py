for num in range(0, 101):
    print('Number is: ' + str(num) + '\n')
    if num%2 == 0 and num%5 == 0:
        print('2 or 5\n\n')
    elif num%2 == 0:
        print('2 only\n\n')
    elif num%5 == 0:
        print('5 only\n\n')
    else:
        print('Not divisible by 2 or 5\n\n')