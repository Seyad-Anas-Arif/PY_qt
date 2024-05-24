import spidev
import time

# Constants for SPI configuration
SPI_BUS = 2        # SPI bus number
SPI_DEVICE = 0     # SPI device number
SPI_MODE = 3       # SPI mode
SPI_SPEED = 3000000 # SPI speed in Hz (3 MHz)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPI_SPEED
spi.mode = SPI_MODE

try:
    while True:
        # Write operation
        tx_data = [0x02, 0x01, 0xF8, 0x00, 0x00, 0x00, 0x00]
        rx_data = spi.xfer(tx_data)
        time.sleep(0.2)
        print("WRITE Response Data:", rx_data)
        print()

        # Read operation
        tx_data = [0x03, 0x00, 0x64, 0xFF, 0xFF, 0xFF, 0xFF]
        rx_data = spi.xfer(tx_data)
        print("READ Response Data:", rx_data)
        time.sleep(0.2)
        print()

        # Chip ID read
        tx_data = [0x03, 0x00, 0x50, 0xFF, 0xFF, 0xFF, 0xFF]
        rx_data = spi.xfer(tx_data)
        print("Chip ID Data:", rx_data)
        time.sleep(0.2)
        print()

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Exiting...")

finally:
    # Close SPI
    spi.close()
