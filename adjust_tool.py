

def adjust_tool_buttons(self=None):
    '''
    Функция отвечает за соединение сигналов и слотов для кнопок переключения между модулями,
    а также настройки внешнего вида кнопок

    '''
    # Кнопка перехода на виджет настройки рабочего пространства (вкладка настройки или Adjustments)
    self.toolButton_1.clicked.connect(self.toolButton_verticalwell_pageClick)

    # Кнопка перехода на виджет управления импортом данных
    self.toolButton_2.clicked.connect(self.toolButton_horizontal_pageClick)

    # Кнопка перехода на виджет построения графиков
    self.toolButton_3.clicked.connect(self.toolButton_graphics_pageClick)