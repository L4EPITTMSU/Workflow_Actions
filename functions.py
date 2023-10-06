def area_of_rectangle(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return width*height

def perimeter_of_rectangle(width: float, height: float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return (width + height)*2

def my_adder(a: float, b: float, c: float) -> float:
    """
    Sum three numbers.

    Args:
        a (float): First number.
        b (float): Second number.
        c (float): Third number.

    Returns:
        float: The sum of a, b, and c.

    """
    return a + b + c

def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """
    Change the status of the thermostat based on temperature and desired temperature.

    Args:
        temp (int): Current temperature.
        desired_temp (int): Desired temperature.

    Returns:
        str: The status of the thermostat ('Heat', 'AC', or 'off').
    """
    if temp < desired_temp - 5:
        return 'Heat'
    elif temp > desired_temp + 5:
        return 'AC'
    else:
        return 'off'

def have_digits(s: str) -> int:
    """
    Check if a string has digits in it.

    Args:
        s (str): The string to check.

    Returns:
        int: 1 if the string has digits, 0 otherwise.
    """
    for c in s:
        if c.isdigit():
            return 1
    return 0
