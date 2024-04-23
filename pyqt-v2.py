# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import Qt
#from PySide6.QtWidgets import QApplication, QWidget, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from form import *
#from ui_form import Ui_Pushbuttons
LINE=2
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.stat_pb.clicked.connect(turn_off_led)
        self.stop_pb.clicked.connect(turn_on_led)



        self.gpio_request = gpiod.request_lines(
                   "/dev/gpiochip0",
                   consumer="led-control",
                   config={
                       LINE: gpiod.LineSettings(
                           direction=Direction.OUTPUT, output_value=Value.INACTIVE
                       )
                   },
               )

                 def turn_on_led(self):
                     if self.gpio_request:
                         self.gpio_request.set_value(LINE, Value.ACTIVE)

                 def turn_off_led(self):
                     if self.gpio_request:
                         self.gpio_request.set_value(LINE, Value.INACTIVE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

