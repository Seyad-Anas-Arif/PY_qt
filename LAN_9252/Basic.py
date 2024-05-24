import spidev
import time

# Constants for SPI configuration
SPI_BUS = 2         # SPI bus number (change according to your setup)
SPI_DEVICE = 0      # SPI device number (change according to your setup)
SPI_MODE = 0        # SPI mode
SPI_SPEED = 500000 # SPI speed in Hz (5 MHz)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPI_SPEED
spi.mode = SPI_MODE

try:
    while True:
        # Write operation
        tx_data_write = 565114616938496
        rx_data_write = spi.xfer2([tx_data_write])
        print("WRITE Response Data:", rx_data_write)
        time.sleep(0.2)

        # Read operation
        tx_data_read = 844858721828863
        rx_data_read = spi.xfer2([tx_data_read])
        print("READ Response Data:", rx_data_read)
        time.sleep(0.2)

        # Chip ID read
        tx_data_chip_id = 844858721828863
        rx_data_chip_id = spi.xfer2([tx_data_chip_id])
        print("Chip ID Data:", rx_data_chip_id)
        time.sleep(0.2)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Exiting...")

finally:
    # Close SPI
    spi.close()
