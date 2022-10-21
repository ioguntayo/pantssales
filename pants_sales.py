class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        discounted_price = self.price * (1 - discount)
        return discounted_price


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for pants in self.pants_sold:
            print(pants.color, pants.waist, pants.length, pants.price)

    def calculate_sales(self):
        for pants in self.pants_sold:
            self.total_sales += pants.price
            return self.total_sales

    def calculate_commission(self, commission):
        commission_paid = self.total_sales * 1 - commission


pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)
salesperson.sell_pants(pants_one)

a = salesperson.pants_sold
print(a)
print(salesperson.display_sales)