# Printing Hello world
print("Hello world!")

# Printing Variables
firstName = "Karra"
lastName = "NareshReddy"
print("firstName:" + firstName)
print("lastName:" + lastName)

# Printing Datatypes

print(type(firstName))
print(type(lastName))

# Multiple Variables

a, b, c = "abhi", "vamshi", "naresh"
print(a)
print(b)
print(c)

print(a + " " + b + " " + c)  # print in one line
print(a + "\n" + b + "\n" + c)  # print statement in new line

# Global Variables
age = 10


def printAge():
    print(age)


printAge()
print(age)

# Global variables
designation = "Python dev"
companyName = "Wipro"


def printEmployeeDetails():
    print("Designation:" + designation)
    print("Company Name:" + companyName)


printEmployeeDetails()

#
bikename = "Hero"
bikecolor = "Black"


def printBikeDetail():
    print("Bike Name: " + bikename)
    print("Bike color: " + bikecolor)


printBikeDetail()

# person details  firstname lastname email mobilenumber
# employee details empid empName designation salary

firstName = "Karra"
lastName = "NareshReddy"
emailId = "nareshreddykarra98@gmail.com"
mobileNumber = 9490097717
def printPersonDetails():
    print("FirstName: " +firstName)
    print("LastName: " +lastName)
    print("EmailId: " +emailId)
    print("Mobile Number:" + format(mobileNumber))

printPersonDetails()

empId = 94900
empName = "Abhi"
empDesignation = "Python dev"
empSalary = 28000


def printEmployeeDetails():
    print("EmployeeId:" +format(empId))
    print("EmployeeName: " + empName)
    print("EmployeDesignation: " + empDesignation)
    print("EmployeeSalary:" +format(empSalary))
printEmployeeDetails()
