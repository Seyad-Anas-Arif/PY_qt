import sys
import gpiod
from gpiod.line import Direction, Value
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_st1 import Ui_MainWindow  # Import the generated UI code

LINE = 2

class LEDControlApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button signals to slots
        self.ui.button_on.clicked.connect(self.turn_on_led)
        self.ui.button_off.clicked.connect(self.turn_off_led)

        # Initialize GPIO
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

    def closeEvent(self, event):
        if self.gpio_request:
            self.gpio_request.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LEDControlApp()
    window.show()
    sys.exit(app.exec_())

