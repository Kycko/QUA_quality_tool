from   sys          import exit as SYSEXIT
from   tkinter              import BooleanVar
import ttkbootstrap             as TBS
from   ttkbootstrap.tooltip import ToolTip
import globalsMain              as G
import strings                  as S
from   globalFuncs          import sysExit

class Window(TBS.Window):   # окно программы
    # конструкторы интерфейса
    def __init__  (self,app):
        self.app = app  # для вызова функций класса Root() при нажатии кнопок
        super().__init__(title     = G.UI.app['title'],
                         size      = G.UI.app['size'],
                         minsize   = G.UI.app['size'])
        self.setUItheme(G.config.get('main:darkTheme'))
        self.bindSpace ()
        self.place_window_center()  # расположить в центре экрана
        self.buildUI()
    def setUItheme(self,theme:bool):    # theme=true/false для выбора из G.UI.themes[]
        self.style.theme_use(G.UI.themes     [theme])
        G.UI.colors        = G.UI.themeColors[theme]
    def bindSpace (self):
        def callDefault(event):
            try:
                widget = self.nametowidget(event.widget)
                widget.invoke()
            except KeyError: self.tk.call(event.widget,'invoke')

        self.bind_class('TButton','<Key-space>',callDefault,add='+')
    def buildUI   (self,runUI=False):   # runUI = окно выбора (False) или окно выполнения (True)
        if hasattr(self,'frRoot'): self.frRoot.destroy()
        self.frRoot = TBS.Frame(self)
        self.frRoot.pack(fill='both',expand=True,padx=10,pady=10)
        self.buildFrame (('init','mainRun')[runUI],self.frRoot)
    def buildFrame(self,type:str,parent,params=None):
        # frMain = TBS.Frame либо TBS.Labelframe; in... = init...
        if   type == 'init'    : self.buildFrame('inBottom',parent) # тема и закрытие программы
        elif type == 'inBottom':
            frMain = TBS.Frame(parent)
            frMain.pack(fill='x',side='bottom',pady=5)
            self.buildFrame ('inTheme',frMain)
            TBS.Button(frMain,
                       text      = S.UI['init']['btn']['closeApp'],
                       command   = sysExit,
                       bootstyle = 'danger'
                       ).pack(side='right',padx=18)
        elif type == 'inTheme' :
            frMain = TBS.Frame(parent)
            frMain.pack  (side='left')

            for icon in G.UI.icons['theme'].values():
                TBS.Label(frMain,
                          text = icon['pic'],
                          font = G.UI.fonts['iconBig']
                          ).pack(side=icon['side'],padx=icon['padx'])
            cb = TBS.Checkbutton(frMain,
                                 variable  = BooleanVar(value=G.config.get('main:darkTheme')),
                                 command   = lambda:self.switchBoolSetting('main:darkTheme'),
                                 bootstyle = 'round-toggle')
            ToolTip(cb,text=S.UI['init']['tt']['selectTheme'])
            cb.pack(expand=True)

    # кнопки и переключатели
    def switchBoolSetting(self,param:str):
        newVal = not G.config.get(param)
        G.config.set(param,newVal)
        if param == 'main:darkTheme': self.setUItheme(newVal)

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
