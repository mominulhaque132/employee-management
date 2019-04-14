class Employee:
    def __init__(self, emp_id, first_name, sure_name, email, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.sure_name = sure_name
        self.email = email
        self.salary = salary

    def displayEmployee(self):
        print (
            "ID : ", self.emp_id,
            ", First Name : ", self.first_name,
            ", Sure Name : ", self.sure_name,
            ", Email : ", self.email,
            ", Salary: ", self.salary
        )