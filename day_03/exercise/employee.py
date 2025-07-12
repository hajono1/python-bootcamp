class Employee:
    def __init__(self, name, identity, tasks):
        self.name = name
        self.identity = identity
        self.tasks = tasks
    def time_in(self):
        print("time_in")
    def time_out(self):
        print("time_out")

#SUB HIERARCHY
class Recruiter(Employee):
    def __init__(self, name, identity, tasks):
        super().__init__(name,identity,tasks)
    def recruit(self):
        print ("recruit")
class Developer(Employee):
    def __init__(self, name, identity, tasks):
        super().__init__(name,identity,tasks)
    def code(self):
        print ("code")
class Manager(Employee):
    def __init__(self, name, identity, tasks):
        super().__init__(name,identity,tasks)
    def manage(self):
        print ("manage")

#Make Developer, Manager, and Recruiter
Developer1 = Developer("James", "Developer", "Code")
Developer1.time_in()