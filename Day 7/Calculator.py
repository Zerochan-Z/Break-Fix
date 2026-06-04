import sys

if len(sys.argv) != 4:
    print('Error input. Please enter <num1> <operator> <num2> ')
    print('Operators: add, sub, mul, div')
    sys.exit(1)

else: 
    print('Printing results....')
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

if op == 'add':
    result = num1 + num2
    symbol = '+'
elif op == 'sub':
    result = num1 - num2
    symbol = '-'
elif op == 'mul':
    result = num1 * num2
    symbol = '*'
elif op == 'div':
    if num2 == 0:
        print('Unavaiable to divide by zero')
        sys.exit(1)
    else:
        result = num1 / num2
        symbol = '/'
        
else:
    print(f'Sorry {op} is not in our operation list.')
    print('Error input. Please enter <num1> <operator> <num2> ')
    print('Operators: add, sub, mul, div')
    sys.exit(1)

print(f'{num1} {symbol} {num2} = {result}')
        