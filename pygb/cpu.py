from pygb.memory import Memory
from pygb.registers import Registers


def half_carry(a, b, c=0):
    return 1 if (((a & 0xF) + (b & 0xF) + c) & 0x10) == 0x10 else 0

def half_carry_16(a, b, c=0):
    return 1 if (((a & 0xFFF) + (b & 0xFFF) + c) & 0x1000) == 0x1000 else 0

def carry(a, b, c=0):
    return 1 if (((a & 0xFF) + (b & 0xFF) + c) & 0x100) == 0x100 else 0

def carry_16(a, b, c=0):
    return 1 if (((a & 0xFFFF) + (b & 0xFFFF) + c) & 0x10000) == 0x10000 else 0

def half_borrow(a, b, c=0):
    return 0 if (a & 0xF) < (b & 0xF + c) else 1

def half_borrow_16(a, b, c=0):
    return 0 if (a & 0xFFF) < (b & 0xFFF + c) else 1

def borrow(a, b, c=0):
    return 0 if (a & 0xFF) < (b & 0xFF + c) else 1

def borrow_16(a, b, c=0):
    return 0 if (a & 0xFFFF) < (b & 0xFFFF + c) else 1

def get_nibbles(n):
    return n >> 4, n & 0xF

def combine_nibbles(n1, n2):
    return n1 << 4 + n2

def signed(n):
    if n >> 7 == 1:
        return -~(n & 0x7F) - 1
    return n

class CPU(object):

    def __init__(self, filename):
        self.counter = 0
        self.memory = Memory(filename)
        self.registers = Registers()

    def tick(self, n):
        self.counter += 0

    def pc(self, bytes=1):
        value = 0
        if bytes == 1:
            value = self.memory[self.registers.PC]
        elif bytes == 2:
            values = self.memory[self.registers.PC:self.registers.PC+2]
            value = (values[1] << 8) + values[0]
        self.registers.PC += bytes
        return value

    # 8-Bit Loads

    def ld_nn_n(self, nn, n):
        self.memory[self.registers[nn]] = n
        self.tick(8)

    def ld_r1_r2(self, r1, r2):
        tick = 4
        if r1 == 'HL' or r2 == 'HL':
            tick += 4
        if isinstance(r2, str):
            self.registers[r1] = self.registers[r2]
        else:
            self.memory[r2] = self.registers[r1]
            tick += 4
        self.tick(tick)

    def ld_a_n(self, n, mem=False):
        tick = 4
        if not isinstance(n, str):
            if mem:
                self.registers.A = self.memory[n]
                tick += 4
            else:
                self.registers.A = n
                tick += 12
        else:
            if len(n) == 2:
                tick += 4
            self.registers.A = self.registers[n]
        self.tick(tick)

    def ld_n_a(self, n):
        tick = 4
        if not isinstance(n, str):
            n = self.registers.A
            tick += 12
        else:
            if len(n) == 2:
                tick += 4
            self.registers[n] = self.registers.A
        self.tick(tick)

    def ld_a_c(self):
        self.registers.A = self.memory[0xFF00 + self.registers.C]
        self.tick(8)

    def ld_c_a(self):
        self.memory[0xFF00 + self.registers.C] = self.registers.A
        self.tick(8)

    def ldd_a_hl(self):
        self.registers.A = self.memory[self.registers.HL]
        self.registers.HL -= 1
        self.tick(8)

    def ldd_hl_a(self):
        self.memory[self.registers.HL] = self.registers.A
        self.registers.HL -= 1
        self.tick(8)

    def ldi_a_hl(self):
        self.registers.A = self.memory[self.registers.HL]
        self.registers.HL += 1
        self.tick(8)

    def ldi_hl_a(self):
        self.memory[self.registers.HL] = self.registers.A
        self.registers.HL += 1
        self.tick(8)

    def ldh_n_a(self, n):
        self.registers.A = self.memory[0xFF00 + n]
        self.tick(12)

    def ldh_a_n(self, n):
        self.memory[0xFF00 + n] = self.registers.A
        self.tick(12)

    # 16-Bit Loads

    def ld_n_nn(self, nn, n):
        self.registers[n] = nn
        self.tick(12)

    def ld_sp_hl(self):
        self.registers.SP = self.registers.HL
        self.tick(8)

    def ldhl_sp_n(self, n):
        self.registers.HL = self.registers.SP + n
        self.registers._Z = 0
        self.registers._N = 0
        self.registers._H = half_carry(self.registers.SP, n)
        self.registers._C = carry(self.registers.SP, n)
        self.tick(12)

    def ld_nn_sp(self, nn):
        self.registers.SP = nn
        self.tick(20)

    def push_nn(self, nn):
        self.registers.SP -= 2
        self.memory[self.registers.SP] = self.registers[nn]
        self.tick(16)

    def pop_nn(self, nn):
        self.registers[nn] = self.memory[self.registers.SP]
        self.registers.SP += 2
        self.tick(16)

    # 8-Bit ALU

    def add_a_n(self, n):
        tick = 4
        if not isinstance(n, str):
            additive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            additive = self.registers[n]
        result = self.registers.A + additive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = half_carry(self.registers.A, additive)
        self.registers._C = carry(self.registers.A, additive)
        self.registers.A = result
        self.tick(tick)

    def adc_a_n(self, n):
        tick = 4
        if not isinstance(n, str):
            additive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            additive = self.registers[n]
        result = self.registers.A + self.registers._C + additive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = half_carry(self.registers.A, additive, self.registers._C)
        self.registers._C = carry(self.registers.A, additive, self.registers._C)
        self.registers.A = result
        self.tick(tick)

    def sub_a_n(self, n):
        tick = 4
        if not isinstance(n, str):
            subtractive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            subtractive = self.registers[n]
        result = self.registers.A - subtractive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = half_borrow(self.registers.A, subtractive)
        self.registers._C = borrow(self.registers.A, subtractive)
        self.registers.A = result
        self.tick(tick)

    def sbc_a_n(self, n):
        tick = 4
        if not isinstance(n, str):
            subtractive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            subtractive = self.registers[n]
        result = self.registers.A + (subtractive + self.registers._C)
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = half_carry(self.registers.A, subtractive, self.registers._C)
        self.registers._C = carry(self.registers.A, subtractive, self.registers._C)
        self.registers.A = result
        self.tick(tick)

    def and_n(self, n):
        tick = 4
        if not isinstance(n, str):
            anditive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            anditive = self.registers[n]
        result = self.registers.A & anditive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = 1
        self.registers._C = 0
        self.registers.A = result
        self.tick(tick)

    def or_n(self, n):
        tick = 4
        if not isinstance(n, str):
            oritive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            oritive = self.registers[n]
        result = self.registers.A | oritive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = 0
        self.registers._C = 0
        self.registers.A = result
        self.tick(tick)

    def xor_n(self, n):
        tick = 4
        if not isinstance(n, str):
            xoritive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            xoritive = self.registers[n]
        result = self.registers.A ^ xoritive
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers._H = 0
        self.registers._C = 0
        self.registers.A = result
        self.tick(tick)

    def cp_n(self, n):
        tick = 4
        if not isinstance(n, str):
            comparitive = self.memory[n]
            tick += 4
        else:
            if len(n) == 2:
                tick += 4
            comparitive = self.registers[n]
        self.registers._Z = self.registers.A == comparitive
        self.registers._N = 1
        self.registers._H = half_borrow(self.registers.A, comparitive)
        self.registers._C = borrow(self.registers.A, comparitive)
        self.tick(tick)

    def inc_n(self, n):
        tick = 4
        if len(n) == 2:
            tick += 8
            result = (self.registers[n] + 1) % 0xFFFF
            self.registers._H = half_carry(self.registers[n[1]], 1)
        else:
            result = (self.registers[n] + 1) % 0xFF
            self.registers._H = half_carry(self.registers[n], 1)
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers[n] = result
        self.tick(tick)

    def dec_n(self, n):
        tick = 4
        if len(n) == 2:
            tick += 8
            result = 0 if self.registers[n] == 0 else (self.registers[n] - 1) & 0xFFFF
            self.registers._H = half_borrow(self.registers[n[1]], 1)
        else:
            result = 0 if self.registers[n] == 0 else (self.registers[n] - 1) & 0xFF
            self.registers._H = half_borrow(self.registers[n], 1)
        self.registers._Z = result == 0
        self.registers._N = 0
        self.registers[n] = result
        self.tick(tick)

    # 16-Bit ALU

    def add_hl_n(self, n):
        additive = self.registers[n]
        self.registers._H = half_carry_16(self.registers.HL, additive)
        self.registers._C = carry_16(self.registers.HL, additive)
        self.registers._N = 0
        self.registers.HL = (self.registers.HL + self.registers[n]) % 0x10000
        self.tick(8)

    def add_sp_n(self, n):
        self.registers._Z = 0
        self.registers._N = 0
        self.registers._H = half_carry_16(self.registers.HL, n)
        self.registers._C = carry_16(self.registers.HL, n)
        self.registers.HL = (self.registers.HL + n) % 0x10000
        self.tick(16)

    def inc_nn(self, nn):
        self.registers[nn] = (self.registers[nn] + 1) % 0x10000
        self.tick(8)

    def dec_nn(self, nn):
        self.registers[nn] = (self.registers[nn] - 1) % 0x10000
        self.tick(8)

    # Miscellaneous

    def swap_n(self, n):
        tick = 8
        if len(n) == 1:
            n1, n2 = get_nibbles(self.registers[n])
            self.registers[n] = combine_nibbles(n2, n1)
        elif len(n) == 2:
            n1, n2 = get_nibbles(self.registers[n[0]])
            n3, n4 = get_nibbles(self.registers[n[1]])
            self.registers[n[0]] = combine_nibbles(n4, n1)
            self.registers[n[1]] = combine_nibbles(n2, n3)
            tick += 8
        self.registers._Z = self.registers[n] == 0
        self.registers._N = 0
        self.registers._H = 0
        self.registers._C = 0
        self.tick(tick)

    def daa(self):
        if self.registers.A > 0x64:
            self.registers.A %= 0x64
            self.registers._C = 0
        else:
            self.registers._C = 1
        self.registers._Z = self.registers.A == 0
        self.registers._H = 0
        units = self.registers.A % 0xA
        tens = (self.registers.A - units) / 0xA
        self.registers.A = combine_nibbles(tens, units)
        self.tick(8)

    def cpl(self):
        self.registers.A = ~self.registers.A
        self.registers._N = self.registers.A >> 7
        self.registers._H = (self.registers.A & 0xF) >> 4
        self.tick(4)

    def ccf(self):
        self.registers._N = 0
        self.registers._H = 0
        self.registers._C = ~self.registers._C
        self.tick(4)

    def scf(self):
        self.registers._N = 0
        self.registers._H = 0
        self.registers._C = 1
        self.tick(4)

    def nop(self):
        self.tick(4)

    def halt(self):
        # TODO: Implement interrupt and wait
        self.tick(4)

    def stop(self):
        # TODO: Implement button press and wait
        self.tick(4)

    def di(self):
        # TODO: Implement the ability to disable interrupts at next instruction
        self.tick(4)

    def ei(self):
        # TODO: Implement the ability to enable interrupts at next instruction
        self.tick(4)

    # Rotates and shifts

    def rlca(self):
        bit7 = self.registers.A >> 7
        self.registers.A = (self.registers.A << 1) % 0x100 + bit7
        self.registers._C = bit7
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers.A == 0
        self.tick(4)

    def rla(self):
        bit7 = self.registers.A >> 7
        self.registers.A = (self.registers.A << 1) % 0x100 + self.registers._C
        self.registers._C = bit7
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers.A == 0
        self.tick(4)

    def rrca(self):
        bit0 = self.registers.A % 2
        self.registers.A = (self.registers.A >> 1) + bit0 << 7
        self.registers._C = bit0
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers.A == 0
        self.tick(4)

    def rra(self):
        bit0 = self.registers.A % 2
        self.registers.A = (self.registers.A >> 1) + self.registers._C << 7
        self.registers._C = bit0
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers.A == 0
        self.tick(4)

    def rlc_n(self, n):
        tick = 8
        rnum = 7
        modnum = 0x100
        if len(n) == 2:
            tick += 8
            rnum = 15
            modnum = 0x100 ** 2
        bitC = self.registers[n] >> rnum
        self.registers._C = bitC
        self.registers[n] = (self.registers[n] << 1) % modnum + bitC
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def rl_n(self, n):
        tick = 8
        rnum = 7
        modnum = 0x100
        if len(n) == 2:
            tick += 8
            rnum = 15
            modnum = 0x100 ** 2
        bitC = self.registers[n] >> rnum
        self.registers[n] = (self.registers[n] << 1) % modnum + self.registers._C
        self.registers._C = bitC
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def rrc_n(self, n):
        tick = 8
        lnum = 7
        if len(n) == 2:
            tick += 8
            lnum = 15
        bitC = self.registers[n] % 2
        self.registers._C = bitC
        self.registers[n] = (self.registers[n] >> 1) + bitC << lnum
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def rr_n(self, n):
        tick = 8
        lnum = 7
        if len(n) == 2:
            tick += 8
            lnum = 15
        bitC = self.registers[n] % 2
        self.registers[n] = (self.registers[n] >> 1) + self.registers._C << lnum
        self.registers._C = bitC
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def sla_n(self, n):
        tick = 8
        rnum = 7
        modnum = 0x100
        if len(n) == 2:
            tick += 8
            rnum = 15
            modnum = 0x100 ** 2
        self.registers._C = self.registers[n] >> rnum
        self.registers[n] = (self.registers[n] << 1) % modnum
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def sra_n(self, n):
        tick = 8
        andnum = 0x80
        if len(n) == 2:
            tick += 8
            andnum = 0x8000
        self.registers._C = self.registers[n] % 2
        self.registers[n] = (self.registers[n] >> 1) + (self.registers[n] & andnum)
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    def srl_n(self, n):
        tick = 8
        if len(n) == 2:
            tick += 8
        self.registers._C = self.registers[n] % 2
        self.registers[n] = self.registers[n] >> 1
        self.registers._N = 0
        self.registers._H = 0
        self.registers._Z = self.registers[n] == 0
        self.tick(tick)

    # Bit Opcodes

    def bit_b_r(self, b, r):
        tick = 8
        if len(r) == 2:
            tick += 8
        self.registers._Z = ((self.registers[r] >> b) & 1) == 0
        self.registers._N = 0
        self.registers._H = 1
        self.tick(tick)

    def set_b_r(self, b, r):
        tick = 8
        if len(r) == 2:
            tick += 8
        self.registers[r] |= (1 << b)
        self.tick(tick)

    def res_b_r(self, b, r):
        tick = 8
        if len(r) == 2:
            tick += 8
        self.registers[r] &= (2 ** tick - 1 - 1 << b)
        self.tick(tick)

    # Jumps

    def jp_nn(self, nn):
        self.registers.PC = (nn << 8) & 0xFFFF + (nn >> 8) - 2
        self.tick(12)

    def jp_cc_nn(self, cc, nn):
        flag = "_" + cc
        comparitive = 1
        if len(cc) == 2:
            flag = "_" + cc[1]
            comparitive = 0
        if self.registers[flag] == comparitive:
            self.registers.PC = (nn << 8) & 0xFFFF + (nn >> 8) - 2
        self.tick(12)

    def jp_hl(self):
        self.registers.PC = self.registers.HL - 2
        self.tick(4)

    def jr_n(self, n):
        self.registers.PC += signed(n)
        self.tick(8)

    def jr_cc_n(self, cc, n):
        flag = "_" + cc
        comparitive = 1
        if len(cc) == 2:
            flag = "_" + cc[1]
            comparitive = 0
        if self.registers[flag] == comparitive:
            self.registers.PC += signed(n)
        self.tick(8)

    # Calls

    def call_nn(self, nn):
        self.registers.SP -= 2
        self.memory[self.registers.SP] = self.registers.PC & 0xFF
        self.memory[self.registers.SP+1] = self.registers.PC >> 8
        self.registers.PC = nn
        self.tick(12)

    def call_cc_nn(self, cc, nn):
        flag = "_" + cc
        comparitive = 1
        if len(cc) == 2:
            flag = "_" + cc[1]
            comparitive = 0
        if self.registers[flag] == comparitive:
            self.memory[self.registers.SP] = self.registers.PC + 2
            self.registers.PC = nn
        self.tick(12)

    # Restarts

    def rst_n(self, n):
        self.registers.SP = self.registers.PC
        self.registers.PC = n - 2
        self.tick(32)

    # Returns

    def ret(self):
        nn = self.memory[self.registers.SP:self.registers.SP+2]
        self.registers.PC = (nn[1] << 8) + nn[0]
        self.memory[self.registers.SP] = 0
        self.memory[self.registers.SP+1] = 0
        self.registers.SP += 2
        self.tick(8)

    def ret_cc(self, cc):
        flag = "_" + cc
        comparitive = 1
        if len(cc) == 2:
            flag = "_" + cc[1]
            comparitive = 0
        if self.registers[flag] == comparitive:
            self.registers.PC = self.memory[self.registers.SP] - 2
            self.memory[self.registers.SP] = 0
        self.tick(8)

    def reti(self):
        self.registers.PC = self.memory[self.registers.SP] - 2
        self.memory[self.registers.SP] = 0
        # TODO: Enable interrupts
        self.tick(8)

