import re
from typing import Generator

def generator_numbers(input: str) -> Generator[float, None, None]:
    float_regex = r"[-+]?\d*\.\d+|\d+"
    for number in re.finditer(float_regex, input):
        yield float(number.group())

def sum_profit(input: str, func: callable) -> float:
    profit = 0
    for number in func(input):
        profit += number
    return profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
