class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'<Employee: {self.name}, {self.salary}>'

    def raise_salary(self, percent):
        self.salary = int(self.salary + self.salary * percent)

    def work(self):
        print(self.name, 'does something')

class Chef(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def work(self):
        print(self.name, 'cooking foods')

if __name__ == '__main__':
    bob = Employee('bob', 60000)
    print(bob)
    bob.raise_salary(0.5)
    print(bob)
    sara = Chef('Sara', 60000)
    print(sara)
    sara.work()


