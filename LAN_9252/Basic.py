import spidev
import time
from ctypes import Union, c_uint16, c_uint8, c_uint32

ID_REV = 0x0050
COMM_SPI_READ = 0x03
DUMMY_BYTE = 0xFF

spi = spidev.SpiDev()
spi.open(2, 0)  # Assuming SPI bus 2, device 0
spi.max_speed_hz = 1000000  # Adjust as needed
spi.mode = 3

class UWORD(Union):
    _fields_ = [("LANWord", c_uint16),
                ("LANByte", c_uint8 * 2)]

class ULONG(Union):
    _fields_ = [("LANLong", c_uint32),
                ("LANWord", c_uint16 * 2),
                ("LANByte", c_uint8 * 4)]

def Etc_Read_Reg(address, length):
    Result = ULONG()
    Addr = UWORD()
    xfrbuf = (c_uint8 * (3 + length))()  # Adjust buffer size

    Addr.LANWord = address

    xfrbuf[0] = COMM_SPI_READ
    xfrbuf[1] = Addr.LANByte[1]
    xfrbuf[2] = Addr.LANByte[0]

    response = spi.xfer2(xfrbuf)  # Use xfer2 for SPI transfer

    for i in range(length):
        Result.LANByte[i] = response[i + 3]
    return Result.LANLong

def main():
    c_uint32.chip_id = Etc_Read_Reg(ID_REV, 4)
    print("chip id is ", c_uint32.chip_id)
    time.sleep(1)

if __name__ == "__main__":
    while True:
        main()
