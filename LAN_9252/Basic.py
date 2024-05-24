import spidev
import time

# Constants for SPI configuration
SPI_BUS = 2         # SPI bus number (change according to your setup)
SPI_DEVICE = 0      # SPI device number (change according to your setup)
SPI_MODE = 3       # SPI mode
SPI_SPEED = 500000  # SPI speed in Hz (500 kHz)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPI_SPEED
spi.mode = SPI_MODE

def int_to_byte_list(value, length):
    return [(value >> (8 * i)) & 0xFF for i in range(length - 1, -1, -1)]

try:
    while True:
        # Write operation
        tx_data_write = int_to_byte_list(0x0201F800000000, 7)
        print("WRITE Tx Data:", tx_data_write)  # Debugging print
        rx_data_write = spi.xfer2(tx_data_write)
        print("WRITE Response Data:", rx_data_write)
        time.sleep(0.2)

        # Read operation
        tx_data_read = int_to_byte_list(0x030064FFFFFFFF, 7)
        print("READ Tx Data:", tx_data_read)  # Debugging print
        rx_data_read = spi.xfer2(tx_data_read)
        print("READ Response Data:", rx_data_read)
        time.sleep(0.2)

        # Chip ID read
        tx_data_chip_id = int_to_byte_list(0x030050FFFFFFFF, 7)
        print("Chip ID Tx Data:", tx_data_chip_id)  # Debugging print
        rx_data_chip_id = spi.xfer2(tx_data_chip_id)
        print("Chip ID Data:", rx_data_chip_id)
        time.sleep(0.2)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Exiting...")

finally:
    # Close SPI
    spi.close()
