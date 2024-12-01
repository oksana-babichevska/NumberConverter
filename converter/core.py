def convert_to_binary(number: int) -> str:
    return bin(number)[2:]

def convert_to_octal(number: int) -> str:
    return oct(number)[2:]

def convert_to_decimal(number: str, base: int) -> int:
    return int(number, base)

def convert_to_hexadecimal(number: int) -> str:
    return hex(number)[2:].upper()
