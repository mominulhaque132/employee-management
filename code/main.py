from employee import Employee
import sys

def get_choices(menu_strings):
    print('Choices:')
    for i in range(len(menu_strings)):
        print(str(i+1) + ': '+ menu_strings[i])
    user_input = input('Enter your choice [1 - ' + str(len(menu_strings))+ ']: ')
    return user_input

def load_data():
    file_name = '../resources/employee.txt'
    list_employee = []
    with open(file_name) as f:
        for line in f:
            tokens = line.split(',')
            emp = Employee(tokens[0],tokens[1],tokens[2], tokens[3], tokens[4])
            list_employee.append(emp)

    return list_employee


def show_all_employee(list_employee):
    for employee in list_employee:
        print(employee.displayEmployee())


def show_an_employee(emp_id, list_employee):
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    print(emp_index)
    if emp_index != -1:
        list_employee[emp_index].displayEmployee()


def find_employee_pos_in_list(id, list_employee):
    for i in range(len(list_employee)):
        if list_employee[i].emp_id == str(id):
            return i
    return -1


def add_employee(emp_id, first_name, sure_name, email, salary):
    new_employee = Employee(emp_id, first_name, sure_name, email, salary)
    list_employee.append(new_employee)
    return new_employee


def remove_employee(emp_id, list_employee):
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        del list_employee[emp_index]


def change_salary(emp_id, new_salary, list_employee):
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        list_employee[emp_index].salary = new_salary
    return list_employee[emp_index]


def add_bonus(bonus_in_percentage, employee):

    total_bonus = (float(employee.salary) * int(bonus_in_percentage)) // 100
    return employee.emp_id, employee.first_name, employee.sure_name, total_bonus


def generate_bonus_info(bonus_info_file, list_bonus, list_employee):
    list_employee_with_bonus = []
    for i in range(len(list_employee)):
        list_employee_with_bonus.append(add_bonus(list_bonus[i], list_employee[i]))

    with open(bonus_info_file, 'w') as f:
        for item in list_employee_with_bonus:
            f.write(str(item[0])+','+item[1]+','+item[2]+','+str(item[3])+'\n')
    print('All bonuses are written in a file=' + bonus_info_file)


def get_bonus_input(list_employee):
    list_bonus = []
    for i in range(len(list_employee)):
        bonus = input(str(list_employee[i].emp_id) + ': Add bonus=')
        list_bonus.append(bonus)

    return list_bonus


if __name__ == '__main__':

    menu_strings = [
        'View all employee',
        'View a particular employee',
        'Edit the salary of an employee',
        'Add a new employee',
        'Delete an employee',
        'Give a bonus to each employee and writes the details to a file',
        'Quit'
    ]
    list_employee = load_data()
    while True:
        user_input = get_choices(menu_strings);
        if (int(user_input) >= len(menu_strings)) or (int(user_input) <= 0):
            sys.exit(0)
        if int(user_input) == 1:
            show_all_employee(list_employee)
        elif int(user_input) == 2:
            emp_id = input('Enter employee ID=')
            pos = find_employee_pos_in_list(emp_id, list_employee)
            print(pos)
            list_employee[pos].displayEmployee()
        elif int(user_input) == 3:
            emp_id = input('Enter employee ID=')
            new_salary = input('Enter new salary=')
            employee = change_salary(emp_id, new_salary, list_employee)
            employee.displayEmployee()
        elif int(user_input) == 4:
            emp_id = input('Enter employee ID=')
            first_name = input('Enter first name=')
            sure_name = input('Enter sure name=')
            email = input('Enter email=')
            salary = input('Enter salary=')
            employee = add_employee(emp_id, first_name, sure_name, email, salary)
            employee.displayEmployee()
        elif int(user_input) == 5:
            emp_id = input('Enter employee ID=')
            remove_employee(emp_id, list_employee)
        else:
            list_bonus = get_bonus_input(list_employee)
            generate_bonus_info('../resources/bonus.txt', list_bonus, list_employee)

