class Employee:
    @abstractmethod
    def calculate_salary():
        pass
class Intern(Employee):
    def __init__(self,workingdays,dailywage):
        self.workingdays=workingdays
        self.dailywage=dailywage
    def calculate_salary():
        

class FullTimeEmployee(Employee):
class ContractEmployee(Employee):