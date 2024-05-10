import spidev
from lanh import *
import RPi.GPIO as GPIO

SPI_CS_PIN = 2

def SPI_CS_LOW():
    GPIO.output(SPI_CS_PIN, GPIO.LOW)

def SPI_CS_HIGH():
    GPIO.output(SPI_CS_PIN, GPIO.HIGH)

def LAN925X_SPI_Init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SPI_CS_PIN, GPIO.OUT)
    SPI_CS_HIGH()
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Use SPI bus 0, device 0
    spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz
    spi.mode = 0b00  # Set SPI mode to 0b00 (CPOL=0, CPHA=0)
    return spi

def SPI_8bit_Read(spi):
    return spi.xfer([0])[0]

def SPI_8bit_Write(spi, wdata):
    spi.xfer([wdata])

def SQI_RESET():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SPI_CS_PIN, GPIO.OUT)
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_HIGH()
    SPI_CS_LOW()
    SPI_8bit_Write(0xFF)
    SPI_CS_HIGH()

def LAN925X_SPI_READ(spi, addr):
    rdata = 0
    SPI_CS_LOW()
    SPI_8bit_Write(spi, 0x03)  # Instruction
    SPI_8bit_Write(spi, addr >> 8)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    for _ in range(4):
        rdata <<= 8
        rdata |= SPI_8bit_Read(spi)
    SPI_CS_HIGH()
    return rdata

def LAN925X_SPI_WRITE(spi, addr, data):
    SPI_CS_LOW()
    SPI_8bit_Write(spi, 0x02)  # Instruction
    SPI_8bit_Write(spi, addr >> 8)  # Address high byte
    SPI_8bit_Write(spi, addr & 0xFF)  # Address low byte
    SPI_8bit_Write(spi, data & 0xFF)  # Data byte 0
    SPI_8bit_Write(spi, (data >> 8) & 0xFF)  # Data byte 1
    SPI_8bit_Write(spi, (data >> 16) & 0xFF)  # Data byte 2
    SPI_8bit_Write(spi, (data >> 24) & 0xFF)  # Data byte 3
    SPI_CS_HIGH()

