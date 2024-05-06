import spidev
import time 
from lanh2 import *
# Global variable 
Etc_Buffer_Out = PROCBUFFER
Etc_Buffer_In  = PROCBUFFER

# Constants
SPI_BUS = 2          # SPI bus number
SPI_DEVICE = 0       # SPI device number
SPI_Mode = 0b00

# Create SPI object
spi = spidev.SpiDev()
try:
    spi.open(SPI_BUS, SPI_DEVICE)
    spi.max_speed_hz = 1000000  # Set SPI clock speed to 1MHz
    spi.mode = SPI_Mode        # Set SPI mode to 0 (CPOL=0, CPHA=0)
except IOError as e:
    print("Error opening SPI device:", e)
    exit(1)  # Exit the program if SPI device cannot be opened
# Function to read from a directly addressable register
def Etc_Read_Reg(address, length):
    result = ULONG()
    addr = UWORD()
    xfrbuf = [0] * 7  # buffer for SPI transfer

    # Convert address to LANWord type
    addr.LANWord = address

    # Construct the SPI transfer buffer
    xfrbuf[0] = COMM_SPI_READ  # SPI read command
    xfrbuf[1] = addr.LANByte[1]  # address of the register (MSB)
    xfrbuf[2] = addr.LANByte[0]  # address of the register (LSB)
    print("\n Before chages ")
    for i in range(length):
        xfrbuf[i + 3] = DUMMY_BYTE  # fill dummy bytes
        
    print(xfrbuf)

    # Send SPI transfer buffer
    xfrbuf = spi.xfer(xfrbuf)
    print("\n After read:",xfrbuf)
   # Return None if SPI communication fails
    # Extract the result from the received data
    result.LANLong = 0
    for i in range(length):
        result.LANByte[i] = xfrbuf[i + 3]  # read the requested number of bytes (LSB first)

    return result.LANLong

# Function to write to a directly addressable register
def Etc_Write_Reg(address, DataOut):
    Data = ULONG()
    Addr = UWORD()
    xfrbuf = [0] * 7  # buffer for SPI transfer

    # Convert address and data to LANWord and LANLong types respectively
    Addr.LANWord = address
    Data.LANLong = DataOut

    # Construct the SPI transfer buffer
    xfrbuf[0] = COMM_SPI_WRITE  # SPI write command
    xfrbuf[1] = Addr.LANByte[1]  # address of the register (MSB)
    xfrbuf[2] = Addr.LANByte[0]  # address of the register (LSB)
    for i in range(4):
        xfrbuf[i + 3] = Data.LANByte[i]  # data to be written (LSB first)
        # Send SPI transfer buffer
     xfrbuf = spi.xfer(xfrbuf)
     print("write reg",xfrbuf)
   
# Function to read an indirectly addressable register
def Etc_Read_Reg_Wait(address, length):
    TempLong = ULONG()
    Addr = UWORD()
    
    Addr.LANWord = address
    TempLong.LANByte[0] = Addr.LANByte[0]  # address of the register
    TempLong.LANByte[1] = Addr.LANByte[1]  # to read, LsByte first
    TempLong.LANByte[2] = length           # number of bytes to read
    TempLong.LANByte[3] = ESC_READ         # ESC read

    Etc_Write_Reg(ECAT_CSR_CMD, TempLong.LANLong)  # Write the command
    TempLong.LANByte[3] = ECAT_CSR_BUSY

    while True:
        TempLong.LANLong = Etc_Read_Reg(ECAT_CSR_CMD, 4)  # Wait for command execution
        if not (TempLong.LANByte[3] & ECAT_CSR_BUSY):
            break

    TempLong.LANLong = Etc_Read_Reg(ECAT_CSR_DATA, length)  # Read the requested register
    return TempLong.LANLong

# Function to write an indirectly addressable register
def Etc_Write_Reg_Wait(address, DataOut):
    TempLong = ULONG()
    Addr = UWORD()
    
    Addr.LANWord = address
    Etc_Write_Reg(ECAT_CSR_DATA, DataOut)          # Write the data

    # Compose the command
    TempLong.LANByte[0] = Addr.LANByte[0]          # Address of the register
    TempLong.LANByte[1] = Addr.LANByte[1]          # To write, LsByte first
    TempLong.LANByte[2] = 4                        # We write always 4 bytes
    TempLong.LANByte[3] = ESC_WRITE                # ESC write

    Etc_Write_Reg(ECAT_CSR_CMD, TempLong.LANLong)  # Write the command
    TempLong.LANByte[3] = ECAT_CSR_BUSY

    while True:
        TempLong.LANLong = Etc_Read_Reg(ECAT_CSR_CMD, 4)  # Wait for command execution
        if not (TempLong.LANByte[3] & ECAT_CSR_BUSY):
            break

# Function to read from process ram fifo
def Etc_Read_Fifo():
    TempLong = ULONG()
    xfrbuf = [0] * 35  # Buffer for spi xfr

    Etc_Write_Reg(ECAT_PRAM_RD_ADDR_LEN, 0x00201000)  # We always read 32 bytes (0x0020), output process ram offset 0x1000
    Etc_Write_Reg(ECAT_PRAM_RD_CMD, 0x80000000)       # Start command
    TempLong.LANLong = 0
    while True:
        TempLong.LANLong = Etc_Read_Reg(ECAT_PRAM_RD_CMD, 4)  # Wait for data to be transferred from the output process ram to the read fifo
        if (TempLong.LANByte[0] & PRAM_READ_AVAIL) and (TempLong.LANByte[1] == 8):
            break 

    xfrbuf[0] = COMM_SPI_READ        # SPI read command
    xfrbuf[1] = 0x00                  # Address of the read
    xfrbuf[2] = 0x00                  # FIFO MsByte first
    for i in range(32):               # 32 bytes dummy data
        xfrbuf[i + 3] = DUMMY_BYTE

    xfrbuf = spi.xfer(xfrbuf)

    for i in range(32):               # 32 bytes read data to usable buffer
        Etc_Buffer_Out.LANByte[i] = xfrbuf[i + 3]

# Function to write to the process ram fifo
def Etc_Write_Fifo():
    TempLong = ULONG()
    xfrbuf = [0] * 35  # Buffer for spi xfr

    Etc_Write_Reg(ECAT_PRAM_WR_ADDR_LEN, 0x00201200)  # We always write 32 bytes (0x0020), input process ram offset 0x1200
    Etc_Write_Reg(ECAT_PRAM_WR_CMD, 0x80000000)       # Start command
    TempLong.LANLong = 0
    while True:
        TempLong.LANLong = Etc_Read_Reg(ECAT_PRAM_WR_CMD, 4)  # Check fifo has available space for data to be written
        if (TempLong.LANByte[0] & PRAM_WRITE_AVAIL) and (TempLong.LANByte[1] >= 8):
            break

    xfrbuf[0] = COMM_SPI_WRITE      # SPI write command
    xfrbuf[1] = 0x00                 # Address of the write fifo
    xfrbuf[2] = 0x20                 # MsByte first
    for i in range(32):              # 32 bytes write loop
        xfrbuf[i + 3] = Etc_Buffer_In.LANByte[i]

    xfrbuf = spi.xfer(xfrbuf)

# Function to initialize / check the etc interface on SPI, return true if initialization is ok
def Etc_Init():
    TempLong = ULONG()
    print("Enter int to etc init")
    Etc_Write_Reg(RESET_CTL, (DIGITAL_RST & ETHERCAT_RST))  # LAN9252 reset
    time.sleep(0.1)
    TempLong.LANLong = Etc_Read_Reg(BYTE_TEST, 4)             # read test register

    if TempLong.LANLong != 0x87654321:                      # if the test register is not ok
        print("chip id not matched")
        return False

    TempLong.LANLong = Etc_Read_Reg(HW_CFG, 4)              # check also the READY flag
    if (TempLong.LANLong & READY) == 0:
        print("ready flag on red")
        return False
    print("succes fully initialized")
    return True

# Function for one scan of etc
def Etc_Scan():
    print("scan started")
    WatchDog = False
    Operational = False
    TempLong = ULONG()

    TempLong.LANLong = Etc_Read_Reg_Wait(WDOG_STATUS, 1)      # read watchdog status
    if (TempLong.LANByte[0] & 0x01) == 0x01:
        WatchDog = False
    else:
        WatchDog = True

    TempLong.LANLong = Etc_Read_Reg_Wait(AL_STATUS_REG_0, 1)  # read the EtherCAT State Machine status
    Status = TempLong.LANByte[0] & 0x0F
    if Status == ESM_OP:                                      # to see if we are in operational state
        Operational = True
    else:
        Operational = False

    if WatchDog or not Operational:                           # if watchdog is active or we are not in operational state, reset the output buffer
        for i in range(8):
            Etc_Buffer_Out.LANLong[i] = 0
    else:
        Etc_Read_Fifo()                                       # otherwise transfer process data from the EtherCAT core to the output buffer
        Etc_Write_Fifo()                                      # transfer process data from the input buffer to the EtherCAT core

    if WatchDog:                                              # return the status of the State Machine and of the watchdog
        Status |= 0x80
    return Status
    print("Exited from scan")
# Close SPI connection
spi.close()
