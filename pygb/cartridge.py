from enum import Enum, auto

class MBCType(Enum):
    ROM = auto()
    MBC1 = auto()
    MBC2 = auto()
    MBC3 = auto()
    MBC5 = auto()
    MBC6 = auto()
    MBC7 = auto()
    MMM01 = auto()

def get_mbc_type(value):
    if value in {0x00, 0x08, 0x09}:
        return MBCType.ROM
    elif value in {0x01, 0x02, 0x03}:
        return MBCType.MBC1
    elif value in {0x05, 0x06}:
        return MBCType.MBC2
    elif value in {0x0B, 0x0C, 0x0D}:
        return MBCType.MMM01
    elif value in {0x0F, 0x10, 0x11, 0x12, 0x13}:
        return MBCType.MBC3
    elif value in {0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E}:
        return MBCType.MBC5
    elif value == 0x20:
        return MBCType.MBC6
    elif value == 0x22:
        return MBCType.MBC7

RAM_CODES = {0x02, 0x03, 0x08, 0x09, 0x0C, 0x0D, 0x10, 0x12, 0x13, 0x1A, 0x1B, 0x1D, 0x1E, 0x22}
BATTERY_CODES = {0x03, 0x06, 0x09, 0x0D, 0x0F, 0x10, 0x13, 0x1B, 0x1E, 0x22}
TIMER_CODES = {0x0F, 0x10}
RUMBLE_CODES = {0x1C, 0x1D, 0x1E}

ROM_BANKS_CODES = {
    0x00: 2,
    0x01: 4,
    0x02: 8,
    0x03: 16,
    0x04: 32,
    0x05: 64,
    0x06: 128,
    0x07: 256,
    0x08: 512,
    0x52: 72,
    0x53: 80,
    0x54: 96,
}

RAM_SIZE_CODES = {
    0x00: 0,
    0x01: 2,
    0x02: 8,
    0x03: 32,
    0x04: 128,
    0x05: 64,
}

def bank_number_1_translator(number, mbc_type):
    if mbc_type == MBCType.MBC1:
        number &= 0b00011111
    elif mbc_type == MBCType.MBC2:
        number &= 0b00001111
    elif mbc_type == MBCType.MBC3:
        number &= 0b01111111
    if mbc_type != MBCType.MBC5 and number == 0:
        number += 1
    if mbc_type in {MBCType.MBC1, MBCType.MBC2} and number in {0x20, 0x40, 0x60}:
        number += 1
    return number

class Cartridge(object):

    def __init__(self, filename):
        data = bytearray(open(filename, 'rb').read())
        type = data[0x0147]
        rom_size = data[0x0148]
        ram_size = data[0x0149]

        self.mbc_type = get_mbc_type(type)
        self.ram = type in RAM_CODES
        self.battery = type in BATTERY_CODES
        self.timer = type in TIMER_CODES
        self.rumble = type in RUMBLE_CODES

        self.rom = [0x00 for i in range(ROM_BANKS_CODES[rom_size] * 0x4000)]
        self.ram = [0x00 for i in range(RAM_SIZE_CODES[ram_size] * 0x400)]

        self.rom[0:len(data)] = data

        self.ram_enable = 0x00
        self.bank_register_1 = 0x01
        self.bank_register_2 = 0x00
        self.rom_ram_mode = 0x00

    def __getitem__(self, addr):
        return self.read(addr)

    def __setitem__(self, addr, value):
        self.write(self, addr, value)

    def read(self, addr):
        if 0x0000 <= addr < 0x4000:
            return self.rom[addr]
        elif 0x4000 <= addr < 0x8000:
            return self.read_switchable_rom_bank(addr)
        elif 0xA000 <= addr < 0xC000:
            return self.read_ram(addr)

    def read_switchable_rom_bank(self, addr):
        read_addr = addr
        if self.mbc_type != MBCType.ROM:
            bank_number = self.bank_register_1
            if self.rom_ram_mode == 0x00:
                bank_number += self.bank_register_2 << 5
            else:
                read_addr += (bank_number << 4) + addr
        return self.rom[read_addr]

    def read_ram(self, addr):
        if self.rom_ram_mode:
            return self.ram[addr]
        else:
            return self.ram[self.bank_register_2 * 0x2000 + addr]

    def write(self, addr, value):
        if 0x0000 <= addr < 0x2000:
            self.ram_enable = 0b00001111 & value
        elif 0x2000 <= addr < 0x4000:
            self.bank_register_1 = bank_number_1_translator(value)
        elif 0x4000 <= addr < 0x6000:
            self.bank_register_2 = value
        elif 0x6000 <= addr < 0x8000:
            self.rom_ram_mode = value
        elif 0xA000 <= addr < 0xC000:
            self.write_ram(addr, value)

    def write_ram(self, addr, value):
        if self.rom_ram_mode:
            self.ram[addr] = value
        else:
            self.ram[self.bank_register_2 * 0x2000 + addr] = value