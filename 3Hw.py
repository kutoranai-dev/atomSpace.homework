while True:
    user_number1 = input("Введіть перше число (q для виходу): ")
    if user_number1 == "q":
        print("Кінець програми")
        break

    user_number2 = input("Введіть друге число: ")
    user_operation = input("Введіть операцію: ")

    user_number1 = float(user_number1)
    user_number2 = float(user_number2)

    if user_operation == "+":
        print("результат:", user_number1 + user_number2)
    elif user_operation == "-":
        print("результат:", user_number1 - user_number2)
    elif user_operation == "*":
        print("результат:", user_number1 * user_number2)
    elif user_operation == "/":
        print("результат:", user_number1 / user_number2)
    elif user_operation == "**":
        print("результат:", user_number1 ** user_number2)
    else:
        print("невірна операція")

#task 2
balance = float(input("Введіть початковий баланс: "))
expenses_by_category = {}

while True:
    category_name = input("Введіть категорію (або 'вихід'): ").lower()
    
    if category_name == "вихід":
        print("Кінець програми")
        break

    expense_amount = float(input("Введіть суму витрат: "))

    if balance - expense_amount < 0:
        print("Помилка: недостатньо коштів!")
        continue

    balance = balance - expense_amount

    if category_name in expenses_by_category:
        expenses_by_category[category_name] = expenses_by_category[category_name] + expense_amount
    else:
        expenses_by_category[category_name] = expense_amount

    print("Залишок:", balance)
    print("Витрати:", expenses_by_category)
