def fibonacci(number, previous_value=0, current_value=1):
    """
    Checks if the number is present in the Fibonnaci sequence

    :param previous_value: Previous value of the Fibonnaci sequence
    :param current_value: Current value of the Fibonnaci sequence
    :param number: Number to be found
    :return: True if the number is present, else False
    """

    if number == 0 or number == 1:
        return True

    if current_value == number:  # Found the number
        return True
    elif current_value > number:   # Number not found
        return False
    else:
        return fibonacci(number, current_value, current_value + previous_value)


if __name__ == '__main__':
    if fibonacci(int(input("Informe um número: "))):
        print("Esse número pertence a sequência de Fibonacci !!\n")
    else:
        print("Esse número não pertence a sequência de Fibonnaci !!\n")
