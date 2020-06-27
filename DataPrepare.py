# -*- coding: utf-8 -*-
def prepare_two_row_data(x_col_name, y_col_name, table):
    """
    Подготовка данных двух столбцов из табличного виджета QTableWidget по имени столбцов
    при возникновении ошибки функция возвращает пустой список иначе список со значениями требуемого ряда
    """
    column_one_container = []
    column_two_container = []
    x = None  # Изначально x не задан
    y = None  # Изначально y не задан
    for column in range(0, table.columnCount()): #Цикл перебор имен в шапке
        column_name = table.horizontalHeaderItem(column).text()
        if column_name == x_col_name:  # Если текст в колонке совпадает с названием требуемой колонки для переменной x
           x = column  # Присвоение номера колонки переменной x
        if column_name == y_col_name:  # Если текст в колонке совпадает с названием требуемой колонки для переменной y
           y = column  # Присвоение номера колонки переменной y
    try:
      for i in range(0, table.rowCount()):
          if table.item(i, x).text() != "":
              column_one_container.append(table.item(i, x).text()) # Перебираем ряды добовляя значения колонки с индексом x в список
              column_two_container.append(table.item(i, y).text()) # Перебираем ряды добовляя значения колонки с индексом y в список

      return column_one_container, column_two_container
    except:
      return column_one_container, column_two_container
