a=float(input("Enter marks in Telugu:  \t"))
b=float(input("Enter marks in Hindhi:  \t"))
c=float(input("Enter marks in English:  \t"))
d=float(input("Enter marks in maths:  \t"))
e=float(input("Enter marks in Scince:  \t"))
f=float(input("Enter marks in Social:  \t"))
avg = ((a+b+c+d+e+f) /600)*100

if (avg >= 80):
    print(" You have secured first Class, and your percentage is ", avg)
elif (avg >= 60 and avg < 80):
    print("You have secured Second Class , and your percentage is ",avg)
elif (avg>=40 and avg <60):
    print(" You have secured Third Class,and your percentage is ",avg)
elif  (avg < 40):
    print("You are fail")
