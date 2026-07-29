from langchain.tools import tool

@tool
def square_root(x: float) -> float:
    """Calculate the square root of a number"""
    return x ** 0.

@tool
def square(x: float) -> float:
    """Calculate the square of a number"""
    return x ** 2