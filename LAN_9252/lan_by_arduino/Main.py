from spi2 import *
import time

# LAN9252 RESET
def LAN9252_RESET():
    addr = LAN925X_SPI.RESET_CTL
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, LAN925X_SPI.ETHERCAT_RST)
    
    addr = LAN925X_SPI.BYTE_TEST
    rdata = LAN925X_SPI.LAN925X_SPI_READ(addr)
    while rdata != 0x87654321:
        addr = LAN925X_SPI.BYTE_TEST
        rdata = LAN925X_SPI.LAN925X_SPI_READ(addr)

# LAN9252 EtherCAT CSR WRITE
def LAN9252_EtherCAT_CSR_WRITE(CSR_SIZE, CSR_ADDR, CSR_DATA):
    addr = LAN925X_SPI.ECAT_CSR_DATA
    wdata = CSR_DATA
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)

    addr = LAN925X_SPI.ECAT_CSR_CMD
    wdata = LAN925X_SPI.CSR_BUSY | 0 << 30 | CSR_SIZE << 16 | CSR_ADDR  # Write
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)
    
    addr = LAN925X_SPI.ECAT_CSR_CMD
    while LAN925X_SPI.CSR_BUSY & LAN925X_SPI.LAN925X_SPI_READ(addr):
        pass

# LAN9252 EtherCAT CSR READ
def LAN9252_EtherCAT_CSR_READ(CSR_SIZE, CSR_ADDR):
    addr = LAN925X_SPI.ECAT_CSR_CMD
    wdata = LAN925X_SPI.CSR_BUSY | 1 << 30 | CSR_SIZE << 16 | CSR_ADDR  # Read
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)
    
    addr = LAN925X_SPI.ECAT_CSR_CMD
    while LAN925X_SPI.CSR_BUSY & LAN925X_SPI.LAN925X_SPI_READ(addr):
        pass
    
    addr = LAN925X_SPI.ECAT_CSR_DATA
    return LAN925X_SPI.LAN925X_SPI_READ(addr)

# LAN9252 EtherCAT Process RAM Read
def LAN9252_EtherCAT_PRAM_READ(PRAM_READ_LEN, PRAM_READ_ADDR):
    addr = LAN925X_SPI.ECAT_PRAM_RD_ADDR_LEN
    wdata = PRAM_READ_LEN << 16 | PRAM_READ_ADDR
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)

    addr = LAN925X_SPI.ECAT_PRAM_RD_CMD
    wdata = LAN925X_SPI.PRAM_READ_BUSY
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)

    addr = LAN925X_SPI.ECAT_PRAM_RD_DATA
    rdata = LAN925X_SPI.LAN925X_SPI_READ(addr)

    addr = LAN925X_SPI.ECAT_PRAM_RD_CMD
    while LAN925X_SPI.PRAM_READ_BUSY & LAN925X_SPI.LAN925X_SPI_READ(addr):
        pass
    
    return rdata

# LAN9252 EtherCAT Process RAM Write
def LAN9252_EtherCAT_PRAM_WRITE(PRAM_WRITE_LEN, PRAM_WRITE_ADDR, PRAM_WR_DATA):
    addr = LAN925X_SPI.ECAT_PRAM_WR_DATA
    wdata = PRAM_WR_DATA
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)
    
    addr = LAN925X_SPI.ECAT_PRAM_WR_ADDR_LEN
    wdata = PRAM_WRITE_LEN << 16 | PRAM_WRITE_ADDR
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)

    addr = LAN925X_SPI.ECAT_PRAM_WR_CMD
    wdata = LAN925X_SPI.PRAM_WRITE_BUSY
    LAN925X_SPI.LAN925X_SPI_WRITE(addr, wdata)

    addr = LAN925X_SPI.ECAT_PRAM_WR_CMD
    while LAN925X_SPI.PRAM_WRITE_BUSY & LAN925X_SPI.LAN925X_SPI_READ(addr):
        pass

# Example usage:
if __name__ == "__main__":
    # Initialize SPI
    spi2.LAN925X_SPI_Init()
    
    # Reset LAN9252 chip
    LAN9252_RESET()

    # Write to EtherCAT CSR
    LAN9252_EtherCAT_CSR_WRITE(1, 0x0100, 0xABCD)
    
    # Read from EtherCAT CSR
    csr_data = LAN9252_EtherCAT_CSR_READ(1, 0x0100)
    print("CSR Data:", csr_data)
    
    # Read from EtherCAT Process RAM
    pram_data = LAN9252_EtherCAT_PRAM_READ(16, 0x1000)
    print("PRAM Data:", pram_data)
    
    # Write to EtherCAT Process RAM
    LAN9252_EtherCAT_PRAM_WRITE(16, 0x1000, 0x12345678)

