import spidev

# Initialize SPI
spi = spidev.SpiDev()
spi.open(2, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 30000000  # Set SPI speed to 30 MHz
spi.mode = 0b11

# Data to be transmitted
tx_data = [0x02, 0x01, 0xF8, 0x00, 0x00, 0x00, 0x00]

# Perform SPI transaction
rx_data = spi.xfer2(tx_data)

print(" WRITE Response Data:", rx_data)
print()

# Data to be transmitted
tx_data = [0x03, 0x00, 0x64, 0xFF, 0xFF, 0xFF, 0xFF]

# Perform SPI transaction
rx_data = spi.xfer2(tx_data)

# Display received data
print(" READ Response Data:", rx_data)

print()

# Data to be transmitted
tx_data = [0x03, 0x00, 0x50, 0xFF, 0xFF, 0xFF, 0xFF]

# Perform SPI transaction
rx_data = spi.xfer2(tx_data)

# Display received data
print("chip id Data:", rx_data)

# Close SPI
spi.close()
