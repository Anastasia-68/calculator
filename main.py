print("--- Простой калькулятор ---")

try:
    num1 = float(input("Введите первое число: "))
    operation = input("Введите действие (+, -, *, /): ").strip()
    num2 = float(input("Введите второе число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
            exit()
        result = num1 / num2
    else:
        print("Ошибка: Неизвестная операция!")
        exit()

    # Красивый вывод (преобразование 15.0 в 15)
    if result.is_integer():
        result = int(result)

    print(f"Результат: {result}")

except ValueError:
    print("Ошибка: Пожалуйста, вводите только числа!")