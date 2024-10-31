class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0.00
        self.spent = 0.00

    def __str__(self):
        category_str = ''
        left_category_name = self.name[:len(self.name) // 2]
        right_category_name = self.name[len(self.name) // 2:]

        category_str += left_category_name.rjust(
            15, '*') + right_category_name.ljust(15, '*')

        for data in self.ledger:
            # print(data)
            new_line = data['description'] if len(
                data['description']) <= 23 else data['description'][:23]
            new_line += f'{data["amount"]:.2f}'.rjust(30 - len(new_line), ' ')
            category_str += '\n' + new_line

        category_str += f'\nTotal: {self.balance:.2f}'
        return str(category_str)

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.spent += amount
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.spent += amount
        self.ledger.append(
            {'amount': -amount, 'description': f'Transfer to {category.name}'})
        category.deposit(amount, f'Transfer from {self.name}')
        # print(category)
        return True

    def check_funds(self, amount):
        return False if self.balance < amount else True


def create_spend_chart(categories):
    # print('test incoming')
    if len(categories) == 0:
        return None
    # print(categories[2])
    text_to_print = 'Percentage spent by category\n'
    graph_percent = 100
    total = sum(category.spent for category in categories)
    percents = [(category.spent / total) * 100 for category in categories]
    # print(total, percents)
    for _ in range(0, 11):
        print_line = str(graph_percent).rjust(3) + '| '
        # print_line += ' o  o  o'
        for percent in percents:
            if percent >= graph_percent:
                print_line += 'o  '
            else:
                print_line += '   '
        text_to_print += print_line + '\n'
        graph_percent -= 10

    # print(len(categories) * 3)
    text_to_print += '    -'.ljust((len(categories) * 3) + 5, '-') + '\n'

    # print names
    names = [list(category.name) for category in categories]
    longest = len(max(names, key=len))
    for i in range(0, longest):
        print_line = '     '
        for name in names:
            # print(name, len(name), i)
            if len(name) >= i + 1:
                print_line += name[i] + '  '
            else:
                print_line += '   '
        text_to_print += print_line
        if i + 1 != longest:
            text_to_print += '\n'

    return text_to_print


# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# # print(food)

# auto = Category('Auto')
# auto.deposit(10, 'deposit')
# auto.withdraw(15.89, 'restaurant and more food for dessert')

# # print(clothing)
# create_spend_chart([food, clothing, auto])

# food = Category('Test')
# food.deposit(900, 'deposit')
# food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
# print(food.get_balance())

business = Category('Business')
business.deposit(900, 'deposit')
business.withdraw(10.99)
# print(business)

food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(105.55)
# print(food)

entertainment = Category('Entertainment')
entertainment.deposit(900, 'deposit')
entertainment.withdraw(33.40)

print(create_spend_chart([business, food, entertainment]))
