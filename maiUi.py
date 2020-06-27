# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 119, 941, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("vertical_well_rate_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 941, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        #   Vertical well label
        hboxforvertbiglabel = QtWidgets.QHBoxLayout()
        self.biglabel1 = QtWidgets.QLabel(" Вертикальная скважина ")  # initializing of QLabel
        self.biglabel1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.biglabel1.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        hboxforvertbiglabel.addWidget(self.biglabel1)  # for horizontal position of label
        self.verticalLayout.addLayout(hboxforvertbiglabel)

        # Initial data Label
        hboxforfirstbiglabel = QtWidgets.QHBoxLayout()
        self.biglabel1 = QtWidgets.QLabel(" Исходные данные: ")  # initializing of QLabel
        self.biglabel1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.biglabel1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        hboxforfirstbiglabel.addWidget(self.biglabel1)  # for horizontal position of label
        self.verticalLayout.addLayout(hboxforfirstbiglabel)

        # -------------------------------------#-------------------------------------
        # Positioning of QLineEdit and QLabel order by order for each parameters
        # Initializing Oil formation volume factor
        hbox = QtWidgets.QHBoxLayout()
        self.lbl1 = QtWidgets.QLabel("Объемный фактор, м^3/м^3 = ")  # initializing of QLabel
        self.lbl1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        hbox.addWidget(self.lbl1)  # for horizontal position of label
        self.qle1 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle1.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle1.setMaximumSize(122, 20)
        hbox.addWidget(self.qle1)  # for horizontal position QLineEdit


        # Initializing kh, Horizontal permeability
        self.lbl2 = QtWidgets.QLabel("Kh, мД = ")  # initializing of QLabel
        self.lbl2.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        hbox.addWidget(self.lbl2)  # for horizontal position of label
        self.qle2 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle2.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle2.setMaximumSize(122, 20)
        hbox.addWidget(self.qle2)  # for horizontal position QLineEdit
        self.verticalLayout.addLayout(hbox)

        # Initializing Kv, Vertical permeability
        self.lbl3 = QtWidgets.QLabel("Kv, мД = ")  # initializing of QLabel
        self.lbl3.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        hbox.addWidget(self.lbl3)  # for horizontal position of label
        self.qle3 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle3.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle3.setMaximumSize(122, 20)
        hbox.addWidget(self.qle3)  # for horizontal position QLineEdit
        self.verticalLayout.addLayout(hbox)

        # Initializing h, height of oil column
        h2box = QtWidgets.QHBoxLayout()
        self.lbl4 = QtWidgets.QLabel("h, м = ")  # initializing of QLabel
        self.lbl4.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h2box.addWidget(self.lbl4)  # for horizontal position of label
        self.qle4 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle4.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle4.setMaximumSize(122, 20)
        h2box.addWidget(self.qle4)  # for horizontal position QLineEdit

        # Initializing viscosity of oil
        self.lbl5 = QtWidgets.QLabel("Вязкость, сП = ")  # initializing of QLabel
        self.lbl5.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h2box.addWidget(self.lbl5)  # for horizontal position of label
        self.qle5 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle5.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle5.setMaximumSize(122, 20)
        h2box.addWidget(self.qle5)  # for horizontal position QLineEdit

        # Initializing density of water
        self.lbl6 = QtWidgets.QLabel("Плотность воды, гр/см^3 = ")  # initializing of QLabel
        self.lbl6.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h2box.addWidget(self.lbl6)  # for horizontal position of label
        self.qle6 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle6.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle6.setMaximumSize(122, 20)
        h2box.addWidget(self.qle6)  # for horizontal position QLineEdit
        self.verticalLayout.addLayout(h2box)  # verticalize of line with 2 objects

        # Initializing density of oil
        h3box = QtWidgets.QHBoxLayout()
        self.lbl7 = QtWidgets.QLabel("Плотность нефти, гр/см^3 = ")  # initializing of QLabel
        self.lbl7.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h3box.addWidget(self.lbl7)  # for horizontal position of label
        self.qle7 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle7.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle7.setMaximumSize(122, 20)
        h3box.addWidget(self.qle7)  # for horizontal position QLineEdit

        # Initializing drainage radius
        self.lbl8 = QtWidgets.QLabel("Радиус дренирования, м = ")  # initializing of QLabel
        self.lbl8.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h3box.addWidget(self.lbl8)  # for horizontal position of label
        self.qle8 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle8.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle8.setMaximumSize(122, 20)
        h3box.addWidget(self.qle8)  # for horizontal position QLineEdit

        # Initializing thickness of perforated interval
        self.lbl11 = QtWidgets.QLabel("Высота интервала перф. hp, м = ")  # initializing of QLabel
        self.lbl11.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h3box.addWidget(self.lbl11)  # for horizontal position of label
        self.qle11 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle11.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle11.setMaximumSize(122, 20)
        h3box.addWidget(self.qle11)  # for horizontal position QLineEdit
        self.verticalLayout.addLayout(h3box)  # verticalize of line with 2 objects

        h4box = QtWidgets.QHBoxLayout()
        # Initializing wellbore radius
        self.lbl17 = QtWidgets.QLabel("-------------------------------------------------------------------")
        h4box.addWidget(self.lbl17)
        self.lbl12 = QtWidgets.QLabel("Радиус скважины rw, м = ")  # initializing of QLabel
        #self.lbl12.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        h4box.addWidget(self.lbl12)  # for horizontal position of label
        self.qle12 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.qle12.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.qle12.setMaximumSize(122, 20)
        h4box.addWidget(self.qle12)  # for horizontal position QLineEdit

        self.lbl18 = QtWidgets.QLabel("-------------------------------------------------------------------")
        h4box.addWidget(self.lbl18)
        self.verticalLayout.addLayout(h4box)  # verticalize of line with 2 objects

        # Button for calculating
        h5box = QtWidgets.QHBoxLayout()

        self.toolButton_4 = QtWidgets.QToolButton()
        self.toolButton_4.pressed.connect(self.myfunction)
        self.toolButton_4.setMaximumSize(100, 50)
        self.toolButton_4.clicked.connect(self.prepare_item_for_table)
        h5box.addWidget(self.toolButton_4)
        self.verticalLayout.addLayout(h5box)
        # -------------------------------------#-------------------------------------

        # QLabel for Results
        hboxforsecondbiglabel = QtWidgets.QHBoxLayout()
        self.biglabel2 = QtWidgets.QLabel(" Результаты: ")  # initializing of QLabel
        self.biglabel2.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.biglabel2.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        hboxforsecondbiglabel.addWidget(self.biglabel2)  # for horizontal position of label
        self.verticalLayout.addLayout(hboxforsecondbiglabel)

        # -------------------------------------##-------------------------------------
        # Spinbox1 for showing results of calculation
        vresultsbox = QtWidgets.QVBoxLayout()
        hresultsbox = QtWidgets.QHBoxLayout()
        self.lbl13 = QtWidgets.QLabel("Метод Chaperon ")  # initializing of QLabel
        self.lbl13.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.lbl13.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        vresultsbox.addWidget(self.lbl13)

        self.lbl18 = QtWidgets.QLabel("Qкр, м^3/сут = ")  # initializing of QLabel
        self.lbl18.setAlignment(QtCore.Qt.AlignVCenter)
        hresultsbox.addWidget(self.lbl18)
        self.sbox1 = QtWidgets.QDoubleSpinBox() #Spinbox for chaperon
        self.sbox1.setRange(0, 9999999)
        self.sbox1.setFont(QtGui.QFont("Times", 12))
        self.sbox1.setAlignment(QtCore.Qt.AlignHCenter)
        vresultsbox.addWidget(self.sbox1)
        hresultsbox.addLayout(vresultsbox)

        # Spinbox2 for showing results of calculation
        vresultsbox2 = QtWidgets.QVBoxLayout()
        self.lbl14 = QtWidgets.QLabel("Метод Meyer, Gardner: ")  # initializing of QLabel
        self.lbl14.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.lbl14.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        vresultsbox2.addWidget(self.lbl14)

        self.sbox2 = QtWidgets.QDoubleSpinBox()  # Spinbox for meyergardner
        self.sbox2.setRange(0, 9999999)
        self.sbox2.setFont(QtGui.QFont("Times", 12))
        self.sbox2.setAlignment(QtCore.Qt.AlignHCenter)
        vresultsbox2.addWidget(self.sbox2)
        hresultsbox.addLayout(vresultsbox2)

        # Spinbox3 for showing results of calculation
        vresultsbox3 = QtWidgets.QVBoxLayout()
        self.lbl15 = QtWidgets.QLabel("Метод Schols: ")  # initializing of QLabel
        self.lbl15.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.lbl15.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        vresultsbox3.addWidget(self.lbl15)

        self.sbox3 = QtWidgets.QDoubleSpinBox()  # Spinbox for Schols
        self.sbox3.setRange(0, 9999999)
        self.sbox3.setFont(QtGui.QFont("Times", 12))
        self.sbox3.setAlignment(QtCore.Qt.AlignHCenter)
        vresultsbox3.addWidget(self.sbox3)
        hresultsbox.addLayout(vresultsbox3)

        # Spinbox4 for showing results of calculation
        vresultsbox4 = QtWidgets.QVBoxLayout()
        self.lbl16 = QtWidgets.QLabel("Метод Hoyland: ")  # initializing of QLabel
        self.lbl16.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.lbl16.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        vresultsbox4.addWidget(self.lbl16)

        self.sbox4 = QtWidgets.QDoubleSpinBox()  # Spinbox for Hoyland
        self.sbox4.setRange(0, 9999999)
        self.sbox4.setAlignment(QtCore.Qt.AlignHCenter)
        self.sbox4.setFont(QtGui.QFont("Times", 12))
        vresultsbox4.addWidget(self.sbox4)
        hresultsbox.addLayout(vresultsbox4)
        self.verticalLayout.addLayout(hresultsbox)

        #Adding buttons for adding results to table
        haddingbox = QtWidgets.QHBoxLayout()
        self.btn_table1 = QtWidgets.QPushButton("Добавить в таблицу")
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(120, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        haddingbox.addItem(spacerItem_adding_to_table)

        self.btn_table1.setMaximumSize(120, 40)
        haddingbox.addWidget(self.btn_table1)
        self.btn_table1.pressed.connect(self.myfunction)
        self.btn_table1.pressed.connect(self.prepare_item_for_table)
        self.btn_table1.pressed.connect(self.add_item_chaperon)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        haddingbox.addItem(spacerItem_adding_to_table)

        self.btn_table2 = QtWidgets.QPushButton("Добавить в таблицу")
        self.btn_table2.setMaximumSize(120, 40)
        haddingbox.addWidget(self.btn_table2)
        self.btn_table2.pressed.connect(self.myfunction)
        self.btn_table2.pressed.connect(self.prepare_item_for_table)
        self.btn_table2.pressed.connect(self.add_item_meyer)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        haddingbox.addItem(spacerItem_adding_to_table)

        self.btn_table3 = QtWidgets.QPushButton("Добавить в таблицу")
        self.btn_table3.setMaximumSize(120, 40)
        haddingbox.addWidget(self.btn_table3)
        self.btn_table3.pressed.connect(self.myfunction)
        self.btn_table3.pressed.connect(self.prepare_item_for_table)
        self.btn_table3.pressed.connect(self.add_item_schols)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        haddingbox.addItem(spacerItem_adding_to_table)

        self.btn_table4 = QtWidgets.QPushButton("Добавить в таблицу")
        self.btn_table4.setMaximumSize(120, 40)
        haddingbox.addWidget(self.btn_table4)
        self.btn_table4.pressed.connect(self.myfunction)
        self.btn_table4.pressed.connect(self.prepare_item_for_table)
        self.btn_table4.pressed.connect(self.add_item_hoyland)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        haddingbox.addItem(spacerItem_adding_to_table)
        self.verticalLayout.addLayout(haddingbox)
        #-------------------------------------##-------------------------------------



        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("horizontal_well_rate_page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 941, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)

        #   Horizontal well page
        #==============================================================================================================

        #   Horizontal well label
        hboxforhorbiglabel = QtWidgets.QHBoxLayout()
        self.hbiglabel1 = QtWidgets.QLabel(" Горизонтальная скважина ")  # initializing of QLabel
        self.hbiglabel1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.hbiglabel1.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        hboxforhorbiglabel.addWidget(self.hbiglabel1)  # for horizontal position of label
        self.verticalLayout_2.addLayout(hboxforhorbiglabel)

        # Initial data Label
        horhboxforfirstbiglabel = QtWidgets.QHBoxLayout()
        self.horbiglabel1 = QtWidgets.QLabel(" Исходные данные: ")  # initializing of QLabel
        self.horbiglabel1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.horbiglabel1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        horhboxforfirstbiglabel.addWidget(self.hbiglabel1)  # for horizontal position of label
        self.verticalLayout_2.addLayout(horhboxforfirstbiglabel)

        # -------------------------------------#-------------------------------------
        # Positioning of QLineEdit and QLabel order by order for each parameters
        # Initializing Oil formation volume factor
        horhbox = QtWidgets.QHBoxLayout()
        self.horlbl1 = QtWidgets.QLabel("Объемный фактор, м^3/м^3 = ")  # initializing of QLabel
        self.horlbl1.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horhbox.addWidget(self.horlbl1)  # for horizontal position of label
        self.horqle1 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle1.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle1.setMaximumSize(122, 20)
        horhbox.addWidget(self.horqle1)  # for horizontal position QLineEdit


        # Initializing kh, Horizontal permeability
        self.horlbl2 = QtWidgets.QLabel("Kh, мД = ")  # initializing of QLabel
        self.horlbl2.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horhbox.addWidget(self.horlbl2)  # for horizontal position of label
        self.horqle2 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle2.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle2.setMaximumSize(122, 20)
        horhbox.addWidget(self.horqle2)  # for horizontal position QLineEdit
        self.verticalLayout_2.addLayout(horhbox)

        # Initializing Kv, Vertical permeability
        self.horlbl3 = QtWidgets.QLabel("Kv, мД = ")  # initializing of QLabel
        self.horlbl3.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horhbox.addWidget(self.horlbl3)  # for horizontal position of label
        self.horqle3 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle3.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle3.setMaximumSize(122, 20)
        horhbox.addWidget(self.horqle3)  # for horizontal position QLineEdit
        self.verticalLayout_2.addLayout(horhbox)

        # Initializing h, height of oil column
        horh2box = QtWidgets.QHBoxLayout()
        self.horlbl4 = QtWidgets.QLabel("h, м = ")  # initializing of QLabel
        self.horlbl4.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh2box.addWidget(self.horlbl4)  # for horizontal position of label
        self.horqle4 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle4.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle4.setMaximumSize(122, 20)
        horh2box.addWidget(self.horqle4)  # for horizontal position QLineEdit

        # Initializing viscosity of oil
        self.horlbl5 = QtWidgets.QLabel("Вязкость, сП = ")  # initializing of QLabel
        self.horlbl5.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh2box.addWidget(self.horlbl5)  # for horizontal position of label
        self.horqle5 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle5.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle5.setMaximumSize(122, 20)
        horh2box.addWidget(self.horqle5)  # for horizontal position QLineEdit

        # Initializing density of water
        self.horlbl6 = QtWidgets.QLabel("Плотность воды, гр/см^3 = ")  # initializing of QLabel
        self.horlbl6.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh2box.addWidget(self.horlbl6)  # for horizontal position of label
        self.horqle6 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle6.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle6.setMaximumSize(122, 20)
        horh2box.addWidget(self.horqle6)  # for horizontal position QLineEdit
        self.verticalLayout_2.addLayout(horh2box)  # verticalize of line with 2 objects

        # Initializing density of oil
        horh3box = QtWidgets.QHBoxLayout()
        self.horlbl7 = QtWidgets.QLabel("Плотность нефти, гр/см^3 = ")  # initializing of QLabel
        self.horlbl7.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh3box.addWidget(self.horlbl7)  # for horizontal position of label
        self.horqle7 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle7.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle7.setMaximumSize(122, 20)
        horh3box.addWidget(self.horqle7)  # for horizontal position QLineEdit

        # Initializing drainage radius
        self.horlbl8 = QtWidgets.QLabel("Радиус дренирования, м = ")  # initializing of QLabel
        self.horlbl8.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh3box.addWidget(self.horlbl8)  # for horizontal position of label
        self.horqle8 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle8.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle8.setMaximumSize(122, 20)
        horh3box.addWidget(self.horqle8)  # for horizontal position QLineEdit

        # Initializing wellbore radius
        self.horlbl12 = QtWidgets.QLabel("Длина скважины L, м = ")  # initializing of QLabel
        self.horlbl12.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horh3box.addWidget(self.horlbl12)  # for horizontal position of label
        self.horqle12 = QtWidgets.QLineEdit("", self)  # initializing of QLineEdit
        self.horqle12.setPlaceholderText("Введите число: ...")  # Text in QLineEdit like tips
        self.horqle12.setMaximumSize(122, 20)
        horh3box.addWidget(self.horqle12)  # for horizontal position QLineEdit
        self.verticalLayout_2.addLayout(horh3box)  # verticalize of line with 2 objects

        # Button for calculating
        horh5box = QtWidgets.QHBoxLayout()
        self.hortoolButton_4 = QtWidgets.QToolButton()
        self.hortoolButton_4.pressed.connect(self.myfunction)
        self.hortoolButton_4.setMaximumSize(100, 50)
        self.hortoolButton_4.clicked.connect(self.prepare_item_for_table)
        horh5box.addWidget(self.hortoolButton_4)
        self.verticalLayout_2.addLayout(horh5box)
        # -------------------------------------#-------------------------------------

        # QLabel for Results
        horhboxforsecondbiglabel = QtWidgets.QHBoxLayout()
        self.horbiglabel2 = QtWidgets.QLabel(" Результаты: ")  # initializing of QLabel
        self.horbiglabel2.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        self.horbiglabel2.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        horhboxforsecondbiglabel.addWidget(self.horbiglabel2)  # for horizontal position of label
        self.verticalLayout_2.addLayout(horhboxforsecondbiglabel)

        # -------------------------------------##-------------------------------------
        # Spinbox1 for showing results of calculation
        horvresultsbox = QtWidgets.QVBoxLayout()
        horhresultsbox = QtWidgets.QHBoxLayout()
        self.horlbl13 = QtWidgets.QLabel("Метод Chaperon ")  # initializing of QLabel
        self.horlbl13.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.horlbl13.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horvresultsbox.addWidget(self.horlbl13)

        self.horlbl18 = QtWidgets.QLabel("Qкр, м^3/сут = ")  # initializing of QLabel
        self.horlbl18.setAlignment(QtCore.Qt.AlignVCenter)
        horhresultsbox.addWidget(self.horlbl18)
        self.horsbox1 = QtWidgets.QDoubleSpinBox() #Spinbox for chaperon
        self.horsbox1.setRange(0, 9999999)
        self.horsbox1.setFont(QtGui.QFont("Times", 12))
        self.horsbox1.setAlignment(QtCore.Qt.AlignHCenter)
        horvresultsbox.addWidget(self.horsbox1)
        horhresultsbox.addLayout(horvresultsbox)

        # Spinbox2 for showing results of calculation
        horvresultsbox2 = QtWidgets.QVBoxLayout()
        self.horlbl14 = QtWidgets.QLabel("Метод Efors")  # initializing of QLabel
        self.horlbl14.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.horlbl14.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horvresultsbox2.addWidget(self.horlbl14)

        self.horsbox2 = QtWidgets.QDoubleSpinBox()  # Spinbox for meyergardner
        self.horsbox2.setRange(0, 9999999)
        self.horsbox2.setFont(QtGui.QFont("Times", 12))
        self.horsbox2.setAlignment(QtCore.Qt.AlignHCenter)
        horvresultsbox2.addWidget(self.horsbox2)
        horhresultsbox.addLayout(horvresultsbox2)

        # Spinbox3 for showing results of calculation
        horvresultsbox3 = QtWidgets.QVBoxLayout()
        self.horlbl15 = QtWidgets.QLabel("Метод Giger")  # initializing of QLabel
        self.horlbl15.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.horlbl15.setAlignment(QtCore.Qt.AlignHCenter)  # horizontal aligning
        horvresultsbox3.addWidget(self.horlbl15)

        self.horsbox3 = QtWidgets.QDoubleSpinBox()  # Spinbox for Schols
        self.horsbox3.setRange(0, 9999999)
        self.horsbox3.setFont(QtGui.QFont("Times", 12))
        self.horsbox3.setAlignment(QtCore.Qt.AlignHCenter)
        horvresultsbox3.addWidget(self.horsbox3)
        horhresultsbox.addLayout(horvresultsbox3)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(100, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        horhresultsbox.addItem(spacerItem_adding_to_table)
        self.verticalLayout_2.addLayout(horhresultsbox)

        #Adding buttons for adding results to table
        horhaddingbox = QtWidgets.QHBoxLayout()
        self.horbtn_table1 = QtWidgets.QPushButton("Добавить в таблицу")
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(120, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horhaddingbox.addItem(spacerItem_adding_to_table)

        self.horbtn_table1.setMaximumSize(120, 40)
        horhaddingbox.addWidget(self.horbtn_table1)
        self.horbtn_table1.pressed.connect(self.myfunction)
        self.horbtn_table1.pressed.connect(self.prepare_item_for_table)
        self.horbtn_table1.pressed.connect(self.add_item_hor_chaperon)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        horhaddingbox.addItem(spacerItem_adding_to_table)

        self.horbtn_table2 = QtWidgets.QPushButton("Добавить в таблицу")
        self.horbtn_table2.setMaximumSize(120, 40)
        horhaddingbox.addWidget(self.horbtn_table2)
        self.horbtn_table2.pressed.connect(self.myfunction)
        self.horbtn_table2.pressed.connect(self.prepare_item_for_table)
        self.horbtn_table2.pressed.connect(self.add_item_efors)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        horhaddingbox.addItem(spacerItem_adding_to_table)

        self.horbtn_table3 = QtWidgets.QPushButton("Добавить в таблицу")
        self.horbtn_table3.setMaximumSize(120, 40)
        horhaddingbox.addWidget(self.horbtn_table3)
        self.horbtn_table3.pressed.connect(self.myfunction)
        self.horbtn_table3.pressed.connect(self.prepare_item_for_table)
        self.horbtn_table3.pressed.connect(self.add_item_giger)
        spacerItem_adding_to_table = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding,
                                                           QtWidgets.QSizePolicy.Minimum)
        horhaddingbox.addItem(spacerItem_adding_to_table)

        self.verticalLayout_2.addLayout(horhaddingbox)
        #   ============================================================================================


        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("graphics_page")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 941, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.MplWidget = QtWidgets.QWidget(self.verticalLayoutWidget_3)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout_3.addWidget(self.MplWidget)

        self.hboxforgraphicpage = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_3)
        # Buttons for plots
        self.plot_button_Q_kh = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_kh.setMaximumSize(50, 50)
        self.plot_button_Q_kh.setText('Q(kh)')
        self.plot_button_Q_kh.clicked.connect(self.plot_Q_kh_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_kh)

        self.plot_button_Q_kv = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_kv.setMaximumSize(50, 50)
        self.plot_button_Q_kv.setText('Q(kv)')
        self.plot_button_Q_kv.clicked.connect(self.plot_Q_kv_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_kv)

        self.plot_button_Q_h = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_h.setMaximumSize(50, 50)
        self.plot_button_Q_h.setText('Q(h)')
        self.plot_button_Q_h.clicked.connect(self.plot_Q_h_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_h)

        self.plot_button_Q_myu = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_myu.setMaximumSize(50, 50)
        self.plot_button_Q_myu.setText('Q(µ)')
        self.plot_button_Q_myu.clicked.connect(self.plot_Q_myu_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_myu)

        self.plot_button_Q_B = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_B.setMaximumSize(50, 50)
        self.plot_button_Q_B.setText('Q(B)')
        self.plot_button_Q_B.clicked.connect(self.plot_Q_B_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_B)

        self.plot_button_Q_row = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_row.setMaximumSize(50, 50)
        self.plot_button_Q_row.setText('Q(ρw)')
        self.plot_button_Q_row.clicked.connect(self.plot_Q_row_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_row)

        self.plot_button_Q_roo = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_roo.setMaximumSize(50, 50)
        self.plot_button_Q_roo.setText('Q(ρo)')
        self.plot_button_Q_roo.clicked.connect(self.plot_Q_roo_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_roo)

        self.plot_button_Q_re = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_re.setMaximumSize(50, 50)
        self.plot_button_Q_re.setText('Q(re)')
        self.plot_button_Q_re.clicked.connect(self.plot_Q_re_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_re)

        self.plot_button_Q_hp = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_hp.setMaximumSize(50, 50)
        self.plot_button_Q_hp.setText('Q(hp)')
        self.plot_button_Q_hp.clicked.connect(self.plot_Q_hp_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_hp)

        self.plot_button_Q_rw = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_rw.setMaximumSize(50, 50)
        self.plot_button_Q_rw.setText('Q(rw)')
        self.plot_button_Q_rw.clicked.connect(self.plot_Q_rw_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_rw)

        self.plot_button_Q_L = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_Q_L.setMaximumSize(50, 50)
        self.plot_button_Q_L.setText('Q(L)')
        self.plot_button_Q_L.clicked.connect(self.plot_Q_L_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_Q_L)

        self.plot_button_clear = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        self.plot_button_clear.setMaximumSize(100, 100)
        self.plot_button_clear.setText('Clear graph')
        self.plot_button_clear.clicked.connect(self.clear_graph_draw)
        self.hboxforgraphicpage.addWidget(self.plot_button_clear)

        self.verticalLayout_3.addLayout(self.hboxforgraphicpage)

        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 941, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_1 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Avertical.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1.setIcon(icon)
        self.toolButton_1.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_1.setObjectName("toolButton_1")
        self.horizontalLayout.addWidget(self.toolButton_1)
        self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setMouseTracking(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Ahorizon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_3 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Aicon_scatter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_3.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout.addWidget(self.toolButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 480, 941, 151))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # QTableWidget for showing answers
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.vertical_for_tablewidget_buttons = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.excel_toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.excel_toolButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excel_toolButton.setIcon(icon2)
        self.excel_toolButton.setIconSize(QtCore.QSize(40, 40))
        self.excel_toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.excel_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.excel_toolButton.setObjectName("toolButton_5")
        self.vertical_for_tablewidget_buttons.addWidget(self.excel_toolButton)

        self.clear_table_toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_table_toolButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear_table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_table_toolButton.setIcon(icon2)
        self.clear_table_toolButton.setIconSize(QtCore.QSize(40, 40))
        self.clear_table_toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.clear_table_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clear_table_toolButton.setObjectName("toolButton_6")
        self.vertical_for_tablewidget_buttons.addWidget(self.clear_table_toolButton)

        self.horizontalLayout_2.addLayout(self.vertical_for_tablewidget_buttons)


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 21))
        self.menubar.setObjectName("menubar")
        filemenu = self.menubar.addMenu('&Файл')
        exportAction = QtWidgets.QAction(QtGui.QIcon('icons/excel.png'), '&Экспорт в Excel', self)
        exportAction.setShortcut('Ctrl+S')
        exportAction.setStatusTip('Экспорт в Excel')
        exportAction.triggered.connect(self.savefile)
        filemenu.addAction(exportAction)
        exitAction = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), 'Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из программы')
        exitAction.triggered.connect(self.close)
        filemenu.addAction(exitAction)
        self.help = self.menubar.addMenu('&Помощь')
        self.helpAction = QtWidgets.QAction(QtGui.QIcon('icons/help_icon.png'), '&Помощь', self)
        self.helpAction.setStatusTip('Помощь')
        self.helpAction.triggered.connect(self.help_menu)
        self.help.addAction(self.helpAction)

        self.aboutAction = QtWidgets.QAction(QtGui.QIcon('icons/about_icon.png'), '&О программе', self)
        self.aboutAction.setStatusTip('О программе')
        self.aboutAction.triggered.connect(self.about_menu)
        self.help.addAction(self.aboutAction)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Critical oil rate by Jocund v0.1", "Critical oil rate by Jocund v0.1 Email: jasurbekodilov@gmail.com"))
        MainWindow.setWindowIcon(QtGui.QIcon('icons/coning.png'))
        MainWindow.setFixedSize(981, 680)
        self.toolButton_1.setText(_translate("MainWindow", "  Вертикальная скважина  "))
        self.toolButton_2.setText(_translate("MainWindow", " Горизонтальная скважина "))
        self.toolButton_3.setText(_translate("MainWindow", "         График         "))
        self.toolButton_4.setText(_translate("MainWindow", "Рассчитать"))
        self.hortoolButton_4.setText(_translate("MainWindow", "Рассчитать"))
        self.excel_toolButton.setText(_translate("Mainwindow", " Экспорт "))
        self.clear_table_toolButton.setText(_translate("Mainwindow", "Очистить"))

