##define a class about worker
class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)
        return self.pay

##use the class to do somethings
bob = Worker('Bob Smith',50000)
sue = Worker('Sue Jones',60000)
print(bob.lastName())
print(sue.lastName())
print(sue.giveRaise(.10))
print(sue.pay)
