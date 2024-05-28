import spidev
import time

# Constants for SPI configuration
SPI_BUS = 2         # SPI bus number (change according to your setup)
SPI_DEVICE = 0      # SPI device number (change according to your setup)
SPI_SPEED = 500000  # SPI speed in Hz (500 kHz)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPI_SPEED
spi.mode = 0  # SD cards typically use SPI mode 0

def spi_transfer(data):
    return spi.xfer2(data)

def sd_command(cmd, arg):
    crc = 0x95 if cmd == 0 else 0x87  # Default CRC values for CMD0 and CMD8
    packet = [0x40 | cmd] + [(arg >> (8 * i)) & 0xFF for i in range(3, -1, -1)] + [crc]
    response = spi_transfer(packet)
    return response

def sd_init():
    # Send 80 clock cycles to initialize SD card
    spi_transfer([0xFF] * 10)
    
    # Send CMD0 to reset the SD card
    response = sd_command(0, 0)
    while response[0] != 0x01:
        response = sd_command(0, 0)
        time.sleep(0.1)
    
    # Send CMD8 to check voltage range
    response = sd_command(8, 0x1AA)
    if response[0] != 0x01:
        print("SD card initialization failed.")
        return False
    else:
        print("SD card initialized.")
        return True

def sd_read_block(block_num):
    block_addr = block_num * 512
    response = sd_command(17, block_addr)
    if response[0] != 0x00:
        print("Failed to read block.")
        return None
    # Read 512 bytes of data
    block_data = spi_transfer([0xFF] * 512)
    return block_data

try:
    if sd_init():
        block_num = 0  # Read the first block
        block_data = sd_read_block(block_num)
        if block_data:
            print(f"Block {block_num} data: {block_data}")

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Exiting...")

finally:
    # Close SPI
    spi.close()
