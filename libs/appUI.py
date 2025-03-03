from   sys import exit as SYSEXIT
import ttkbootstrap    as TBS
import globalsMain     as G

class Window(TBS.Window):   # окно программы
    # конструкторы интерфейса
    def __init__ (self,app):
        self.app = app  # для вызова функций класса Root() при нажатии кнопок
        super().__init__(title     = G.UI.app['title'],
                         themename = G.UI.app['themes'][G.config.get('main:darkTheme')],
                         size      = G.UI.app['size'],
                         minsize   = G.UI.app['size'])
        self.bindSpace()
        self.place_window_center()  # расположить в центре экрана
        # self.buildUI()
    def bindSpace(self):
        def callDefault(event):
            try:
                widget = self.nametowidget(event.widget)
                widget.invoke()
            except KeyError: self.tk.call(event.widget,'invoke')

        self.bind_class('TButton','<Key-space>',callDefault,add='+')

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
