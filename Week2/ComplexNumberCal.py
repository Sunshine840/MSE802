#Author: Sanjeev Kumar
# About this program: Simple Complex Number Calculator

print("Complex Number Calculator")

# Input complex numbers like: 3+2j  or  5-4j
c1 = complex(input("Enter first complex number: "))
c2 = complex(input("Enter second complex number: "))

print("\nChoose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")

if choice == "1":
    result = c1 + c2
elif choice == "2":
    result = c1 - c2
elif choice == "3":
    result = c1 * c2
elif choice == "4":
    result = c1 / c2
else:
    result = "Invalid option!"

print("\nResult:", result)
