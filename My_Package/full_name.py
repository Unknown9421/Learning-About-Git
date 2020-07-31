# Generate a formatted full name including a middle name


def get_full_name(first_name: str, last_name: str, middle_name='', greeting='Hello Master: ') -> str:
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return f'{greeting} {full_name}'




