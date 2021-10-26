##instance class example

class Student:
    def __init__(self,name,rollno,mobileno,collegename,branch):
        self.name=name
        self.rollno=rollno
        self.mobileno=mobileno
        self.collegename=collegename
        self.branch=branch

    def display(self):
        print("My Name is :" ,self.name)
        print("My Rollno is :" ,self.rollno)
        print("My Mobile no is :" ,self.mobileno)
        print("My CollegeName is :" ,self.collegename)
        print("My Branch is :" ,self.branch)

s=Student("NareshReddy","15UM1A0544",9490097717,"Vaageswari college of engineering","CSE")
s.display()

# Student details:
# Student name
# Student roll no
# Student branch
# Student Mobile no
# Student age

class Student:
    def __init__(self,name,rollno,branch,mobileno,age):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.mobileno=mobileno
        self.age=age

    def display(self):
        print("Student name is :" ,self.name)
        print("Student RollNo is :" ,self.rollno)
        print("Student Branch is :" ,self.branch)
        print("Student MobileNo is :" ,self.mobileno)
        print("Student age is :" ,self.age)

s=Student("NareshReddy","15UM1A0544","CSE",9490097717,23)
s.display()
