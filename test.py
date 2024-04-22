from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import time
import gpiod

from gpiod.line import Direction, Value
LINE = 2 

with gpiod.request_lines(
    "/dev/gpiochip0",
    consumer="blink-example",
    config={
	LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )
    },
) as request:

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LED Controller")
        self.setGeometry(100, 100, 300, 200)

        # Assuming the LED is connected to GPIO pin 50
      #  self.led_gpio = 50

        # Export the GPIO pin
       # os.system("echo {} > /sys/class/gpio/export".format(self.led_gpio))
       # os.system("echo out > /sys/class/gpio/gpio{}/direction".format(self.led_gpio))

        self.button_on = QPushButton("ON", self)
        self.button_on.setGeometry(50, 50, 100, 50)
        self.button_on.clicked.connect(self.turn_on_led)

        self.button_off = QPushButton("OFF", self)
        self.button_off.setGeometry(160, 50, 100, 50)
        self.button_off.clicked.connect(self.turn_off_led)

    def turn_on_led(self):
        request.set_value(LINE, Value.ACTIVE)
        # Turn on the LED
       # os.system("echo 1 > /sys/class/gpio/gpio{}/value".format(self.led_gpio))
       

    def turn_off_led(self):
    	 request.set_value(LINE, Value.INACTIVE)
        # Turn off the LED
        #os.system("echo 0 > /sys/class/gpio/gpio{}/value".format(self.led_gpio))

    def closeEvent(self, event):
        # Cleanup GPIO on window close
       # os.system("echo {} > /sys/class/gpio/unexport".format(self.led_gpio))
       # event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


