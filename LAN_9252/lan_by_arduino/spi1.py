import spidev
import lanh 

def LAN925X_SPI_Init():
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Use SPI bus 0, device 0
    spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz
    spi.mode = 0b00  # Set SPI mode to 0b00 (CPOL=0, CPHA=0)
    return spi

def SPI_8bit_Read(spi):
    return spi.xfer([0])[0]

def SPI_8bit_Write(spi, wdata):
    spi.xfer([wdata])

def SQI_RESET(spi):
    for _ in range(8):
        SPI_8bit_Write(spi, 0xFF)

def LAN925X_SPI_READ(spi, addr):
    rdata = 0
    SPI_8bit_Write(spi, 0x03)  # Instruction
    SPI_8bit_Write(spi, (addr >> 8) & 0xFF)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    for _ in range(4):
        rdata <<= 8
        rdata |= SPI_8bit_Read(spi)
    return rdata

def LAN925X_SPI_WRITE(spi, addr, data):
    SPI_8bit_Write(spi, 0x02)  # Instruction
    SPI_8bit_Write(spi, (addr >> 8) & 0xFF)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    SPI_8bit_Write(spi, data & 0xFF)  # Data byte 0
    SPI_8bit_Write(spi, (data >> 8) & 0xFF)  # Data byte 1
    SPI_8bit_Write(spi, (data >> 16) & 0xFF)  # Data byte 2
    SPI_8bit_Write(spi, (data >> 24) & 0xFF)  # Data byte 3

# Example usage
if __name__ == "__main__":
    spi = LAN925X_SPI_Init()

    try:
        # Perform a SQI reset
        SQI_RESET(spi)

        # Example read from address 0x1234
        read_addr = 0x1234
        read_data = LAN925X_SPI_READ(spi, read_addr)
        print(f"Read Data from 0x{read_addr:04X}: 0x{read_data:08X}")

        # Example write to address 0x1234
        write_addr = 0x1234
        write_data = 0xDEADBEEF
        LAN925X_SPI_WRITE(spi, write_addr, write_data)
        print(f"Wrote Data 0x{write_data:08X} to 0x{write_addr:04X}")

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("Exiting...")

    finally:
        # Close SPI
        spi.close()
