import spidev

# Define ADXL345 registers
ADXL345_REG_DEVID      = 0x00
ADXL345_REG_DATAX0     = 0x32
ADXL345_REG_DATAY0     = 0x34
ADXL345_REG_DATAZ0     = 0x36
ADXL345_REG_POWER_CTL  = 0x2D
ADXL345_REG_DATA_FORMAT= 0x31
ADXL345_REG_BW_RATE    = 0x2C

# Define ADXL345 constants
ADXL345_RANGE_2_G      = 0x00

class Adafruit_ADXL345_Unified:
    def __init__(self, sensorID):
        self._sensorID = sensorID
        self.spi = spidev.SpiDev()
        self.spi.open(2, 0)  # Use SPI bus 0, device 0
        self.spi.max_speed_hz = 5000000  # Set SPI speed to 1 MHz
        self.spi.mode = 0b01  # Set SPI mode to 0b01 (CPOL=0, CPHA=1)
       # self.setRange(ADXL345_RANGE_2_G)

    def __del__(self):
        if self.spi:
            self.spi.close()

    def writeRegister(self, reg, value):
        self.spi.xfer2([reg, value])

    def readRegister(self, reg):
        return self.spi.xfer2([reg ])

    def read16(self, reg):
        low_byte = self.readRegister(reg)
        high_byte = self.readRegister(reg + 1)
        return (high_byte << 8) | low_byte

    def getDeviceID(self):
        return self.readRegister(ADXL345_REG_DEVID)

    def getX(self):
        return self.read16(ADXL345_REG_DATAX0)

    def getY(self):
        return self.read16(ADXL345_REG_DATAY0)

    def getZ(self):
        return self.read16(ADXL345_REG_DATAZ0)

    def begin(self):
     device_id = self.getDeviceID()
     if isinstance(device_id, list):
        # If getDeviceID() returns a list, take the first element
        device_id = device_id[0]

     print("ADXL345 Device ID:", hex(device_id))
     if device_id != 0xE5:
        return False
     self.writeRegister(ADXL345_REG_POWER_CTL, 0x08)  # Enable measurements
     return True

    def getDataRate(self):
        return self.readRegister(ADXL345_REG_BW_RATE)

    def setDataRate(self, dataRate):
        self.writeRegister(ADXL345_REG_BW_RATE, dataRate)

# Example usage
if __name__ == "__main__":
    print("Script started")

    adxl = Adafruit_ADXL345_Unified(sensorID=123)
    if adxl.begin():
        print("ADXL345 detected!")
        print("X-axis acceleration:", adxl.getX())
        print("Y-axis acceleration:", adxl.getY())
        print("Z-axis acceleration:", adxl.getZ())

