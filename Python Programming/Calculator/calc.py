def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Can't be performed."
    else:
        return a/b

def main():
    print("CodSoft Calculator!")
    
    while True:
        try:
            print("press 1--> Addition")
            print("press 2--> Subtraction")
            print("press 3--> Multiplication")
            print("press 4--> Division")
            
            calculation = input("\n Enter your choice : ")
            
            a = float(input("\n Enter the first number: "))
            b = float(input(" Enter the second number: "))
            
            if calculation == '1':
                c = add(a, b)
                print(f"{a} + {b} =\n Answer :{c}")
            elif calculation == '2':
                c = subtract(a, b)
                print(f"{a} - {b} =\n Answer :{c}")
            elif calculation == '3':
                c = multiply(a, b)
                print(f"{a} * {b} =\n Answer :{c}")
            elif calculation == '4':
                c = divide(a, b)
                print(f"{a} / {b} =\n Answer :{c}")
            else:
                print("Invalid calculation choice. Please enter a number between 1 and 4.")

            again = input("\n For another calculation? press 1 (or) press 2: ").lower()
            
            if again != '1':
                print("Thank you for using the calculator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
