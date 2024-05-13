import spidev

# Initialize SPI
spi = spidev.SpiDev()
spi.open(2, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 30000000  # Set SPI speed to 30 MHz

# Data to be transmitted
tx_data = [0x02, 0x01, 0xF8, 0x00, 0x00, 0x00, 0x00]

# Perform SPI transaction
rx_data = spi.xfer(tx_data)

print(" WRITE Received Data:", rx_data)
print()

# Data to be transmitted
tx_data = [0x03, 0x00, 0x64, 0xFF, 0xFF, 0xFF, 0xFF]

# Perform SPI transaction
rx_data = spi.xfer(tx_data)

# Display received data
print(" READ Received Data:", rx_data)

print()

# Data to be transmitted
tx_data = [0x03, 0x00, 0x50, 0xFF, 0xFF, 0xFF, 0xFF]

# Perform SPI transaction
rx_data = spi.xfer(tx_data)

# Display received data
print("Received Data:", rx_data)

# Close SPI
spi.close()
