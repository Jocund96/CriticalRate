# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QHeaderView, QFileDialog, QTextBrowser, QDialog
import xlwt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from maiUi import Ui_MainWindow
from adjust_tool import adjust_tool_buttons
from methods import *
from Graphics import *



class Program(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        adjust_tool_buttons(self=self)
        self.widgets_adjust()
        self.i = 0
        self.j = 0
        self.write_table_widget()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Уведомление', "Вы уверены, что хотите уйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            self.myfunction()

    def ed(self):

        self.B = strToFloat(self.qle1.text())
        self.kh = strToFloat(self.qle2.text())
        self.kv = strToFloat(self.qle3.text())
        self.h = strToFloat(self.qle4.text())
        self.myu = strToFloat(self.qle5.text())
        self.row = strToFloat(self.qle6.text())
        self.roo = strToFloat(self.qle7.text())
        self.re = strToFloat(self.qle8.text())
        self.hp = strToFloat(self.qle11.text())
        self.rw = strToFloat(self.qle12.text())
        #   For horizontal
        self.hB = strToFloat(self.horqle1.text())
        self.hkh = strToFloat(self.horqle2.text())
        self.hkv = strToFloat(self.horqle3.text())
        self.hh = strToFloat(self.horqle4.text())
        self.hmyu = strToFloat(self.horqle5.text())
        self.hrow = strToFloat(self.horqle6.text())
        self.hroo = strToFloat(self.horqle7.text())
        self.hre = strToFloat(self.horqle8.text())
        self.hl = strToFloat(self.horqle12.text())

    def myfunction(self):
        self.ed()
        self.ch = chaperon(self.B, self.kv, self.kh, self.h, self.myu, self.row, self.roo, self.re)      #Chaperon Method
        self.mgp = meyergardner(self.B, self.kh, self.h, self.myu, self.row, self.roo, self.re, self.hp, self.rw)    # Meyer Gardner, Pirson Method
        self.sch = schols(self.B, self.kh, self.h, self.myu, self.row, self.roo, self.re, self.hp, self.rw)  # Schols Method
        self.hoy = hoyland(self.B, self.kh, self.h, self.myu, self.row, self.roo, self.re, self.hp)  # Hoyland Method
        self.h_ch = hor_chaperon(self.hB, self.hkv, self.hkh, self.hh, self.hmyu, self.hrow, self.hroo, self.hre, self.hl)
        self.efor = hor_efors(self.hB, self.hkh, self.hh, self.hmyu, self.hrow, self.hroo, self.hre, self.hl)
        self.gig = hor_giger(self.hB, self.hkh, self.hh, self.hmyu, self.hrow, self.hroo, self.hre, self.hl)
        self.sbox1.setValue(self.ch)
        self.sbox2.setValue(self.mgp)
        self.sbox3.setValue(self.sch)
        self.sbox4.setValue(self.hoy)
        self.horsbox1.setValue(self.h_ch)
        self.horsbox2.setValue(self.efor)
        self.horsbox3.setValue(self.gig)

    def toolButton_verticalwell_pageClick(self):
        # При нажатии на кнопку виджет QStackedWidget переклюается на вкладку Vertical Well
        self.stackedWidget.setCurrentIndex(0)

    def toolButton_horizontal_pageClick(self):
        # При нажатии на кнопку виджет QStackedWidget переклюается на вкладку horizontalWell
        self.stackedWidget.setCurrentIndex(1)

    def toolButton_graphics_pageClick(self):
        # При нажатии на кнопку виджет QStackedWidget переклюается на вкладку графики
        self.stackedWidget.setCurrentIndex(2)

    def widgets_adjust(self):
        # Создание вертикального размещения в виджете QWidget
        self.companovka_for_mpl = QVBoxLayout(self.MplWidget)
        # Добавляем виджет с холстом матплотлиб для отображеня диаграммы рассеяния
        self.canvas, self.toolbar = prepare_canvas_and_toolbar(layout=self.companovka_for_mpl)
        self.excel_toolButton.clicked.connect(self.savefile)
        self.clear_table_toolButton.clicked.connect(self.clear_table)


    def prepare_item_for_table(self):
        self.chap_massive = ['Chaperon', self.ch, self.B, self.kh, self.h, self.myu, self.row,
                             self.roo, self.re, self.kv]
        self.mgp_massive = ['Meyer', self.mgp, self.B, self.kh, self.h, self.myu, self.row,
                            self.roo, self.re, self.hp, self.rw]
        self.sch_massive = ['Schols', self.sch, self.B, self.kh, self.h, self.myu, self.row,
                            self.roo, self.re, self.hp, self.rw]
        self.hoy_massive = ['Hoyland', self.hoy, self.B, self.kh, self.h, self.myu, self.row,
                            self.roo, self.re, self.hp]

        self.hchap_massive = ['H_Chaperon', self.h_ch, self.hB, self.hkh, self.hh, self.hmyu,
                              self.hrow, self.hroo, self.hre, self.hkv, self.hl]
        self.efor_massive = ['Efors', self.efor, self.hB, self.hkh, self.hh, self.hmyu,
                             self.hrow, self.hroo, self.hre, self.hl]
        self.gig_massive = ['Giger', self.gig, self.hB, self.hkh, self.hh, self.hmyu,
                            self.hrow, self.hroo, self.hre, self.hl]

    def write_table_widget(self):
        self.table = self.tableWidget
        self.table.setColumnCount(13)  # Устанавливаем 12 столбцов
        self.header = ('Методы', 'Q, м3/сут', 'B, м3/м3', 'kh, мД', 'h, м', 'µ, сП', 'ρw,гр/см3',
                       'ρo,гр/см3', 're, м', 'hp, м', 'rw, м', 'kv, мД', 'L, м')
        self.realheader = self.table.horizontalHeader()
        self.realheader.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(self.header)

    def add_item_chaperon(self):
        """
        Function for adding Chaperon method results and init data to QTableWidget
        """
        self.chap_massive_round = []
        self.chap_massive_round = [round(x, 4) for x in self.chap_massive[1:]]
        self.chap_massive_round.insert(0, self.chap_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.chap_massive_round)):
            if i in (9, 10):
                continue
            item = QTableWidgetItem(str(self.chap_massive_round[j]))

            self.tableWidget.setItem(self.numrows - 1, i, item)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            j += 1
            self.tableWidget.setItem(self.numrows - 1, 11, QTableWidgetItem(str(self.chap_massive_round[9])))

    def add_item_meyer(self):
        """
        Function for adding Meyer, Gardnet, Pirson method results and init data to QTableWidget
        """
        self.mgp_massive_round = []
        self.mgp_massive_round = [round(x, 4) for x in self.mgp_massive[1:]]
        self.mgp_massive_round.insert(0, self.mgp_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.mgp_massive_round)):
            item = QTableWidgetItem(str(self.mgp_massive_round[j]))
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            self.tableWidget.setItem(self.numrows - 1, i, item)
            j += 1

    def add_item_schols(self):
        """
        Function for adding Schols method results and init data to QTableWidget
        """
        self.sch_massive_round = []
        self.sch_massive_round = [round(x, 4) for x in self.sch_massive[1:]]
        self.sch_massive_round.insert(0, self.sch_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.sch_massive_round)):
            item = QTableWidgetItem(str(self.sch_massive_round[j]))
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            self.tableWidget.setItem(self.numrows - 1, i, item)
            j += 1

    def add_item_hoyland(self):
        """
        Function for adding Hoyland method results and init data to QTableWidget
        """
        self.hoy_massive_round = []
        self.hoy_massive_round = [round(x, 4) for x in self.hoy_massive[1:]]
        self.hoy_massive_round.insert(0, self.hoy_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.hoy_massive_round)):
            item = QTableWidgetItem(str(self.hoy_massive_round[j]))
            self.tableWidget.setItem(self.numrows - 1, i, item)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            j += 1

    def add_item_hor_chaperon(self):
        """
        Function for adding Horizontal well Chaperon method results and init data to QTableWidget
        """
        self.hchap_massive_round = []
        self.hchap_massive_round = [round(x, 4) for x in self.hchap_massive[1:]]
        self.hchap_massive_round.insert(0, self.hchap_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.hchap_massive_round)):
            if i in (9, 10):
                continue
            item = QTableWidgetItem(str(self.hchap_massive_round[j]))
            self.tableWidget.setItem(self.numrows - 1, i, item)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            j += 1
            self.tableWidget.setItem(self.numrows - 1, 11, QTableWidgetItem(str(self.hchap_massive_round[9])))
            self.tableWidget.setItem(self.numrows - 1, 12, QTableWidgetItem(str(self.hchap_massive_round[10])))

    def add_item_efors(self):
        """
        Function for adding Efors method results and init data to QTableWidget
        """
        self.efor_massive_round = []
        self.efor_massive_round = [round(x, 4) for x in self.efor_massive[1:]]
        self.efor_massive_round.insert(0, self.efor_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.efor_massive_round)):
            if i in (9, 10, 11):
                continue
            item = QTableWidgetItem(str(self.efor_massive_round[j]))
            self.tableWidget.setItem(self.numrows - 1, i, item)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            j += 1
            self.tableWidget.setItem(self.numrows - 1, 12, QTableWidgetItem(str(self.efor_massive_round[9])))

    def add_item_giger(self):
        """
        Function for adding Giger method results and init data to QTableWidget
        """
        self.gig_massive_round = []
        self.gig_massive_round = [round(x, 4) for x in self.gig_massive[1:]]
        self.gig_massive_round.insert(0, self.gig_massive[0])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.numrows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.numrows)
        j = 0
        for i in range(len(self.gig_massive_round)):
            if i in (9, 10, 11):
                continue
            item = QTableWidgetItem(str(self.gig_massive_round[j]))
            self.tableWidget.setItem(self.numrows - 1, i, item)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
            j += 1
            self.tableWidget.setItem(self.numrows - 1, 12, QTableWidgetItem(str(self.gig_massive_round[9])))

    def clear_table(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(self.header)

    def clear_graph_draw(self):
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        clear_graph(axes=axes)

    def plot_Q_kh_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_kh(table=self.table, axes=axes)

    def plot_Q_kv_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_kv(table=self.table, axes=axes)

    def plot_Q_h_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_h(table=self.table, axes=axes)

    def plot_Q_myu_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_myu(table=self.table, axes=axes)

    def plot_Q_B_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_B(table=self.table, axes=axes)

    def plot_Q_row_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_row(table=self.table, axes=axes)

    def plot_Q_roo_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_roo(table=self.table, axes=axes)

    def plot_Q_re_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_re(table=self.table, axes=axes)

    def plot_Q_hp_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_hp(table=self.table, axes=axes)

    def plot_Q_rw_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_rw(table=self.table, axes=axes)

    def plot_Q_L_draw(self):
        """
        Get axes then draw
        """
        axes = self.canvas.figure.get_children()[1]
        # Вызов методов отображения функции
        axes.cla()
        plot_data_Q_L(table=self.table, axes=axes)

    def savefile(self):
        self.qfile = QFileDialog
        fname = self.qfile.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("Результат", cell_overwrite_ok=True)
        self.add2(sheet)
        wbk.save(fname[0])

    def add2(self, sheet):
        for currentColumn in range(self.tableWidget.columnCount()):
            sheet.write(0, currentColumn, self.header[currentColumn])
            for currentRow in range(1, self.tableWidget.rowCount()+1):
                try:
                    teext = str(self.tableWidget.item(currentRow-1, currentColumn).text())
                    sheet.write(currentRow, currentColumn, teext)
                except AttributeError:
                    pass

    def about_menu(self):
        QMessageBox.about(self, self.tr('О программе'),
                            self.tr('Программа предназначена для подсчета критического безводного дебита скважин '
                                    'и для построения графиков\n'
                                        ' Email: jasurbekodilov@gmail.com '))

    def help_menu(self):
        helpDialog = QDialog(self)  # Added QTextBrowser() QDialog
        helpDialog.setAttribute(Qt.WA_DeleteOnClose)  # Added
        browser = QTextBrowser()
        browser.setMinimumSize(400, 400)
        browser.setFont(QFont("SansSerif", 12))
        browser.append('Рекомендации по использованию программы')
        browser.append('\n 1. Используйте только один из методов для построения графика.\n '
                       '2. Кнопка "Добавить таблицу" тоже рассчитывает по формулам, поэтому не обязательно '
                       'нажимать кнопку "Рассчитать", чтобы получить новые данные для добавления в таблицу. \n '
                       '3. Экспорт в Excel производится в старый формат .xls, учитывайте это при работе с файлом'
                       'в дальнейшем')
        layout = QVBoxLayout()
        layout.addWidget(browser)
        helpDialog.setLayout(layout)  # Added
        helpDialog.setWindowTitle("Critical Oil Rate by Jocund v0.1 - Help")  # Added for neatness
        helpDialog.show()  # Changed


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    pr = Program()
    pr.show()
    sys.exit(app.exec())
