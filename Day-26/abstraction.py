'''

from abc import ABC, abstractmethod

class BankAccount(ABC):

    def checkbalance(self):
        print("You can check your balance")

    def viewhistory(self):
        print("You can view your transactions")

    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through net banking")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class CurrentAccount(BankAccount):

    def deposit(self):
        print("You can deposit - Current Account")

    def withdraw(self):
        print("You can withdraw - Current Account")


class SavingAccount(BankAccount):

    def deposit(self):
        print("You can deposit - Saving Account")

    def withdraw(self):
        print("You can withdraw - Saving Account")


class FixedDeposit(BankAccount):

    def deposit(self):
        print("You can deposit - Fixed Deposit")

    def withdraw(self):
        print("Withdrawal is not allowed before maturity.")


class SalaryAccount(BankAccount):

    def deposit(self):
        print("You can deposit - Salary Account")

    def withdraw(self):
        print("You can withdraw - Salary Account")


class ZeroBalanceAccount(BankAccount):

    def deposit(self):
        print("You can deposit - Zero Balance Account")

    def withdraw(self):
        print("You can withdraw - Zero Balance Account")


subbu = ZeroBalanceAccount()
subbu.deposit()
subbu.withdraw()
subbu.checkbalance()
subbu.viewhistory()
subbu.userinfo()
subbu.transactions()

print()

srikanth = ZeroBalanceAccount()
srikanth.deposit()
srikanth.withdraw()
srikanth.checkbalance()
srikanth.viewhistory()
srikanth.userinfo()
srikanth.transactions()
'''

from abc import ABC, abstractmethod

# Abstract Class
class Student(ABC):

    # Constructor
    def __init__(self, name, rollno):
        self.name = name          # Instance Variable
        self.rollno = rollno      # Instance Variable

    # Instance Method
    def student_details(self):
        print("Name :", self.name)
        print("Roll No :", self.rollno)

    # Instance Method
    def attendance(self):
        print("Attendance is available.")

    # Instance Method
    def exams(self):
        print("You can view exam schedule.")

    # Abstract Method
    @abstractmethod
    def course(self):
        pass

    # Abstract Method
    @abstractmethod
    def fee(self):
        pass


# Child Class
class EngineeringStudent(Student):

    def course(self):
        print("Course : Engineering")

    def fee(self):
        print("Fee : Rs. 80,000")


# Child Class
class MedicalStudent(Student):

    def course(self):
        print("Course : Medical")

    def fee(self):
        print("Fee : Rs. 1,20,000")


# Child Class
class DegreeStudent(Student):

    def course(self):
        print("Course : Degree")

    def fee(self):
        print("Fee : Rs. 40,000")


# Creating Objects
student1 = EngineeringStudent("Srikanth", 101)

student1.student_details()
student1.course()
student1.fee()
student1.attendance()
student1.exams()

print()

student2 = MedicalStudent("Rahul", 102)

student2.student_details()
student2.course()
student2.fee()
student2.attendance()
student2.exams()














































