def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"
    

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser" 
    else:
        return "Equal"
    

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total_sum = 0
    max_number = numbers[0]
    min_number = numbers[0]

    for number in numbers:
        total_sum += number
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    result = (total_sum, max_number, min_number)
    return result

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """

    students = []
    for student in students_dict:
        # assume student as the key of students_dict
        if students_dict[student] > 80:
            students.append(student)         
    return students

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements = set()
    for element in list1:
        if element in list2:
            common_elements.add(element)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    arithmetic = {}
    arithmetic["sum"] = a + b
    arithmetic["difference"] = a - b
    arithmetic["product"] = a * b
    if b != 0:
        arithmetic["quotient"] = a / b
    else:
        arithmetic["quotient"] = False
    
    return arithmetic

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    results = {}
    results["and"] = x and y
    results["or"] = x or y
    results["not_x"] = not x

    return results



def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    results = {}
    results["and"] = a & b
    results["or"] = a | b
    results["xor"] = a ^ b 

    return results