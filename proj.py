class Person:
    def __init__(self, first_name, last_name, date_of_birth, address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"can't compare {type(self)} with {type(other)}")

        __checks = (
            self.first_name == other.first_name,
            self.last_name == other.last_name,
            self.date_of_birth == other.date_of_birth,
            self.address == other.address
        )
        return all(__checks)
class Company:
    __departments = []
    __employees = []

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__mission_statement = "We make the world a better place"
        self.__revenue = 0

    def __str__(self):
        return self.__name + ", " + self.__address + ", Phone:" + self.__phone

    def add_department(self, department):
        self.__departments.append(department)

    def __add_employee_to_company(self, emp):
        self.__employees.append(emp)

    def remove_department(self, department):
        if department in self.__departments:
            self.__departments.remove(department)
        else:
            print("Department not found")


    def set_mission_statement(self, mission_statement):
        self.__mission_statement = mission_statement


    def get_mission_statement(self):
        return self.__mission_statement

    def set_rev(self, revenue):
        if revenue < 0:
            print("Revenue cannot be negative")
        else:
            self.__revenue = revenue


    def get_rev(self):
        return self.__revenue


    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name





import random


class Employee(Person):

    # Private Class attributes
    __LVL_1_BASE_SALARY = 2000
    __LVL_2_BASE_SALARY = 4000
    __LVL_3_BASE_SALARY = 8000

    # If Person already exists we can just create it like this
    @classmethod
    def from_person(cls, person, company,department):
        return cls(
            person.first_name,
            person.last_name,
            person.date_of_birth,
            person.address,
            company,
            department
            
        )

    def __init__(self, first_name, last_name, date_of_birth, address, company,department, level=1):
        super().__init__(first_name, last_name, date_of_birth, address)

        self.id = random.randint(1, 99999)
        if isinstance(company, Company) and isinstance(department,Department):  # To handle when we create Manager from Employee, company is Employee.company which is a string already
            self.company = company.get_name()
            self.department=department.dept_name
        else: 
            self.company = company
            self.department=department
            
        self.__level = level
        self.__status = 'Employee'
        
        # Setting default salaries --> TODO BASE_SALARY should come from company?   it will come from HR. check this method,please
        def __set_default_salary(self,hr_employee,level):
          if isinstance(hr_employee, Human_resources):
            if self.__level == 3:
                self.__salary = self.__LVL_3_BASE_SALARY
            elif self.__level == 2:
                self.__salary = self.__LVL_2_BASE_SALARY
            else:
            # lvl 1 salary for every one else
                self.__salary = self.__LVL_1_BASE_SALARY

    def show(self):
        # Show public details of employee
        print(f"\n---------- ID: {self.id} ------------")
        print(f"First Name:\t\t {self.first_name}")
        print(f"Last Name:\t\t {self.last_name}")
        print(f"Date of Birth:\t\t {self.date_of_birth}")
        print(f"Address:\t\t {self.address}")
        print(f"Company:\t\t {self.company}")
        if hasattr(self, 'email'):
            print(f"Email:\t\t\t {self.email}")
            
    def private(self,hr_employee):
        # TODO make it private for HR?
        if isinstance(hr_employee,Human_resources):
        # Show all (public+private) details of employee
            self.show()
            print(f"Status:\t\t\t {self.__status}")
            print(f"Level:\t\t\t {self.__level}")
            print(f"Salary:\t\t\t {self.__salary}")
        
        
    def create_email(self,hr_employee):
        # TODO make it private for the HR?   yesss
        if isinstance(hr_employee,Human_resources):
        # Creates employee email justs if not exists already
            try:
                getattr(self, "email")
                print(f"Email for {self.first_name} {self.last_name} already exists")
            except AttributeError:
                self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@{self.company.lower()}.com"
                print(f"Created email: {self.email}")
            
    def get_email(self):
        # Get employee email
        try:
            return getattr(self, "email")
        except AttributeError:
            print(f"Email for {self.first_name} {self.last_name} doesn't exists in database")
            
            
    def set_email(self, email,hr_employee):
        # TODO make it private for the HR?       yesss
        if isinstance(hr_employee,Human_resources):
        # Change employee email
            try:
                curr_email = getattr(self, "email")
                changeEmail = input(f"Current email is {curr_email} change it to {email}@{self.company.lower()}.com? Yes/No: \t")
                if 'y' in changeEmail.lower():
                    self.email = f"{email}@{self.company.lower()}.com"
                    print(f"Email changed succesfuly.")
                else:
                    print(f"Email not changed.")
            except AttributeError:
                self.email = f"{email}@{self.company.lower()}.com"
                print(f"Created email: {self.email}")
            
    def __get_salary(self,boss_hr_employee):
        # Get employee salary                # only HR&boss can get the salary so...
        if isinstance(boss_hr_employee,(Human_resources, Boss)):
            try:
                print(getattr(self, 'salary'))
              
            except AttributeError:
                print(f"Employee {self.first_name} {self.last_name} has no salary!!!")
        else:
            raise ValueError('Not Allowed!')
            
    #def set_salary(self, salary:float)->float:    
        # TODO make it private for the HR?  yesss
    def __set_salary__(self,hr_employee,salary:float)->float:
        if isinstance(hr_employee,Human_resources):
#            self.__salary=salary
    

#        try:
#            salary = float(salary)
 #       except Exception as ex:
 #           print(f"Couldn't set salary. '{salary}' is not a valid salary input.")            
            try:
                prev_salary = getattr(self, "salary")
                changeSalary = input(f"Current salary is {prev_salary} change it to {salary}.com? Yes/No")
                if 'y' in changeSalary.lower():
                    self.salary = salary
                    print(f"Salary changed succesfuly.")
                else:
                    print(f"Salary not changed.")
            except AttributeError:
                self.salary = salary
                print(f"Salary set succesfuly.")
        else:
            print('Not allowed')
            

class Manager(Employee):

    # If Empolyee already exists we can just create it like this
    @classmethod
    def from_employee(cls, employee):
        return cls(
            employee.first_name,
            employee.last_name,
            employee.date_of_birth,
            employee.address,
            employee.company
        )

    def __init__(self, first_name, last_name, date_of_birth, address, company, level=2):
        super().__init__(first_name, last_name, date_of_birth, address, company, level)

        self.status = "Manager"
        self.__team = []

    def add_to_team(self, hr_employee,employee):
        # TODO make it private for HR?
        if isinstance(hr_employee,Human_resources):
            self.__team.append(employee)

    def show_team(self):
        print(f"Current team:")
        for m, member in enumerate(self.__team):
            print(f"\t {m}. {member.first_name} {member.last_name}")
    
    def get_team(self):
        return self.__team

    def get_employee_salary(self, manager_hr_employee,employee):
        # Only if employee is in managers team
        if isinstance(manager_hr_employee,(Human_resources, Boss,Manager)):
            if employee in self.__team:
            #self._Employee__see_salary(employee)
                return employee._Employee__get_salary()
            else:
                print(f"You don't have access to {employee.name} salary")
            
class Boss(Manager):
    # If Manager already exists we can just create it like this
    @classmethod
    def from_manager(cls, manager):
        return cls(
            manager.first_name,
            manager.last_name,
            manager.date_of_birth,
            manager.address,
            manager.company
        )

    def __init__(self, first_name, last_name, date_of_birth, address, company, level=3):
        super().__init__(first_name, last_name, date_of_birth, address, company, level)
        self.status = "Boss"

    def show_team(self):
        print(f"Current team:")
        for m, member in enumerate(self.__team):
            print(f"\t {m}. {member.first_name} {member.last_name}")
    
    def get_team(self):
        return self.__team

    def get_employee_salary(self,hr_boss_employee,employee):
        # Boss can see everyone's salary
        if isinstance (hr_boss_employee,(Human_resources, Boss)):
            return employee._Employee__get_salary(hr_boss_employee)
        else:
            raise ValueError('Not Allowed!')


            
class Department(Company):
    Department_employees= []
    def __init__(self, company_name, company_address, company_phone, dept_name):
        super().__init__(company_name, company_address, company_phone)
        
        self.dept_name = dept_name

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            Department.Department_employees.append(employee)
            print(Department.Department_employees)
        else:
            raise TypeError("wrong type")
 #       self.employee_list.append(employee)
  #      return self.employee_list
    def __str__(self):
        return f"Department {self.dept_name} at {self.get_name()} Co."
        
    


class Human_resources(Employee):
    HR_employees=[]
    @classmethod
    def from_employee(cls,employee):
        return cls(
            employee.first_name,
            employee.last_name,
            employee.date_of_birth,
            employee.address,
            employee.company,
            employee.department,
            employee._Employee__level
        )
    def __init__(self, first_name, last_name, date_of_birth, address, company,department, level=1):
        super().__init__(first_name, last_name, date_of_birth, address, company,department, level)
    
    def set_name(self,employee):
        if isinstance(employee,Employee):
            self.first_name=employee.first_name
            self.last_name=employee.last_name
            self.company=employee.company
            self.department=employee.department
            self.date_of_birth=employee.date_of_birth
            self.address=employee.address
            self.__level=employee.__level
            Human_resources.HR_employees.append(employee)
    def __setattr__(self,name,value):
            if name not in ('first_name', 'last_name', 'company', 'date_of_birth', 'address', '_Employee__level','id','department','_Employee__status'):
                 raise AttributeError("Attribute not allowed")
            super().__setattr__(name, value)


class Production(Department):
    def __init__(self, name, address, phone, employee, Position, salary):
        super().__init__(name, address, phone, employee, Position)
        self.__salary = salary

if __name__ == "__main__":
    p1=Person('rovan','elgendy','14 May 1995','Munich')
    p2=Person('Mary','Clark','10 June 1990','England')
    p3=Person('John','Smith','22 October 1997','England')
    c1 = Company("Google", "Mountain View",'10747567')
    c2=Company('Wiley Edge','England','244765')
   # print(c1)
    d1=Department(c1.get_name(),c1.get_address(),c1.get_phone(),'IT')
    d2=Department(c1.get_name(),c1.get_address(),c1.get_phone(),'Quality')
    print(d1)
    e1=Employee.from_person(p1,c1,d1)
    e2=Employee.from_person(p3,c2,d1)
    print(e1)
    print(e1.show())
    print(e2.show())
    hr1=Human_resources(e1.first_name,e1.last_name,e1.date_of_birth,e1.address,e1.company,e1.department,e1._Employee__level)
    print(hr1.__dict__)
    
    e1.__set_salary__(hr1,4000)  # set successfully as hr1 is an HR employee
    e1.__set_salary__(p1,4000)   # will give error because p1 is not an HR employee
   # print(e1.__dict__)
    e3=Employee.from_person(p2,c1,d1)
    #print(e3.__dict__)
    hr2=Human_resources.from_employee(e3)
  #  print(hr2.__dict__)
    B1=Boss.from_employee(e3)
    #print(B1.__dict__)
 #   B1.get_employee_salary(e1,e1)   # Not allowed
    B1.get_employee_salary(B1,e1)
    

    #print("mission statement: " + c1.get_mission_statement())
    #c1.set_rev(1000000000)
    #print("revenue: " + str(c1.get_rev()))        