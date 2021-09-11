"""
https://stepik.org/lesson/193188/step/8?unit=167629
PyTest — как пишут тесты
PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest.

Мы уже увидели, что PyTest может запускать тесты, написанные в unittest-стиле.
Перепишем наши тесты из test_abs_project.py в более простом формате, который также понимает PyTest.

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

Запустим тесты в этом файле:

pytest test_abs.py
Код тестов стал короче и читабельнее.
"""


def test_abs1():
    assert abs(-42) == 42, "Should be absoluted value of a namber"


def test_abs2():
    assert abs(-42) == -42, "Should be absoluted value of a namber"
