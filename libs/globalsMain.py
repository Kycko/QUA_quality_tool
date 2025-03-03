from sys          import exit as SYSEXIT
from userSettings import userCfg
from globalsUI    import globUI

# глобальные переменные интерфейса (UI)
UI = globUI()

# файлы
files = {'config':UI.app['shortName']+'.config'}

# настройки
config = userCfg(files['config'])

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
