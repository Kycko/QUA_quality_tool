from sys import exit as SYSEXIT

# надписи элементов интерфейса
# labels, labelFrames(lfr), buttons, checkBoxes, toolTips
UI = {'init':{'btn':{'closeApp'   :'❌ Закрыть'},
              'tt' :{'selectTheme':'Выбрать светлую/тёмную тему оформления.'}}}

# защита от запуска модуля
if __name__ == '__main__':
    print  ("This is module, please don't execute.")
    SYSEXIT()
