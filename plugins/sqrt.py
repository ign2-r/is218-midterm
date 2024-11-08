"""Square root plugin with flexible arguments."""
import math

def sqrt(a, *args):
    """Calculate square root of a number, ignoring any extra arguments."""
    return math.sqrt(a)

plugin = {
    "sqrt": sqrt
}
