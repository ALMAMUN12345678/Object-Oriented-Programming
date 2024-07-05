class Person:
    def __init__(self, person_name:str, date_of_birth:int, ht:int = None):
        self.name = person_name
        self.dof = date_of_birth
        self.height = ht
        self.abc = None

    def get_dof(self):
        return self.dof

    def get_name(self):
        return self.name

    def get_date_f(self):
        return self.dof

    def get_ht(self):
        return self.height
    def set_name(self,new_name):
        if self.__has_any_number(new_name):
            print("Sorry! Person Name will not be numeric:>>>>>> ")
            return
        self.name = new_name
    def __has_any_number(self,string):
        return "0" in string

    def get_summary(self):
        return f"name:{self.name},date of birth:{self.dof},Height:{self.height if self.height is not None else 'Invalid'}"
    # def __str__(self):
    #     return f"name:{self.name},date of birth:{self.dof},Height:{self.height if self.height is not None else 'Invalid'}"




# a_name = Person("mamun",13,56)
# a_name.name = "000Mamun"
# a_name.set_name("0Muhammad Al Mamun")
# print(a_name.get_summary())
person_list = []
person_list.append(Person("Mamun",1996,25))
person_list.append(Person("Shahad",2004,27))
person_list.append(Person("Labib",1996,40))
person_list.append(Person("Shabit",2001))
person_list.append(Person("Lotion",1990,82))
person_list.append(Person("Emon",1993,18))
print(person_list)
for person in person_list:
    if person.get_dof() >= 1991:
        print(person.get_summary())



class Student(Person):
    def __init__(self, person_name: str, date_of_birth: int,email_id: str, student_id:str):
        super().__init__(person_name, date_of_birth)
        self.email_id = email_id
        self.student_id = student_id
    def get_summary(self):
        return f"Name:{self.get_name()} Email:{self.email_id} Birth:{self.get_dof()}"
# student = Student("Mamun",2185,"Mamun@123","234435324")
# print(student.get_summary())
# student.set_name("Muhammad Mamun")
# print(student.get_summary())

class Teacher(Person):
    def __init__(self, person_name: str, date_of_birth: int,department:str):
        super().__init__(person_name, date_of_birth)
        self.department = department
    def get_summary(self):
        return f"Name:{self.get_name()} Date Of Birth:{self.get_dof()} Department:{self.department}"
new_list = [Person("Mamun",1995,25),
            Student("Khan",1996,"mamun@","1332324sf"),
            Teacher("Muhammad",1997,"OCG")]

for p in new_list:
    print(p.get_summary())


# class Person:
#     def __init__(self, person_name):
#         self.name = person_name
#
#     def get_name(self):
#         return self.name
#
# a_name = Person("mamun")
# print(a_name.get_name())

# class Sum:
#     def __init__(self, num_1, num_2):
#         print(num_1*num_2)
# Sum(100, 200)

# class Sum:
#     def __init__(self, num_1, num_2):
#
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#
#     def number_sum(self):
#         return self.num_1 * self.num_2
#
# sum_2 = Sum(20, 190)
# print(sum_2.number_sum())

# class Fruits:
#     def __init__(self,bananna):
#         self.bananna_1 = bananna
# f = Fruits("Apple")
# print(f.bananna_1)

# class Item:
#     pay_rate = 0.83
#     def __init__(self,customer_id,name,sales_1:int, sales_2:int):
#         assert sales_1 >= 0, f"Sales_1{sales_1} is  greater than or equal to zero"
#         assert sales_1 >= 0, f"Sales_1{sales_2} is  greater than or equal to zero"
#         self.customer_id = customer_id
#         self.name = name
#         self.sales_1 = sales_1
#         self.sales_2 = sales_2
#
#     def set_customer_id(self):
#         return self.customer_id
#     def set_any_name(self):
#         return self.name
#     def sum_sales(self):
#         return self.sales_1 * self.sales_2
#     def analysis_discount(self):
#         self.sales_1 = self.sales_1 * Item.pay_rate
#
#
#
# item_1 = Item(2554966,"Mamun",58,500)
# item_1.analysis_discount()
# print(item_1.sales_1)
# print(f"The Customer ID: {item_1.set_customer_id()}\n"
#       f"The name will be: {item_1.set_any_name()}\n"
#       f"The total Sales will be: {item_1.sum_sales()}")
# print(item_1.sales_1)
# print(item_1.sales_2)


# class Item:
#     pay_rate = 0.83
#     all = []
#     def __init__(self,customer_id,name,sales_1:int, sales_2:int):
#         assert sales_1 >= 0, f"Sales_1{sales_1} is  greater than or equal to zero"
#         assert sales_1 >= 0, f"Sales_1{sales_2} is  greater than or equal to zero"
#         self.customer_id = customer_id
#         self.name = name
#         self.sales_1 = sales_1
#         self.sales_2 = sales_2
#         Item.all.append(self)
#
#     def set_customer_id(self):
#         return self.customer_id
#     def set_any_name(self):
#         return self.name
#     def sum_sales(self):
#         return self.sales_1 * self.sales_2
#     def analysis_discount(self):
#         return self.sales_1 * self.pay_rate
#     def __repr__(self):
#         return f"Item('{self.customer_id}','{self.name}','{self.sales_1}',{self.sales_2}')"
#
# item_1 = Item(2554966,"Mamun",58,500)
# item_2 = Item(2554966,"Mamun",100,500)
# item_3 = Item(25549,"Mamun",100,18)
# item_1.pay_rate = 0.45  ############### Self
# item_1.sales_2 = 1000
# item_1.analysis_discount()
# print(item_1.analysis_discount())
# print(f"The Customer ID: {item_1.set_customer_id()}\n"
#       f"The name will be: {item_1.set_any_name()}\n"
#       f"The total Sales will be: {item_1.sum_sales()}")
# print(item_1.sales_1)
# print(item_1.sales_2)
# print(Item.all)
# for instances in Item.all:
#     print(instances.name)