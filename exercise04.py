"""
    迭代员工管理器
    要求:自行推导
"""
class EmployeeController:
    def __init__(self):
        self.__list_employees = []

    def add_employee(self, graphic):
        self.__list_employees.append(graphic)


controller = EmployeeController()
controller.add_employee("程序员")
controller.add_employee("销售员")
controller.add_employee("测试员")
for item in controller:
    print(item)
