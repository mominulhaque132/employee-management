from employee import Employee
import sys
import random

def get_choices(menu_strings):
    """
     This mothod selects the user menu choices
    :param menu_strings: A list of menu choice
    :return: A particlar menu as user input.
    """
    print('Choices:')
    for i in range(len(menu_strings)):
        print(str(i+1) + ': '+ menu_strings[i])
    user_input = input('Enter your choice [1 - ' + str(len(menu_strings))+ ']: ')
    return user_input


def load_data():
    """
    This method read a file to load a list of Employee.
    :return: a list of Employee
    """
    file_name = '../resources/employee.txt'
    list_employee = []
    with open(file_name) as f:
        for line in f:
            tokens = line.rstrip('\n').split(',')
            emp = Employee(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4])
            list_employee.append(emp)

    return list_employee

def write_data(list_employee):
    """
    This method overwride employee.txt file using a new updated list of employee.
    :param list_employee: a list if Employee object.
    """
    file_name = '../resources/employee.txt'
    with open(file_name, 'w') as f:
        for employee in list_employee:
            f.write(str(employee.emp_id)+','+employee.first_name+','
                    +employee.sure_name+',' + employee.email +',' + str(employee.salary) + '\n')

def displayEmployee(employee):
    """
    Print an Empolyee object

    :param employee: an instance of Employee.
    """
    print(
        "ID:" + str(employee.emp_id) +
        ",First Name:" + employee.first_name +
        ",Sure Name:" + employee.sure_name +
        ",Email:" + employee.email +
        ",Salary:" + str(employee.salary)
    )


def show_all_employee(list_employee):
    """
    Display the list of employee

    :param list_employee: list of Employee
    """
    for employee in list_employee:
        displayEmployee(employee)


def find_employee_pos_in_list(id, list_employee):
    """
    Search a particular Employee with ID no.

    :param id: an Employee ID
    :param list_employee: List of Employees
    :return: index of an employee (-1 if not exist)
    """
    for i in range(len(list_employee)):
        if list_employee[i].emp_id == str(id):
            return i
    return -1

def generate_uniquie_id(list_employee):
    """
    Generates Unique Employee ID
    :param list_employee: List of Employees
    :return: New Employee ID
    """
    list_employee_id = []
    for i in range(len(list_employee)):
        list_employee_id.insert(len(list_employee_id), list_employee[i])

    valid = False
    while valid == False:
        new_id = random.randint(100000, 999999)
        if not new_id in list_employee_id:
            valid = True
    return new_id

def add_employee(emp_id, first_name, sure_name, email, salary):
    """
    Add new employee

    :param emp_id: Unique Employee ID
    :param first_name: First name of an employee
    :param sure_name:surname of an employee
    :param email: email address of an employee
    :param salary:salary of an employee
    :return: a new Employee
    """
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        return None
    new_employee = Employee(emp_id, first_name, sure_name, email, salary)
    list_employee.append(new_employee)
    return new_employee


def remove_employee(emp_id, list_employee):
    """
    Delete a particular Employee with unique employee ID

    :param emp_id: Unique Employee ID
    :param list_employee: an Employee list
    """
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        del list_employee[emp_index]
    else:
        print('ID: ' + str(emp_id) + ' is not associated with any employee.')


def change_salary(emp_id, new_salary, list_employee):
    """
    Update salary for a particular Employee
    :param emp_id: Unique Employee ID
    :param new_salary: Updated salary
    :param list_employee: a list of Employee
    :return: an employee (if exist) with new salary OR None, if not exist
    """
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        list_employee[emp_index].salary = new_salary
        return list_employee[emp_index]
    return None


def add_bonus(bonus_in_percentage, employee):
    """
    Calculate bonus for an employee based on given parcentage

    :param bonus_in_percentage: take the parcentage of bonus
    :param employee: lisyt of employee
    :return: A Tuple of (emp_ID, First name, last name, total bonus)
    """
    total_bonus = (float(employee.salary) * int(bonus_in_percentage)) // 100
    return employee.emp_id, employee.first_name, employee.sure_name, total_bonus


def generate_bonus_info(bonus_info_file, list_bonus, list_employee):
    """
    Generate bonus file

    :param bonus_info_file: a file to write bonus information
    :param list_bonus: a list of bonus for all employee
    :param list_employee: Employee list
    """
    list_employee_with_bonus = []
    for i in range(len(list_employee)):
        list_employee_with_bonus.append(add_bonus(list_bonus[i], list_employee[i]))

    with open(bonus_info_file, 'w') as f:
        for item in list_employee_with_bonus:
            f.write(str(item[0])+','+item[1]+','+item[2]+','+str(item[3])+'\n')
    print('All bonuses are written in a file=' + bonus_info_file)


def get_bonus_input(list_employee):
    """
    This method takes input from user to give a percentage of bonus to each employee.

    :param list_employee: Employee list
    :return:a list of bonuses (how much Bonus gets every Employee)
    """
    list_bonus = []
    for i in range(len(list_employee)):
        bonus = input(str(list_employee[i].emp_id) + ': Add bonus=')
        list_bonus.append(bonus)

    return list_bonus

def generate_reports(list_employee):
    """
    Generates and display a report to show Average salary and the employees with maximum salary.
    :param list_employee:a list of Employee
    """
    sum = 0
    max = 0;
    for employee in list_employee:
        sum = sum + float(employee.salary)
        if max < float(employee.salary):
            max = float(employee.salary)

    average_salary = sum / len(list_employee)
    print('Average Salary='+str(average_salary))
    print('Employees with max salary=' + str(max))
    for employee in list_employee:
        if float(employee.salary) == max:
            displayEmployee(employee)



if __name__ == '__main__':

    menu_strings = [
        'View all employee',
        'View a particular employee',
        'Edit the salary of an employee',
        'Add a new employee',
        'Delete an employee',
        'Give a bonus to each employee and writes the details to a file',
        'Generate a report for management',
        'Quit and Save Reports'
    ]

    list_employee = load_data()
    # This loop get choices from user.
    while True:
        user_input = get_choices(menu_strings);
        if (int(user_input) >= len(menu_strings)) or (int(user_input) <= 0):
            print('Write updated employee list in file and exit')
            write_data(list_employee)
            sys.exit(0)
        if int(user_input) == 1:
            show_all_employee(list_employee)
        elif int(user_input) == 2:
            emp_id = input('Enter employee ID=')
            pos = find_employee_pos_in_list(emp_id, list_employee)
            print(pos)
            if pos != -1:
                displayEmployee(list_employee[pos])
            else:
                print('ID: '+ str(emp_id) + ' is not associated with any employee.')
        elif int(user_input) == 3:
            emp_id = input('Enter employee ID=')
            new_salary = input('Enter new salary=')
            employee = change_salary(emp_id, new_salary, list_employee)
            if employee is None:
                print('ID: '+ str(emp_id) + ' is not associated with any employee.')
            else:
                displayEmployee(employee)
        elif int(user_input) == 4:
            emp_id = generate_uniquie_id(list_employee)
            first_name = input('Enter first name=')
            sure_name = input('Enter sure name=')
            email = first_name + '.' + sure_name +'.' + str(emp_id) + '@mycit.ie'
            salary = input('Enter salary=')
            employee = add_employee(emp_id, first_name, sure_name, email, salary)
            if employee is None:
                print('ID: '+ str(emp_id) + ' is already exist')
            else:
                displayEmployee(employee)
        elif int(user_input) == 5:
            emp_id = input('Enter employee ID=')
            remove_employee(emp_id, list_employee)
        elif int(user_input) == 6:
            list_bonus = get_bonus_input(list_employee)
            generate_bonus_info('../resources/bonus.txt', list_bonus, list_employee)
        else:
            print('generate report')
            generate_reports(list_employee)
