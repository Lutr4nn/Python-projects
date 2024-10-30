#Make by Lutr4nn
# -*- coding: utf-8 -*-

def main():
    number1 = input('Enter your first number :')
    opération = input("What operation do you want to do? ['+', '-', '*' ou '/']")
    number2 = input('Enter your second number :')
    
    result = 0

    if not number1.isnumeric() or not number2.isnumeric():
        print('Please use number')
    else: 
         number1 = int(number1)
         number2 = int(number2)
    
    match opération:
         case '+':
              result = number1 + number2
         case '-':
              result = number1 - number2
         case '*':
              result = number1 * number2
         case '/':
             if number2 == 0:
                 print('You cannot divide by zero')
             else:
               result = number1 / number2
         case _:
              print('Please use an operative symbol')
    print(f'The result of the operation is: {result}')        

if __name__ == "__main__":
    main()
            

