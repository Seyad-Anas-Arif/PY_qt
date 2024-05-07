import spidev
import time
spi = spidev.SpiDev()
spi.open(2, 0)  # Assuming SPI bus 0, device 0
spi.max_speed_hz = 1000000  # Adjust as needed
spi.mode = 3

def main():
    # Initialize EtherCAT interface
    if not etc_init():
        print("EtherCAT initialization failed")
        return

if __name__ == "__main__":
    while True:
        main()  # Call the main function
        time.sleep(2)  # Sleep for 2 seconds before running again
