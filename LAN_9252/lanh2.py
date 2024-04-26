import ctypes

# Access to EtherCAT registers
RESET_CTL               = 0x01F8
ECAT_CSR_DATA           = 0x0300
ECAT_CSR_CMD            = 0x0304
ECAT_PRAM_RD_ADDR_LEN   = 0x0308
ECAT_PRAM_RD_CMD        = 0x030C
ECAT_PRAM_WR_ADDR_LEN   = 0x0310
ECAT_PRAM_WR_CMD        = 0x0314
ECAT_PRAM_RD_DATA       = 0x0000
ECAT_PRAM_WR_DATA       = 0x0020
ID_REV                  = 0x0050
IRQ_CFG                 = 0x0054
INT_STS                 = 0x0058
INT_EN                  = 0x005C
BYTE_TEST               = 0x0064
HW_CFG                  = 0x0074
PMT_CTRL                = 0x0084
GPT_CFG                 = 0x008C
GPT_CNT                 = 0x0090
FREE_RUN                = 0x009C

# LAN9252 Datasheet TABLE 12-15: ETHERCAT CORE CSR REGISTERS
TYPE_REG                = 0x0000
REV_REG                 = 0x0001
BUILD_REG_1             = 0x0002
BUILD_REG_2             = 0x0003
FMMU_REG                = 0x0004
SYNCMANAGER_REG         = 0x0005
RAM_SIZE_REG            = 0x0006
PORT_DESCR_REG          = 0x0007
ESC_FEATUR_REG_1        = 0x0008
ESC_FEATUR_REG_2        = 0x0009
CONF_STATION_REG_1      = 0x0010
CONF_STATION_REG_2      = 0x0011
CONF_STATION_ALI_REG_1  = 0x0012
CONF_STATION_ALI_REG_2  = 0x0013

# Write Protection Register
WD_REG_EN               = 0x0020
WD_REG_PR               = 0x0021
ESC_WD_REG_EN           = 0x0030
ESC_WD_REG_PR           = 0x0031

# Data Link Layer
ESC_RST_REG             = 0x0040
ESC_RST_PDI_REG         = 0x0041
ECL_DL_CTRL_REG_0       = 0x0100
ECL_DL_CTRL_REG_1       = 0x0101
ECL_DL_CTRL_REG_2       = 0x0102
ECL_DL_CTRL_REG_3       = 0x0103
PHY_R_W_OFF_1           = 0x0108
PHY_R_W_OFF_2           = 0x0109
ECL_DL_STATUS_REG_0     = 0x0110
ECL_DL_STATUS_REG_1     = 0x0111

# Application Layer
AL_CTRL_REG_0           = 0x0120
AL_CTRL_REG_1           = 0x0121
AL_STATUS_REG_0         = 0x0130
AL_STATUS_REG_1         = 0x0131
AL_STATUS_COD_REG_0     = 0x0134
AL_STATUS_COD_REG_1     = 0x0135
RUN_LED_OVERRIDE_REG    = 0x0138

# PDI (Process Data Interface)
PDI_CTRL_REG            = 0x0140
ESC_CONF_REG            = 0x0141
ASIC_CONF_REG_0         = 0x0142
ASIC_CONF_REG_1         = 0x0143
PDI_CONF_REG            = 0x0150
SYNC_PDI_CONF_REG       = 0x0151
EXT_PDI_CONF_REG_0      = 0x0152
EXT_PDI_CONF_REG_1      = 0x0153

# Interrupts
ECAT_EVENT_MASK_REG_0   = 0x0200
ECAT_EVENT_MASK_REG_1   = 0x0201
AL_EVENT_MASK_REG_0     = 0x0204
AL_EVENT_MASK_REG_1     = 0x0205
AL_EVENT_MASK_REG_2     = 0x0206
AL_EVENT_MASK_REG_3     = 0x0207
ECAT_EVENT_REQ_REG_0    = 0x0210
ECAT_EVENT_REQ_REG_1    = 0x0211
AL_EVENT_REQ_REG_0      = 0x0220
AL_EVENT_REQ_REG_1      = 0x0221
AL_EVENT_REQ_REG_2      = 0x0222
AL_EVENT_REQ_REG_3      = 0x0223

# Error Counters
RX_ERROR_CNT_REG_0      = 0x0300
RX_ERROR_CNT_REG_7      = 0x0307
FWD_RX_ERROR_CNT_REG_0  = 0x0308
FWD_RX_ERROR_CNT_REG_B  = 0x030B
ECAT_PRO_UNIT_CNT_ERROR = 0x030C
PDI_CNT_ERROR           = 0x030D
PDI_CODE_ERROR          = 0x030E
LOST_LINK_CNT_REG_0     = 0x0310 
LOST_LINK_CNT_REG_3     = 0x0313 

# EEPROM Interface
EEPROM_CONF_REG         = 0x0500
EEPROM_PDI_STATE_REG    = 0x0501
EEPROM_CTRL_REG_0       = 0x0502
EEPROM_CTRL_REG_1       = 0x0503
EEPROM_ADDR_REG_0       = 0x0504
EEPROM_ADDR_REG_4       = 0x0507
EEPROM_DATA_REG_0       = 0x0508
EEPROM_DATA_REG_4       = 0x050B

# MII Management Interface
MII_MANAGE_CTRL_REG_0   = 0x0510
MII_MANAGE_CTRL_REG_1   = 0x0511
PHY_ADDR_REG            = 0x0512
PHY_REGISTER_ADDR_REG   = 0x0513
PHY_DATA_REG_0          = 0x0514
PHY_DATA_REG_1          = 0x0515
MII_MANAGE_ECAT_REG     = 0x0516
MII_MANAGE_PDI_REG      = 0x0517
AL_STATUS               = 0x0130
WDOG_STATUS             = 0x0440

# LAN9252 flags
ECAT_CSR_BUSY           = 0x80
PRAM_READ_BUSY          = 0x80
PRAM_READ_AVAIL         = 0x01
PRAM_WRITE_AVAIL        = 0x01
READY                   = 0x08000000
DIGITAL_RST             = 0x00000001
ETHERCAT_RST            = 0x00000040

# EtherCAT flags
ESM_INIT                = 0x01
ESM_PREOP               = 0x02
ESM_BOOT                = 0x03
ESM_SAFEOP              = 0x04
ESM_OP                  = 0x08

# ESC commands
ESC_WRITE               = 0x80
ESC_READ                = 0xC0

# SPI
COMM_SPI_READ           = 0x03
COMM_SPI_WRITE          = 0x02
DUMMY_BYTE              = 0xFF

class UWORD(ctypes.Union):
    _fields_ = [("LANWord", ctypes.c_uint16),
                ("LANByte", ctypes.c_uint8 * 2)]

class ULONG(ctypes.Union):
    _fields_ = [("LANLong", ctypes.c_uint32),
                ("LANWord", ctypes.c_uint16 * 2),
                ("LANByte", ctypes.c_uint8 * 4)]

class PROCBUFFER(ctypes.Union):
    _fields_ = [("LANByte", ctypes.c_uint8 * 32),
                ("LANLong", ctypes.c_uint32 * 8)]
