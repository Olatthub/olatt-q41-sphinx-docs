def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First factor.
    b : float
        Second factor.

    Returns
    -------
    float
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide one number by another.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator. Must not be zero.

    Returns
    -------
    float
        The result of a / b.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator must not be zero.")
    return a / b
