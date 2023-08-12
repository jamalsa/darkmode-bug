import sys
from PySide6.QtCore import QObject, QThread, Slot
from PySide6.QtWidgets import QApplication
from qfluentwidgets import SplitFluentWindow, setTheme, Theme
import darkdetect

class Window(SplitFluentWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Dark Mode")
        self.titleBar.raise_()

class ThemeThread(QThread):

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

    @Slot()
    def run(self):
        print('Start theme thread')
        darkdetect.listener(self.callback)

    def callback(self, mode: str):
        print('Callback with mode: ', mode)
        if mode == "Light":
            setTheme(Theme.LIGHT)
        else:
            setTheme(Theme.DARK)

if __name__ == '__main__':
    if darkdetect.isDark():
        setTheme(Theme.DARK)
    else:
        setTheme(Theme.LIGHT)

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    t = ThemeThread(window)
    t.start()

    app.exec()
    t.terminate()