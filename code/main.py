from employee import Employee


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


def find_employee_pos_in_list(id, list_employee):
    for i in range(len(list_employee)):
        if list_employee[i].emp_id == str(id):
            return i
    return -1


def add_employee(emp_id, first_name, sure_name, email, salary):
    new_employee = Employee(emp_id, first_name, sure_name, email, salary)
    list_employee.append(new_employee)


def remove_employee(emp_id, list_employee):
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        del list_employee[emp_index]


def change_salary(emp_id, new_salary, list_employee):
    emp_index = find_employee_pos_in_list(emp_id, list_employee)
    if emp_index != -1:
        list_employee[emp_index].salary = new_salary


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


def get_bonus_input(list_employee):
    list_bonus = []
    for i in range(len(list_employee)):
        bonus = input(str(list_employee[i].emp_id) + ': Add bonus=')
        list_bonus.append(bonus)

    return list_bonus


if __name__ == '__main__':

    # file read
    list_employee = load_data()
    # show all employee
    show_all_employee(list_employee)

    emp_index = find_employee_pos_in_list(67581, list_employee)
    print(emp_index)

    add_employee(67582, 'mohadmmad', 'haque', 'm.haque@mycit.ie', 233223.0)
    print(len(list_employee))

    remove_employee(67581, list_employee)
    print(len(list_employee))

    emp_index = find_employee_pos_in_list(67581, list_employee)
    print(emp_index)

    change_salary(12345, 1234566, list_employee)
    show_all_employee(list_employee)

    list_bonus = get_bonus_input(list_employee)
    generate_bonus_info('../resources/bonus.txt', list_bonus, list_employee)
