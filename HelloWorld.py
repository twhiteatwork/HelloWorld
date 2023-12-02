def main():
    #Output Hello World
    #print('Hello World!')
    #secondary_function()
    #logical_operators()
    #greet_someone()
    #call_math_function()
    #variables()
    #data_types()
    #logical_operators()
    #if_statements()
    #for_loops()
    while_loops()

def square(num):
    #Squares a number
    numSquared = num * num
    return numSquared

def data_types():
    temperature = int(101.2)
    print(type(temperature))

    temperature = float(101.2)
    print(type(temperature))

    temperature = bool(101.2)
    print(type(temperature))

    temperature = str(101.2)
    print(type(temperature))

def call_math_function():
    print(square(4))

def logical_operators():
    #Logical operators
    print('Logical operators')
    x = 5
    y = 2
 
    print('arithmetic operator (x + y): ', x + y)
    print('comparison operator (x >= y): ', x >= y)
    print('logical operator (x == y and x > y): ', x == y and x > y)

def secondary_function():
    #Function useful for demonstrating function call
    print('2nd function')

def greet_someone():
   #Input and output
   name = input('What is your name?')
   hometown = input('And where are you from?')
   print('Very nice to meet you {}'.format(name), f'from {hometown}!')

def variables():
    #Set and output variables
    int_value = 4
    print(int_value)
    print(type(int_value))

    print()

    float_value = float(int_value)
    print(float_value)
    print(type(float_value))

def logical_operators():
    #Show how some logical operators work
    x = 5
    y = 3

    print(f'where x={x} and y={y}')
    print('arithmetic operator (x + y): ', x + y)
    print('comparison operator (x >= y): ', x >= y)
    print('logical operator (x == y and x > y): ', x == y and x > y)

def if_statements():
    #Evaluate a variable against options
    score = 10
 
    if score >= 92:
        print('Your final grade is an A')
    elif score >= 85:
        print('Your final grade is a B')
    elif score >= 70:
        print('Your final grade is a C')
    else:
        print('Talk with your instructor about your grade!')

def for_loops():
    #Loop through collection of collection
    teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
    for team in teams:
        for name in team:
            print(name)

def while_loops():
    #Loop through number range
    i = 3
    while i < 258:
        if i == 9:
            #continue #Move onto next iteration, causes infinite loop
            #pass #Do nothing
            break #Stop iterating, exit loop
        else:
            print(i)
        i = i ** 2

if __name__ == '__main__':
    main()