def reverse_string(string):
    """
    Reverse the given string

    :param string: String to be reversed
    :return: Reversed string
    """

    string_size = len(string)
    reversed_string = [None] * string_size

    # Char delimiters
    i = 0

    while string_size > 0:
        reversed_string[i] = string[string_size - 1]
        string_size -= 1
        i += 1

    return "".join(reversed_string)


if __name__ == '__main__':
    word = input("Informe uma palavra: ")

    reversed_word = reverse_string(word)

    print("O reverso é:", reversed_word)
