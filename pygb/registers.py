class Registers(object):
    def __init__(self):
        self.__dict__['registers'] = {
            'A': 0x0,
            'F': 0x0,
            'B': 0x0,
            'C': 0x0,
            'D': 0x0,
            'E': 0x0,
            'H': 0x0,
            'L': 0x0,
            'SP': 0x0,
            'PC': 0x0
        }

    def get(self, reg):
        if len(reg) == 1 or reg in self.registers:
            return self.registers[reg]
        else:
            return (self.registers[reg[0]] << 8) + self.registers[reg[1]]

    def set(self, reg, val):
        if len(reg) == 1 or reg in self.registers:
            self.registers[reg] = val
        else:
            self.registers[reg[0]] = val >> 8
            self.registers[reg[1]] = val & ((1 << 8) - 1)

    def __getattr__(self, name):
        if len(name) == 1 or name in self.registers:
            return self.registers[name]
        elif name[0] == '_':
            if name[1] == 'Z':
                return (self.registers['F'] >> 7) & 1
            elif name[1] == 'N':
                return (self.registers['F'] >> 6) & 1
            elif name[1] == 'H':
                return (self.registers['F'] >> 5) & 1
            elif name[1] == 'C':
                return (self.registers['F'] >> 4) & 1
            else:
                return 0
        else:
            return (self.registers[name[0]] << 8) + self.registers[name[1]]

    def __setattr__(self, name, value):
        if len(name) == 1 or name in self.registers:
            if len(name) == 1:
                value &= 0xFF
            else:
                value &= 0xFFFF
            self.registers[name] = value
        elif name[0] == '_':
            value &= 0xFF
            if name[1] == 'Z':
                self.registers['F'] |= (value << 7)
            elif name[1] == 'N':
                self.registers['F'] |= (value << 6)
            elif name[1] == 'H':
                self.registers['F'] |= (value << 5)
            elif name[1] == 'C':
                self.registers['F'] |= (value << 4)
        else:
            value &= 0xFFFF
            self.registers[name[0]] = value >> 8
            self.registers[name[1]] = value & ((1 << 8) - 1)

    def __getitem__(self, name):
        return self.__getattr__(name)

    def __setitem__(self, name, value):
        self.__setattr__(name, value)
