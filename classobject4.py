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