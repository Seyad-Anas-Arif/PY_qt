# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import Qt
import lanc
from ui_st2 import Ui_Widget
#from form import *
#from ui_form import Ui_Pushbuttons
LINE=2
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ETC_Startup()


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
                         
	def Etc_Startup(self):
	etc_init_ok = False
        chip_id = 0
        etc_command = 0
        etc_command_value = 0.0
        etc_status_reg = 0
        received_setpoint = 0.0
        received_command = 0

        ETC_HOME_STATUS = 0
        ETC_POSITIVE_LIMIT = 1
        ETC_NEGATIVE_LIMIT = 2
        ETC_DRIVE_FAULT = 3
        ETC_PCAP_ERROR_BIT = 4

        # Read chip ID and initialize EtherCAT
        chip_id = Etc_Read_Reg(ID_REV, 4)
        etc_init_ok = etc_init()

        # EtherCAT Communication
        if etc_init_ok:
        print("Etercat Initialized")
            etc_scan()
        else:
            etc_init_ok = etc_init()
            print("Issue in ethercat init")

        # EtherCAT Command Receive
        received_command = Etc_Buffer_Out.LANLong[0]
        received_setpoint = float(Etc_Buffer_Out.LANFloat[1])
      

        # EtherCAT Send Status
        etc_status_reg &= ~(1 << ETC_HOME_STATUS)
        etc_status_reg &= ~(1 << ETC_DRIVE_FAULT)
        Etc_Buffer_In.LANFloat[2] = float(enc_deg)
        Etc_Buffer_In.LANFloat[3] = float(enc_rpm)
        Etc_Buffer_In.LANFloat[4] = float(avg_current)
        Etc_Buffer_In.LANFloat[0] = float(etc_status_reg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


