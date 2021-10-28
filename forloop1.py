"""#syntax for x in sequence:
             body
             where sequence can be string or any collections
             Body will be executed for every element presents in the sequence:  """

#
s="NareshReddy"
for i in s:
    print(i)

#  To print characters present in string index wise:
s=input("Enter Some String: ")
i=0
for x in s:
    print("The character present at ",i,"index is :",x)
    i=i+1

# To print Hello 10 times
for x in range(0,10):
    print("Hello")

# Range 0 to 10    1,2,3,4,5,6,7,8,9
for x in range(0,10):
    print(x)

# To display numbers from 0 to 10
for i in range(11):
    print(i)

#  To display odd numbers from 0 to 20
for x in range(21):
    if(x%2!=0):
        print(x)

# To display even numbers from 0 to 30
for x in range(31):
    if(x%2==0):
        print(x)

#  To display numbers from 10 to 1 in descending order
for x in range(10,0,-1):
    print(x)

#To print sum of numbers presenst inside list

list = eval(input("Enter list: "))
sum=0;
for x in list:
    sum=sum+x;
print("The Sum=",sum)
