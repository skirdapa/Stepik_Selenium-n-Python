"""
https://stepik.org/lesson/36285/step/6?unit=162401
"""
assert abs(-42) == 42  # Здесь исключения не будет
# assert abs(-42) == -42  # Здесь будет, но неинформативное
assert abs(-42) == -42, "Should be absolute value of a number"
