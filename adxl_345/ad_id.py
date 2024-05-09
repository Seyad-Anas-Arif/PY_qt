import time
import spidev
import adxl345.base

WRITE_MASK = 0x0
READ_MASK = 0x80
MULTIREAD_MASK = 0x40

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

    def get_register(self, address):
        value = self.spi.xfer2([address | READ_MASK])
        return value[0]

    def get_registers(self, address, count):
        self.spi.writebytes([address | READ_MASK | MULTIREAD_MASK])
        values = self.spi.readbytes(count)
        return values

    def set_register(self, address, value):
        self.spi.writebytes([address | WRITE_MASK, value])

# Example usage
if __name__ == "__main__":
    # Create an instance of the ADXL345 driver
    adxl345 = ADXL345()

    # Read the device ID register (register address 0x00)
    device_id = adxl345.get_register(0x00)

    # Print the device ID
    print("Device ID:", device_id)
   # Optional: Set the range and resolution of the sensor
    adxl345.set_range(16)  # Set range to +/- 16g
    adxl345.set_data_rate(100)  # Set data rate to 100 Hz

    # Read acceleration values
    while True:
        acceleration = adxl345.get_axes()
        x = acceleration['x']* 0.0078
        y = acceleration['y']* 0.0078
        z = acceleration['z']* 0.0078

        # Print the acceleration values
        print("Acceleration - X: %.2f g, Y: %.2f g, Z: %.2f g" % (x, y, z))

        time.sleep(1)

