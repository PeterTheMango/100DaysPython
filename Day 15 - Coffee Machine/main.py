from machine_data import MENU, resources

total_sales = 0

def CheckMoney(totalMoney, drinkCost):
    if totalMoney >= drinkCost:
        change = round(totalMoney - drinkCost, 2)
        global total_sales
        total_sales += drinkCost
        print(f"Your change is ${change}!")
    else:
        print("You do not have enough money for this drink. Please collect your money.")
        return False
    return True

def PromptUser():
    p = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while not p in ["espresso", "latte", "cappuccino", "report", "off"]:
        p = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return p

def PromptMoney(t, m):
    c = input(f"How many {t}: ").lower()
    while not c.replace('.', '', 1).isnumeric():
        print("ERROR: That is not a valid number!")
        c = input(f"How many {t}: ").lower()
    return int(c) * m

def CheckResources(drink):
    for i in drink:
        if drink[i] > resources[i]:
            print(f"We do not have enough {i} for this drink.")
            return False
    return True

def MakeCoffee(drink):
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
    print(f"Here is your {drink}. Enjoy!")

prompt = PromptUser()
while not prompt == "off":
    if prompt == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${total_sales}")
    else:
        choice = MENU[prompt]
        if CheckResources(choice["ingredients"]):
            money = PromptMoney("quarters", 0.25) + PromptMoney("dimes", 0.1) + PromptMoney("nickels", 0.05) + PromptMoney("pennies", 0.01)
            if CheckMoney(money, choice["cost"]):
                MakeCoffee(prompt)
    prompt = PromptUser()
