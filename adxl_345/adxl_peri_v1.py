from periphery import SPI
import time

# Constants
SPI_BUS = "/dev/spidev2.0"  # SPI device path
SPI_SPEED = 500000  # SPI speed in Hz
SPI_MODE = 0

# SPI setup
spi = SPI(SPI_BUS, SPI_MODE, SPI_SPEED)

# Functions
def adxl_write(address, value):
    data = [address | 0x40, value]
    spi.transfer(data)  # Transmit the address and data

def adxl_read(address, length):
    address |= 0x80  # Read operation
    address |= 0x40  # Multibyte read
    data = spi.transfer([address] + [0x00] * length)  # Send the address and read `length` bytes of data
    return data[1:]  # Skip the first byte (address byte)

def adxl_init():
    adxl_write(0x2D, 0x00)  # Power Control: reset all bits
    time.sleep(0.01)
    adxl_write(0x2D, 0x08)  # Power Control: Measure mode
    adxl_write(0x31, 0x01)  # Data Format: +/- 4g range

# Helper function to convert raw data to signed integer
def convert_to_signed(value):
    if value & (1 << 15):  # If the sign bit is set
        value -= (1 << 16)
    return value

# Main function
def main():
    adxl_init()  # Initialize ADXL345
    time.sleep(0.1)
    
    # Read the device ID
    device_id = adxl_read(0x00, 1)[0]
    print("Device ID:", device_id)
    
    while True:
        # Read data
        data_rec = adxl_read(0x32, 6)
        print("Raw Data:", data_rec)  # Debug: print raw data

        x = convert_to_signed((data_rec[1] << 8) | data_rec[0])
        y = convert_to_signed((data_rec[3] << 8) | data_rec[2])
        z = convert_to_signed((data_rec[5] << 8) | data_rec[4])

        # Convert into 'g'
        xg = x * 0.0078
        yg = y * 0.0078
        zg = z * 0.0078

        # Display the result (print to console)
        print("X: %.5f g, Y: %.5f g, Z: %.5f g" % (xg, yg, zg))

        # Wait for 1000 ms
        time.sleep(1)

if __name__ == "__main__":
    main()
