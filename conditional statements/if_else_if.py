# if else is else statement

time=input("enter time")
x=time.lower()
if x=="morning":
    print("Good morning")
elif x=="Afternoon" or "Eveninng":
    print("good afternoon/evening")
else:
     print("invalid time")


# Define a variable
x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")

# Another example
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
