from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib import pyplot as plt
from DataPrepare import prepare_two_row_data


class MyMplCanavas(FigureCanvasQTAgg):
    '''
    Класс холста Qt для помещения рисунка Matplotlib
    '''
    def __init__(self, fig):
        FigureCanvasQTAgg.__init__(self, fig)
        self.setMinimumSize(200,200)


def prepare_canvas_and_toolbar(layout = None):
    '''
    Функция для инициализации рисунка Matplotlib и его размещения в виджете Qt, добавления панели навигаии
    '''
    # Подготовка рисунка и осей
    fig, axes = plot_single_empty_graph()
    # Получение экземпляра класса холста с размещенным рисунком
    canvas = MyMplCanavas(fig)
    # Добавление виджета холста с рисунком в размещение
    layout.addWidget(canvas)
    # Добавление навигационной панели с привязкой к созданному холсту с рисунком Matplotlib
    toolbar = NavigationToolbar2QT(canvas, layout.parent())
    layout.addWidget(toolbar)
    return canvas, toolbar


def plot_single_empty_graph():
    '''
    Функция для подготовки рисунка с пустыми осями и предварительного их оформления, без задания данных
    '''
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 7), dpi=85, facecolor='white', frameon=True, edgecolor='black', linewidth=1)
    fig.subplots_adjust(wspace=0.4, hspace=0.6, left=0.15, right=0.85, top=0.9, bottom=0.15)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Диаграмма', fontsize=10)
    axes.set_xlabel('X', fontsize=8)
    axes.set_ylabel('Y', fontsize=8)
    return fig, axes

def clear_graph(axes):
    # Отображаем данные и настраиваем внений вид графика
    x=0
    y=0
    axes.plot(x, y)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Диаграмма', fontsize=10)
    axes.set_xlabel('X', fontsize=8)
    axes.set_ylabel('Y', fontsize=8)
    axes.get_figure().canvas.draw()

def plot_data_Q_kh(table, axes):
    # Получаем из таблицы данные Q и kh для отображения на графике
    data_to_plot = prepare_two_row_data('kh, мД', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(kh)')
    axes.grid(True)
    axes.set_title('Qкр от горизнотальной проницаемости kh', fontsize=10)
    axes.set_xlabel('kh', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_h(table, axes):
    # Получаем из таблицы данные Q и h для отображения на графике
    data_to_plot = prepare_two_row_data('h, м', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(h)')
    axes.grid(True)
    axes.set_title('Qкр от толщины пласта h', fontsize=10)
    axes.set_xlabel('h', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()


def plot_data_Q_kv(table, axes):
    # Получаем из таблицы данные Q и kv для отображения на графике
    data_to_plot = prepare_two_row_data('kv, мД', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(kv)')
    axes.grid(True)
    axes.set_title('Qкр от вертикальной проницаемости kv', fontsize=10)
    axes.set_xlabel('kv', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_myu(table, axes):
    # Получаем из таблицы данные Q и µ для отображения на графике
    data_to_plot = prepare_two_row_data('µ, сП', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(µ)')
    axes.grid(True)
    axes.set_title('Qкр от вязкости µ', fontsize=10)
    axes.set_xlabel('µ', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()


def plot_data_Q_B(table, axes):
    # Получаем из таблицы данные Q и B для отображения на графике
    data_to_plot = prepare_two_row_data('B, м3/м3', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(B)')
    axes.grid(True)
    axes.set_title('Qкр от объемного фактора B', fontsize=10)
    axes.set_xlabel('B', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_row(table, axes):
    # Получаем из таблицы данные Q и ρw для отображения на графике
    data_to_plot = prepare_two_row_data('ρw,гр/см3', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(ρw)')
    axes.grid(True)
    axes.set_title('Qкр от плотности воды ρw', fontsize=10)
    axes.set_xlabel('ρw', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_roo(table, axes):
    # Получаем из таблицы данные Q и ρo для отображения на графике
    data_to_plot = prepare_two_row_data('ρo,гр/см3', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(ρo)')
    axes.grid(True)
    axes.set_title('Qкр от плотности воды ρo', fontsize=10)
    axes.set_xlabel('ρo', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_re(table, axes):
    # Получаем из таблицы данные Q и re для отображения на графике
    data_to_plot = prepare_two_row_data('re, м', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(re)')
    axes.grid(True)
    axes.set_title('Qкр от радиуса дренирования re', fontsize=10)
    axes.set_xlabel('re', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_hp(table, axes):
    # Получаем из таблицы данные Q и hp для отображения на графике
    data_to_plot = prepare_two_row_data('hp, м', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(hp)')
    axes.grid(True)
    axes.set_title('Qкр от высоты интервала перфорации hp', fontsize=10)
    axes.set_xlabel('hp', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_rw(table, axes):
    # Получаем из таблицы данные Q и rw для отображения на графике
    data_to_plot = prepare_two_row_data('rw, м', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(rw)')
    axes.grid(True)
    axes.set_title('Qкр от радиуса скважины rw', fontsize=10)
    axes.set_xlabel('rw', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()

def plot_data_Q_L(table, axes):
    # Получаем из таблицы данные Q и rw для отображения на графике
    data_to_plot = prepare_two_row_data('L, м', 'Q, м3/сут', table)
    x = [float(x) for x in data_to_plot[0]]
    y = [float(x) for x in data_to_plot[1]]
    # Отображаем данные и настраиваем внений вид графика
    axes.plot(x, y, 'o-', label='Qкр(L)')
    axes.grid(True)
    axes.set_title('Qкр от длины скважины L', fontsize=10)
    axes.set_xlabel('L', fontsize=10)
    axes.set_ylabel('Qкр, м^3/сут', fontsize=10)
    axes.legend(loc='best', fontsize=10)
    axes.get_figure().canvas.draw()