#encapsulation : wrapping data and behaviours/methods into single unit
# making a class that has related methods and data is the example of encapsulation

## ----------- NOTE ------------------##

# There is NO TRUE DATA HIDING (public,protected,private) in PYTHON 
# it means in python private, protected , public variables can be accessed outside the class 
# in python no matter variable is public , protected, private it can be accessible outside the class

class BankAccount :
    def __init__(self,acc_no,holder_name,balance):
        self._acc_no=acc_no # protected
        self.holder_name=holder_name # public 
        self.__balance=balance # private 

acc1=BankAccount(101,"prashant kumar",70_000)
acc2=BankAccount(102,"sumit kumar",10_000)

print(acc1._BankAccount__balance) # private variable accessed
print(acc2._acc_no) # protected var accessed
print(acc1.holder_name) # public var accessed

## ----------------------ETHICS---------------------------

# - always make getters & setters methods inside class to get access & set val of protected & private var
    