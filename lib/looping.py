#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(f"{counter}")
        counter -=1
    print("Happy New Year!")
        
    # code goes here!
    pass

def square_integers(int_list):
    return [n ** 2 for n in int_list]
    # code goes here!
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
            
        elif i % 3 == 0:
            print("Fizz")
            
        elif i % 5 == 0:
            print("Buzz")
            
        else:
            print(i)
    # code goes here!
    
    pass
#happy_new_year()
#print(square_integers([1, 2, 3, 4, 5]))