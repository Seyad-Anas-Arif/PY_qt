import time
import spidev
import adxl345.base

WRITE_MASK = 0x0
READ_MASK = 0x80
MULTIREAD_MASK = 0x40

#lan9252

read_mask = 0x03

class ADXL345(adxl345.base.ADXL345_Base):
    def __init__(self, spi_bus=2, spi_device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_bus, spi_device)
        self.spi.mode = 0b11
        self.spi.max_speed_hz = 5000000
        self.spi.bits_per_word = 8
        self.spi.threewire = False
        self.spi.cshigh = False
        self.spi.lsbfirst = False


# Example usage
if __name__ == "__main__":
    # Create an instance of the ADXL345 driver
    adxl345 = ADXL345()
    

    # Read acceleration values
    while True:
        tx_data = [0x03, 0x00, 0x64, 0xFF, 0xFF, 0xFF, 0xFF]
        # Perform SPI transaction
        rx_data = spi.xfer2(tx_data)
        # Display received data
        print(" READ Response Data:", rx_data)
        time.sleep(1)
