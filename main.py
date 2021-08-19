class Machine:
    menu = ['espresso', 'latte', 'cappuccino']
    count = {
        'espresso': [250, 0, 16, 1],
        'latte': [350, 75, 20, 1],
        'cappuccino': [200, 100, 12, 1]
    }

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def get(self):
        print('\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money\n'.format(self.water, self.milk, self.coffee, self.cups, self.money))

    def set(self, count_water=0, count_milk=0, count_coffee=0, count_cups=0, count_money=0):
        self.water += count_water
        self.milk += count_milk
        self.coffee += count_coffee
        self.cups += count_cups
        self.money += count_money

    def choosing_action(self):
        choose = input('Write action (buy, fill, take, remaining, exit):\n')
        if choose == 'take':
            self.take()
        elif choose == 'fill':
            self.fill()
        elif choose == 'buy':
            self.buy()
        elif choose == 'remaining':
            self.get()
        elif choose == 'exit':
            exit()

    def take(self):
        print(f'\nI gave you ${self.money}\n')
        self.set(count_money=-self.money)

    def fill(self):
        fill_water = int(input('Write how many ml of water do you want to add:\n'))
        fill_milk = int(input('Write how many ml of milk do you want to add:\n'))
        fill_coffee = int(input('Write how many grams of coffee beans do you want to add:\n'))
        fill_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        print('')
        self.set(count_water=fill_water, count_milk=fill_milk, count_coffee=fill_coffee, count_cups=fill_cups)

    def buy(self):
        client_coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if client_coffee == '1':
            if self.check(int(client_coffee)):
                self.espresso()
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Sorry, not enough water!\n')
        if client_coffee == '2':
            if self.check(int(client_coffee)):
                self.latte()
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Sorry, not enough water!\n')
        if client_coffee == '3':
            if self.check(int(client_coffee)):
                self.cappuccino()
                print('I have enough resources, making you a coffee!\n')
            else:
                print('Sorry, not enough water!\n')
        if client_coffee == 'back':
            pass

    def check(self, coffee):
        a = True
        check_list = [self.water, self.milk, self.coffee, self.cups]
        for i in range(4):
            if self.count[self.menu[coffee - 1]][i] > check_list[i]:
                a = False
        return a

    def espresso(self):
        self.set(count_water=-250, count_coffee=-16, count_cups=-1, count_money=4)

    def latte(self):
        self.set(count_water=-350, count_milk=-75, count_coffee=-20, count_cups=-1, count_money=7)

    def cappuccino(self):
        self.set(count_water=-200, count_milk=-100, count_coffee=-12, count_cups=-1, count_money=6)


coffee_machine = Machine(400, 540, 120, 9, 550)
while True:
    coffee_machine.choosing_action()
