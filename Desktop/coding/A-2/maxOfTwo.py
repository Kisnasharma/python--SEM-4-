a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
if a > b :
    print("Max number is : ",a)
else:
    print("Max number is : ",b)

# or second way 
print("Max number is : ",a if a > b else b)
# or third way
print("Max number is : ",max(a,b))

