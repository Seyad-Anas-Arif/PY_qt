import spidev

# Define LAN9252 registers
ECAT_PRAM_RD_DATA       = 0x000
ECAT_PRAM_WR_DATA       = 0x020
ID_REV                  = 0x050
IRQ_CFG                 = 0x054
INT_STS                 = 0x058
INT_EN                  = 0x05C
BYTE_TEST               = 0x064
HW_CFG                  = 0x074
PMT_CTRL                = 0x084
GPT_CFG                 = 0x08C
GPT_CNT                 = 0x090
FREE_RUN                = 0x09C
RESET_CTL               = 0x1F8

ETHERCAT_RST            = 0x40
PHY_B_RST               = 0x04
PHY_A_RST               = 0x02
DIGITAL_RST             = 0x01

ECAT_CSR_DATA           = 0x300
ECAT_CSR_CMD            = 0x304
CSR_BUSY                = 1 << 31
CSR_SIZE_8bit           = 1
CSR_SIZE_16bit          = 2
CSR_SIZE_32bit          = 4
ECAT_PRAM_RD_ADDR_LEN   = 0x308
ECAT_PRAM_RD_CMD        = 0x30C
ECAT_PRAM_WR_ADDR_LEN   = 0x310
ECAT_PRAM_WR_CMD        = 0x314

PRAM_READ_BUSY  = 1 << 31
PRAM_READ_ABORT = 1 << 30
PRAM_WRITE_BUSY = 1 << 31
PRAM_WRITE_ABORT = 1 << 30

# Define ESC Information
Type_Register = 0x0000
Revision_Register = 0x0001
Build_Register = 0x0002
FMMUs_Supported = 0x0004
SyncManagers_Supported = 0x0005
RAM_Size = 0x0006
Port_Descriptor = 0x0007
ESC_Features_Supported = 0x0008

# Define Station Address
Configured_Station = 0x0010
Configured_Station_Alias = 0x0012

# Define Write Protection
Write_Enable = 0x0020
Write_Protection = 0x0021
ESC_Write_Enable = 0x0030
ESC_Write_Protection = 0x0031

# Define Data Link Layer
ESC_Reset_ECAT = 0x0040
ESC_Reset_PDI = 0x0041
ESC_DL_Control = 0x0100
Physical_Read_Write_Offset = 0x0108
ESC_DL_Status = 0x0110

# Define Application Layer
AL_Control = 0x0120
AL_Status = 0x0130
AL_Status_Code = 0x0134
RUN_LED_Override = 0x0138

# Define PDI (Process Data Interface)
PDI_Control = 0x0140
ESC_Configuration = 0x0141
ASIC_Configuration = 0x0142
PDI_Configuration = 0x0150
Sync_Latch_PDI_Configuration = 0x0151
Extended_PDI_Configuration = 0x0152

# Define Interrupts
ECAT_Event_Mask = 0x0200
AL_Event_Mask = 0x0204
ECAT_Event_Request = 0x0210
AL_Event_Request = 0x0220

# Define Error Counters
RX_Error_Counters = 0x0300
Forwarded_RX_Error_Counters = 0x0308
ECAT_Processing_Unit_Error_Counter = 0x030C
PDI_Error_Counter = 0x030D
PDI_Error_Code = 0x030E
Lost_Link_Counters = 0x0310

# Define Watchdogs
Watchdog_Time_PDI = 0x0410
Watchdog_Time_Process_Data = 0x0420
Watchdog_Status_Process_Data = 0x0440
Watchdog_Counter_Process_Data = 0x0442
Watchdog_Counter_PDI = 0x0443

# Define EEPROM Interface
EEPROM_Configuration = 0x0500
EEPROM_PDI_Access_State = 0x0501
EEPROM_Control_Status = 0x0502
EEPROM_Address = 0x0504
EEPROM_Data = 0x0508

# Define MII Management Interface
MII_Management_Control_Status = 0x0510
PHY_Address = 0x0512
PHY_Register_Address = 0x0513
PHY_DATA = 0x0514
MII_Management_ECAT_Access_State = 0x0516
MII_Management_PDI_Access_State = 0x0517
PHY_Port_Statuss = 0x0518

# Define PRAM Read/Write Registers
PRAM_READ_BUSY  = 1 << 31
PRAM_READ_ABORT = 1 << 30
PRAM_WRITE_BUSY = 1 << 31
PRAM_WRITE_ABORT = 1 << 30

# Define Distributed Clocks - Receive Times
Receive_Time_Port_0 = 0x0900
Receive_Time_Port_1 = 0x0904
Receive_Time_Port_2 = 0x0908

# Define ESC Specific
Product_ID = 0x0E00
Vendor_ID = 0x0E08

# Define Digital Input/Output
Digital_IO_Output_Data = 0x0F00
General_Purpose_Output = 0x0F10
General_Purpose_Input = 0x0F18

# Define User RAM
User_RAM = 0x0F80

# Define Process Data RAM
Process_Data_RaM = 0x1000

