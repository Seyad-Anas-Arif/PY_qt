import sys
import gpiod
from gpiod.line import Direction, Value
from PyQt5.QtWidgets import QApplication, QWidget
from ui_st1 import Ui_Widget  # Import the generated UI code from your UI file

LINE = 2

class LEDControlApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect button signals to slots
        self.ui.start_pb.clicked.connect(self.turn_on_led)
        self.ui.stop_pb.clicked.connect(self.turn_off_led)

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

        # Resize the widget based on the display size
        self.resizeWidget()

    def resizeWidget(self):
        # Get the size of the screen
        screen = QApplication.primaryScreen()
        size = screen.size()

        # Calculate the new width and height as integers
        new_width = int(size.width() * 0.8)
        new_height = int(size.height() * 0.8)

        # Adjust the widget size based on the screen size
        self.resize(new_width, new_height)

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
