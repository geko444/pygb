from pygb.cartridge import Cartridge

ROM_FILE_NAME = 'DMG_ROM.bin'

def unmirror(addr):
    if 0xE000 <= addr <= 0xFDFF:
        return addr - 0x2000
    else:
        return addr

def is_echo_addr(addr):
    return 0xE000 <= addr <= 0xFDFF

def unmirror_slice(sl):
    return [unmirror(addr) for addr in slice_to_range(sl)]

def slice_to_range(sl):
    if sl.step == None:
        if sl.start == None:
            return range(sl.stop)
        else:
            return range(sl.start, sl.stop)
    else:
        return range(sl.start, sl.stop, sl.step)

class Memory(object):
    def __init__(self, filename):
        self.__dict__['map'] = [0x0 for i in range(0x10000)]
        self.cartridge = Cartridge(filename)
        self.set_boot_rom()

    def set_boot_rom(self):
        rom_ba = bytearray(open(ROM_FILE_NAME, 'rb').read())
        self.map[0:len(rom_ba)] = rom_ba

    def __getitem__(self, addr):
        if type(addr) is slice:
            if is_echo_addr(addr.start) or is_echo_addr(addr.stop):
                return self.get_echo_slice(addr)
            else:
                return self.map[addr]
        elif 0x0000 <= addr <= 0x7FFF:
            if addr < 0x0100 and self.map[0xFF50] == 0:
                return self.map[addr]
            return self.cartridge[addr]
        elif 0xA000 <= addr <= 0xC000:
            return self.cartridge[addr]
        elif 0xE000 <= addr <= 0xFDFF:
            return self.get_echo(addr)
        else:
            return self.map[addr]

    def __setitem__(self, addr, value):
        if type(addr) is slice:
            if is_echo_addr(addr.start) or is_echo_addr(addr.stop):
                self.set_echo_slice(addr, value)
            else:
                self.map[addr] = value
        elif is_echo_addr(addr):
            self.set_echo(addr, value)
        else:
            self.map[addr] = value

    def get_echo(self, addr):
        return self.map[unmirror(addr)]

    def set_echo(self, addr, value):
        self.map[unmirror(addr)] = value

    def get_echo_slice(self, sl):
        return [self.map[addr] for addr in unmirror_slice(sl)]

    def set_echo_slice(self, sl, vals):
        rg = unmirror_slice(sl)
        for i in range(len(vals)):
            self.map[rg[i]] = vals[i]
