
import spidev
from lanh import *
spi = spidev.SpiDev() 
def LAN925X_SPI_Init():
    spi = spidev.SpiDev()
    spi.open(2, 0)  # Use SPI bus 0, device 0
    spi.max_speed_hz = 3000000  # Set SPI speed to 3 MHz
    spi.mode = 0b11  # Set SPI mode to 0b00 (CPOL=0, CPHA=0)
    return spi

def SPI_8bit_Read():
    return spi.xfer([0])[0]

def SPI_8bit_Write( wdata):
    spi.xfer([wdata])

def SQI_RESET():
    for _ in range(8):
        SPI_8bit_Write(0xFF)

def LAN925X_SPI_READ(addr):
    rdata = 0
    SPI_8bit_Write( 0x03)  # Instruction
    SPI_8bit_Write( addr >> 8)  # Address high byte
    SPI_8bit_Write( addr & 0xFF)  # Address low byte
    for _ in range(4):
        rdata <<= 8
        rdata |= SPI_8bit_Read()
    return rdata

def LAN925X_SPI_WRITE( addr, data):
    SPI_8bit_Write( 0x02)  # Instruction
    SPI_8bit_Write( addr >> 8)  # Address high byte
    SPI_8bit_Write( addr & 0xFF)  # Address low byte
    SPI_8bit_Write( data & 0xFF)  # Data byte 0
    SPI_8bit_Write( (data >> 8) & 0xFF)  # Data byte 1
    SPI_8bit_Write( (data >> 16) & 0xFF)  # Data byte 2
    SPI_8bit_Write( (data >> 24) & 0xFF)  # Data byte 3

def spi_close():
     spi.close()
