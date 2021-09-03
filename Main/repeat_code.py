import math

if __name__ == "__main__":
    pass


def calc_stepic_formula(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_code_into_console(browser):
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])