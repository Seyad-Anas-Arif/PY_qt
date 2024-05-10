import spidev
import gpiod
from lanh import *

SPI_CS_PIN = 2

def SPI_CS_LOW(line):
    line.set_value(0)

def SPI_CS_HIGH(line):
    line.set_value(1)

def LAN925X_SPI_Init():
    chip = gpiod.Chip("gpiochip0")
    line = chip.get_line(SPI_CS_PIN)
    line.request(consumer="lan925x-spi-init", direction=gpiod.LineDirection.OUTPUT, default_vals=[1])
    
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Use SPI bus 0, device 0
    spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz
    spi.mode = 0b00  # Set SPI mode to 0b00 (CPOL=0, CPHA=0)
    
    return spi, line

def SPI_8bit_Read(spi):
    return spi.xfer([0])[0]

def SPI_8bit_Write(spi, wdata):
    spi.xfer([wdata])

def SQI_RESET(line):
    line.release()
    chip = gpiod.Chip("gpiochip0")
    line = chip.get_line(SPI_CS_PIN)
    line.request(consumer="lan925x-spi-reset", direction=gpiod.LineDirection.OUTPUT, default_vals=[1])
    
    SPI_CS_HIGH(line)
    for _ in range(8):
        SPI_CS_HIGH(line)
    SPI_CS_LOW(line)
    SPI_8bit_Write(0xFF)
    SPI_CS_HIGH(line)

def LAN925X_SPI_READ(spi, line, addr):
    rdata = 0
    SPI_CS_LOW(line)
    SPI_8bit_Write(spi, 0x03)  # Instruction
    SPI_8bit_Write(spi, addr >> 8)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    for _ in range(4):
        rdata <<= 8
        rdata |= SPI_8bit_Read(spi)
    SPI_CS_HIGH(line)
    return rdata

def LAN925X_SPI_WRITE(spi, line, addr, data):
    SPI_CS_LOW(line)
    SPI_8bit_Write(spi, 0x02)  # Instruction
    SPI_8bit_Write(spi, addr >> 8)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    SPI_8bit_Write(spi, data & 0xFF)  # Data byte 0
    SPI_8bit_Write(spi, (data >> 8) & 0xFF)  # Data byte 1
    SPI_8bit_Write(spi, (data >> 16) & 0xFF)  # Data byte 2
    SPI_8bit_Write(spi, (data >> 24) & 0xFF)  # Data byte 3
    SPI_CS_HIGH(line)

