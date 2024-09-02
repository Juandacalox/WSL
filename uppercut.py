#!/usr/bin/python3
def print_last_digit(number):
    """Imprime el último dígito de un número y lo devuelve."""
    last_digit = abs(number) % 10
    print (last_digit, end="")
    return last_digit

