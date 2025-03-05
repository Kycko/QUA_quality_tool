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
        super().__init__(title = G.UI.app['title'])
        self.setUItheme (G.config.get('main:darkTheme'))
        self.bindSpace  ()
        self.place_window_center()  # расположить в центре экрана
        self.buildUI  ()
        self.setUIzoom()    # обязательно после buildUI() (обновляется кнопка)
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
        if   type == 'init':
            self.buildFrame('inFiles' ,parent)  # выбор файлов
            self.buildFrame('inBottom',parent)  # тема и закрытие программы
        elif type == 'inFiles':
            frMain =   TBS.Frame(parent)
            frMain.pack(fill='x',pady=5)
        elif type == 'inBottom':
            frMain = TBS.Frame(parent)
            frMain.pack(fill='x',side='bottom',pady=5)
            self.buildFrame ('inCfg',frMain)
            TBS.Button(frMain,
                       text      = S.UI['init']['btn']['closeApp'],
                       command   = sysExit,
                       bootstyle = 'danger'
                       ).pack(anchor='s',side='right',padx=18,pady=4)
        elif type == 'inCfg':
            frMain = TBS.LabelFrame(parent,text=S.UI['init']['lfr']['inCfg'])
            frMain.pack(fill='x',side='left')
            self.buildFrame ('inCfgTheme',frMain)
            self.zoomBtn = TBS.Button(frMain,
                                      command   =  lambda change=True: self.setUIzoom(change),
                                      bootstyle = 'secondary')
            self.zoomBtn.pack(padx=4,pady=4)
        elif type == 'inCfgTheme':
            frMain = TBS.Frame(parent)
            frMain.pack(anchor='w',pady=3)

            for icon in G.UI.icons['theme'].values():
                TBS.Label(frMain,
                          text = icon['pic'],
                          font = G.UI.fonts['iconBig']
                          ).pack(side=icon['side'],padx=icon['padx'])
            cb = TBS.Checkbutton(frMain,
                                 variable  = BooleanVar(value=G.config.get('main:darkTheme')),
                                 command   = lambda:self.switchBoolSetting('main:darkTheme'),
                                 bootstyle = 'round-toggle')
            ToolTip(cb,text=S.UI['init']['tt']['cfgTheme'])
            cb.pack(expand=True)

    # изменение оформления
    def setUItheme(self,theme:bool):    # theme=true/false для выбора из G.UI.themes[]
        self.style.theme_use(G.UI.themes     [theme])
        G.UI.colors        = G.UI.themeColors[theme]
    def setUIzoom (self,change=False):
        cfgName = 'main:zoom'
        sList   =  G.UI.app['sizes']
        cur     =  G.config.get(cfgName)
        if change:
            cur += 1
            if cur == len(sList): cur = 0
            G .config.set(cfgName,cur)

        self.zoomBtn.configure(text = S.UI['init']['btn']['cfgZoom'] + sList[cur]['lbl'])
        x,y = sList[cur]['size']
        self.geometry(str(x)+'x'+str(y))
        self.minsize (x,y)

    # кнопки и переключатели
    def switchBoolSetting(self,param:str):
        newVal = not G.config.get(param)
        G.config.set(param,newVal)
        if param == 'main:darkTheme': self.setUItheme(newVal)

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
