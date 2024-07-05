# class Calculator:
#     def __init__(self,num1,num2=None,num3=None):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#
#     def analysis(self):
#         if self.num1 is not None and self.num2 is not None and self.num3 is not None:
#             print(self.num1*self.num2*self.num3)
#         elif self.num2 is not None and self.num3 is not None:
#             print(self.num2*self.num3)
#         else:
#             print(self.num1)
# p1 = Calculator(320,70,90)
# p2 = Calculator(320,70)
# p1.analysis()
# p2.analysis()
#
# ######################################################################
# class Calculator:
#     def analysis(self,*nums):
#        sum = 1
#        print(nums)
#        for i in nums:
#             sum = sum*i
#        print(sum)
#
# p1 = Calculator()
# p2 = Calculator()
# p1.analysis(10,20)
# p2.analysis(10,2,4,7)
# ######################################################################
# from multipledispatch import dispatch
# class Calculator:
#     @dispatch(int, int)
#     def analysis(self,num1,num2):
#         print(num1*num2)
#     @dispatch(int, int,int)
#     def analysis(self,num1,num2,num3):
#         print(num1*num2*num3)
#     @dispatch(str,str)
#     def analysis(self,num1,num2):
#         print(int(num2)/int(num1))
#
# p1 = Calculator()
# p2 = Calculator()
# p3 = Calculator()
# p1.analysis(10,20)
# p2.analysis(10,2,4)
# p3.analysis("25","50")
# ########################################################
class Student:
    def __init__(self,**info):
        if len(info) == 3:
            self.name = info['name']
            self.id = info['id']
            self.yr = info['yr']
        elif len(info) == 2:
            self.name = info['name']
            self.id = info['id']
        elif len(info) == 2:
            self.id = info['id']
            self.yr = info['yr']
        elif len(info) == 1:
            self.name = info['name']
        print("Alhamdulillah")
    def khan(self):
        return self.id * self.yr


c1 = Student(name="mamun",id=3,yr=6)
c2 = Student(name="mamun",id=3)
c3 = Student(name="mamun")
print(c1.khan())