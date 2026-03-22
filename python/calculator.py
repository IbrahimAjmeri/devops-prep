def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
    
    # Add this at the bottom of calculator.py

if __name__ == "__main__":
    print("Welcome to Calculator!")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Get Grade")
    
    choice = input("Choose (1/2/3/4): ")
    
    if choice in ["1", "2", "3"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == "1":
            print(f"Answer: {add(a, b)}")
        elif choice == "2":
            print(f"Answer: {subtract(a, b)}")
        elif choice == "3":
            print(f"Answer: {multiply(a, b)}")
    
    elif choice == "4":
        marks = float(input("Enter marks: "))
        print(f"Grade: {get_grade(marks)}")