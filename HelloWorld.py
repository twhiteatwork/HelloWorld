import datetime

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
    #while_loops()
    #try_and_except()
    #greetings('Japanese')
    #print(square(2))
    #print(add_three(1,2,3))
    #print(factorial(5))
    #print(add_two(3))
    #uplift_grades()
    #create_dog()
    #use_student_class()
    #use_banking_classes()
    #string_manipulation()
    #list_manipulation()
    #tuple_manipulation()
    #dictionary_manipulation()
    #set_manipulation()
    #queue_manipulation()
    stack_manipulation()


def square(num):
    #Squares a number
    numSquared = num * num
    return numSquared

def add_three(num1, num2, num3):
   sum_three = num1 + num2 + num3
   return sum_three

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

def try_and_except():
    #Try with success
    items = [1, 2, 2, 1]
 
    try:
        print(sum(items))
 
    except:
        print('Cannot print the sum! Your variables are not numbers.')

    finally:
        print('Succeeded')

    #Try with fail
    items = ['a', 'b', 'c', 'd']
 
    try:
        print(sum(items))
 
    except:
        print('Cannot print the sum! Your variables are not numbers.')

    finally:
        print('Failed')

def greetings(language):
    if language == 'Spanish':
        greeting = 'Hola'
 
    elif language == 'English':
        greeting = 'Hello'
 
    elif language == 'French':
        greeting = 'Bonjour'
    
    else:
        greeting = 'Language not found'

    print(greeting)

def factorial(num):
   #recursive fatorial function
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)

add_two = lambda x: x + 2

def uplift_grades():
    import pandas as pd
 
    df = pd.DataFrame({
        'name': ['Amy', 'Jackie', 'Sue'],
        'grades': [90, 84, 76]
    })
 
    # use the lambda function to multiply bump up the values in the grades column by 1.2!
    df['grades'] = df['grades'].apply(lambda x: x * 1.2)

    print(df)

class Dog:
   # this is a blank class
   pass

def create_dog():
    pepper = Dog()
    print(pepper)

class Student:
    def __init__(self, name, age, haircolor):
        self.__name = name #Private class attribute
        self._age = age #Protected class attribute
        self.haircolor = haircolor #Public class attribute

    @classmethod
    def calculate_age(cls, name, birth_year, haircolor):
        # calculate age an set it as a age
        # return new object
        return cls(name, datetime.date.today().year - birth_year, haircolor)

    def show(self):
        print(self.__name + "'s age is: " + str(self._age) + ' and hair color is ' + str(self.haircolor))

def use_student_class():
    # create a ClassSchedule object
    Jessa = Student('Jessa', 20, 'blond')
    Jessa.show()

    Joy = Student.calculate_age('Joy', 2000, 'brown')
    Joy.show()

class Checking():
    #Basic banking class - checking
    def type(self):
        print('You have a checking account at the Codecademy Bank.')
 
    def balance(self):
        print('$20 left in your checking.')
 
class Savings():
    #Basic banking class - savings
    def type(self):
        print('You have a savings account at the Codecademy Bank.')
  
    def balance(self):
        print('$1000 left in your savings.')

def use_banking_classes():
    #Example of polymorphism
    account_a = Savings()
    account_b = Checking()

    for account in (account_a, account_b):
        account.type()
        account.balance()

def string_manipulation():
    intro = "My name is Jeff!"
    print(intro[0]) #Output first character of string
    print(intro[0:2]) #Output first two characters of string
    print(intro[-5:-1]) #Output from end of string
    print(len(intro)) #Output length of string
    print(intro.upper()) #Output string in uppercase, lower() for lowercase
    print(intro.split(' ')[2]) #Split string on delimiter into array of strings and output particular one

def list_manipulation():
    #zero-based indexing of lists
    lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
    print(lst[3]) #Output third item from list
    print(len(lst)) #Output count of items in list
    lst.append('test') #Add item to end of list
    print(len(lst)) #Show that append increased count
    lst.remove('def') #Removes item as requested if found
    print(lst)
    lst.pop() #Removes last item in list and returns it
    lst.pop(0) #Removes first item in list and returns it

def tuple_manipulation():
    #zero-based indexing of tuples
    my_tuple = ('abc', 123, 'abc', 'def', 456)
    #my_tuple = ('abc',) #Single item tuple allowed so long as comma ends it
    print(len(my_tuple))
    print(my_tuple.index(123))
    print(my_tuple.count('abc'))

def dictionary_manipulation():
    groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
            'protein': ['beef', 'pork', 'salmon'],
            'carbs': ['rice', 'pasta', 'bread'],
            'veggies': ['lettuce', 'cabbage', 'onions']}
    
    print(groceries['carbs'])
    print(groceries.keys())

def set_manipulation():
    students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
    students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
    students3 = students1.union(students2) #Duplicates removed by union
    students3.remove('Jane')

    print(students3)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    #Resource: https://medium.com/@Emmanuel.A/data-structure-queue-python-9e5439d2ceea
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def peek(self):
        return self.head.data
    def enqueue(self, data):
        new_data = Node(data)
        if self.head is None:
           self.head = new_data
           self.tail = self.head
        else:
           self.tail.next = new_data
           self.tail = new_data
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
           self.tail is None
        return data

def queue_manipulation():
    #Queue is first in first out
    my_queue = Queue()
    print(my_queue.isEmpty())
    my_queue.enqueue('Ted')
    my_queue.enqueue('Katie')
    print(my_queue.isEmpty())
    print(my_queue.peek())
    next_name = my_queue.dequeue()
    print(next_name)
    next_name = my_queue.dequeue()
    print(next_name)

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def stack_manipulation():
    #Stack is last in first out
    my_stack = Stack()
    print(my_stack.isEmpty())
    my_stack.push('Ted')
    my_stack.push('Katie')
    print(my_stack.isEmpty())
    print(my_stack.peek())

if __name__ == '__main__':
    main()