brand = input("Enter your Favourite band: ")
if brand=="Rc":
    print("it is childrens band")
elif brand=="kf":
    print("it is not that much kick")
elif brand=="Fo":
    print("Buy one get Free One")
else:
    print("Other Brands are not recommended")
#Q. Write a program to find biggest of given 2 numbers from the commad prompt?
n1=input("Enter First number:")
n2=input("Enter second number:")
if n1>n2:
    print("Biggest number is:",n1)
else:
    print("Biggest number is:",n2)

# Q. Write a program to find biggest of given 3 numbers from the commad prompt?
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest number is ",n1)
elif n2>n3:
    print("Biggest number is ",n2)
else:
    print("Biggest number is ",n3)
#Q. Write a program to find smallest of given 2 numbers?
n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
if n1<n2:
    print("The Smallest number is: ",n1)
else:
    print("The Smallest number is: ",n2)

# Q. Write a program to find smallest of given 3 numbers?
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1<n2 and n1<n3:
    print("The Smallest Number is: ",n1)
elif n2<n3:
    print("The Smallest Number is: ",n2)
else:
    print("The Smallest Number is: ",n3)

#Q. Write a program to check whether the given number is even or odd?
n=int(input("Enter the number: "))
if (n%2)==0:
    print("The number is even")
elif (n%2)!=0:
    print("The number is odd")
#Q. Write a program to check whether the given number is in between 1 and 100?
n=int(input("Enter the Number: "))
if n>1 and n<10:
    print("The number",n,"is in between 1 to 10")
else:
    print("The number",n,"is not between 1 to 10")

#Write a program to take a single digit number from the key board and print is value in
#English word?
#0==>ZERO
#1==>ONE

n=int(input("Enter a digit from 0 to 9:"))
if n==0:
    print("Zero")
elif n==1:
    print("One")
elif n==2:
    print("Two")
elif n==3:
    print("Three")
elif n==4:
    print("Four")
elif n==5:
    print("Five")
elif n==6:
    print("Six")
elif n==7:
    print("Seven")
elif n==8:
    print("Eight")
elif n==9:
    print("Nine")
else:
    print("Please enter a digit from 0 to 9 :")