from sys import exit as SYSEXIT

class globUI(): # импортируется в G.UI (в глобальные переменные)
    def __init__(self):
        # базовые переменные приложения
        self.app = {'version'  :  'v.004',
                    'name'     :  'QUA quality tool',
                    'shortName':  'QUAqt',
                    'sizes'    :({'lbl':'100%','size':(270,270)},
                                 {'lbl':'125%','size':(320,320)},
                                 {'lbl':'150%','size':(370,370)},
                                 {'lbl':'175%','size':(430,430)})}
        self.app   ['title'] = self.app['name']+' '+self.app['version'] # название главного окна

        # стили оформления (темы, шрифты и т. п.)
        self.themes = ('flatly',  'superhero')      # светлая/тёмная
        self.fonts  = {'iconBig':('Calibri',17)}    # только для label'ов (для кнопок всё сложнее)

        # иконки и файлы
        self.icons = {'theme':{'light':{'pic':'🔆','side':'left' ,'padx':4},
                                'dark':{'pic':'🌙','side':'right','padx':0}}}

        # цвета (разные для светлой[0] и тёмной[1] тем
        # использовать надо G.UI.colors (он перезаписывается при смене темы)
        self.themeColors = ({'blue'    :'#277CD4',   # ↓ светлая
                             'green'   :'#4AAC7F',
                             'magenta' :'#936BCC',
                             'pink'    :'#D22E9E',
                             'red'     :'#DE3923',
                             'lightRed':'#E36B4F',
                             'sand'    :'#D1A63E'},
                            {'blue'    :'#7BBCFF',   # ↓ тёмная
                             'green'   :'#8EE4BD',
                             'magenta' :'#C4ABE7',
                             'pink'    :'#FBA1DE',
                             'red'     :'#EF6C32',
                             'lightRed':'#E36F47',
                             'sand'    :'#FFE5A7'})  # аналог lightYellow

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
