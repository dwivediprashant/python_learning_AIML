class Student :
    college_name="LNCT" # class variables

    def __init__(self,name,branch,cgpa): # constructor : to initalize instance variables ; only one per class
        self.name=name
        self.branch=branch
        self.cgpa=cgpa
    
    # instance methods can access both class variables (here : college_name) & instance var(name,branch,cgpa)
    def get_info(self):  # instance method ; must have self as 1st parameter that refers to calling object 
        print(f"{self.name} enrolled in {self.branch} in {self.college_name} and has gpa {self.cgpa}")

    @classmethod
    def get_college(cls): # class methods can not access instance variables here name ; they can only access class var
        print(f"College name is {cls.college_name}")

    # static methods can not access class & instance methods
    # static methods are used so that related data/fnx stored in same class 
    @staticmethod
    def calc_percentage(cgpa):
        percentage=cgpa*10
        print(percentage,"%")


s1=Student("prashant","AIML",8.77)
s2=Student("amit","CSE",8.98)
s3=Student("Sumit","ME",8.97)

s1.get_info()
s1.get_college()
s1.calc_percentage(8.77)
