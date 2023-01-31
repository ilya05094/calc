from interface import *
from calc_input import menu_inp, real_inp, complex_inp
import model_calc as sum
import model_calc as sub
import model_calc as mult
import model_calc as div
import model_calc as pow
import model_calc as rem
import model_calc as div_
import model_calc as sqrt
import logger as log


def user_num(start: int):
    if start == 1:
        return real_inp()
    elif start == 2:
        return complex_inp()
    elif start == 0:
        exit()


def run():
    while True:
        draw_menu_start()
        in_run = menu_inp("012")
        if in_run == 1:
            log.write_log("\noperation steps: 1")
            draw_menu_real()
            in_start = menu_inp("012345678")
            operation(in_run, in_start)
        elif in_run == 2:
            log.write_log("\noperation steps: 2")
            draw_menu_complex()
            in_start = menu_inp("0123456")
            operation(in_run, in_start)
        else:
            log.write_log("\n!exit!")
            exit()


def operation_2num(tip_num: int, oper, znak):
    num1 = user_num(tip_num)
    num2 = user_num(tip_num)
    result = oper.init(num1, num2)
    log.logger(num1, znak, result, num2)
    return result


def operation_1num(tip_num: int, oper, znak):
    num1 = user_num(tip_num)
    log.write_log(f"input: {num1}, ")
    result = oper.init(num1)
    log.logger(num1, znak, result)
    return result


def operation(tip_num: int, tip_oper: int):
    if tip_oper == 1:
        log.write_log(f", 1")
        draw_result(operation_2num(tip_num, sum, "+"))
    elif tip_oper == 2:
        log.write_log(f", 2")
        draw_result(operation_2num(tip_num, sub, "-"))
    elif tip_oper == 3:
        draw_result(operation_2num(tip_num, mult, "*"))
    elif tip_oper == 4:
        log.write_log(f", 4")
        draw_result(operation_2num(tip_num, div, "/"))
    elif tip_oper == 5:
        if tip_num == 1:

            log.write_log(f", 5")
            draw_result(operation_2num(tip_num, div_, "//"))
        else:

            log.write_log(f", 5")
            draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 6:
        if tip_num == 1:

            log.write_log(f", 6")
            draw_result(operation_2num(tip_num, rem, "%"))
        else:

            log.write_log(f", 6")
            draw_result(operation_1num(tip_num, sqrt, "sqrt"))
    elif tip_oper == 7:

        log.write_log(f", 7")
        draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 8:
        log.write_log(f", 8")
        draw_result(operation_1num(tip_num, sqrt, "sqrt"))
    elif tip_oper == 0:
        log.write_log(f", 0")
        run()
