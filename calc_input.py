from cheks import menu_check, digit_check
import logger as log


def menu_inp(val: str) -> int:
   
    """ Меню верхнего уровня """
    res = ' '
    while res not in val:                           #
        res = menu_check(input('Введите выбор: '))
    else:
        return int(res)


def real_inp():
    a = input(f"Введите рациональное число: ")  
    log.write_log(f", input: {a}")  
    a = digit_check(a)
    if a % 1 == 0:
        a = int(a)
    return a


def complex_inp() -> complex:
    print()
    temp1_comp = input(
        f"Введите действительную часть комплексного числа: ")  
    log.write_log(f", input: {temp1_comp}")  
    temp1_comp = digit_check(temp1_comp)
    temp2_comp = input(f"Введите действительную часть комплексного числа: ")
    log.write_log(f", input: {temp2_comp}")
    temp2_comp = digit_check(temp2_comp)

    return complex(temp1_comp, temp2_comp)
