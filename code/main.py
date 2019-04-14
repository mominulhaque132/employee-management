from employee import Employee


def load_data():
    file_name = '../resources/employee.txt'
    listEmployee = []
    with open(file_name) as f:
        for line in f:
            tokens = line.split(',')
            emp = Employee(tokens[0],tokens[1],tokens[2], tokens[3], tokens[4])
            listEmployee.append(emp)

    return listEmployee


def show_all_employee(listEmployee):
    for employee in listEmployee:
        print(employee.displayEmployee())


def find_employee_pos_in_list(id, listEmployee):
    for i in range(len(listEmployee)):
        if listEmployee[i].emp_id == str(id):
            return i
    return -1


def add_employee(emp_id, first_name, sure_name, email, salary):
    new_employee = Employee(emp_id, first_name, sure_name, email, salary);
    listEmployee.append(new_employee)


def remove_employee(emp_id, listEmployee):
    emp_index = find_employee_pos_in_list(emp_id, listEmployee);
    if emp_index != -1:
        del listEmployee[emp_index]


def change_salary(emp_id, new_salary, listEmployee):
    emp_index = find_employee_pos_in_list(emp_id, listEmployee);
    if emp_index != -1:
        listEmployee[emp_index].salary = new_salary

if __name__ == '__main__':

    # file read
    listEmployee = load_data()
    # show all employee
    show_all_employee(listEmployee)

    emp_index = find_employee_pos_in_list(67581, listEmployee);
    print(emp_index)

    add_employee(67582, 'mohadmmad', 'haque', 'm.haque@mycit.ie', 233223.0)
    print(len(listEmployee))

    remove_employee(67581, listEmployee);
    print(len(listEmployee))

    emp_index = find_employee_pos_in_list(67581, listEmployee);
    print(emp_index)

    change_salary(12345, 1234566, listEmployee);
    show_all_employee(listEmployee)
