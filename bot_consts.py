OPERATIONSV = {     'Cумма': lambda n1, n2: n1 + n2,
    'Разность'             : lambda n1, n2: n1 - n2,
    'Умножение'            : lambda n1, n2: n1 * n2,
    'Деление'              : lambda n1, n2: n1 / n2,
    'Целочисленное деление': lambda n1, n2: n1 // n2,
    'Деление с остатком'   : lambda n1, n2: n1 % n2,
    'Возведение в спепень' : lambda n1, n2: n1 ** n2,
    'Квадратный корень'    : lambda n1: n1 ** 0.5
}


MESSAGE_HI = 'Добро пожаловать в калькулятор\nКоманда /cancel, остановит работу.\nВыберите, с каким видом чисел мы будем работать:'
KEYS_M = [['Вещественные числа'], ['Комплексные числа']]

KEYS_1 = [['Cумма', 'Разность', 'Умножение'],
          ['Деление', 'Целочисленное деление', 'Деление с остатком'],
          ['Возведение в спепень', 'Квадратный корень'],
          ['Предыдущее меню']]

KEYS_2 = [['Cумма', 'Разность', 'Умножение'],
          ['Деление','Возведение в спепень', 'Квадратный корень'],
          ['Предыдущее меню']]

KEYS_C = [['Еще разок', 'Выход']]