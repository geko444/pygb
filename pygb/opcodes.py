from pygb.cpu import CPU
from pygb.screen import Screen

count = 0

def do_next(cpu):
    opcode = cpu.pc()

    # 8-Bit Loads

    if opcode == 0x06:
        cpu.ld_nn_n('B', cpu.pc())
    elif opcode == 0x0E:
        cpu.ld_nn_n('C', cpu.pc())
    elif opcode == 0x16:
        cpu.ld_nn_n('D', cpu.pc())
    elif opcode == 0x1E:
        cpu.ld_nn_n('E', cpu.pc())
    elif opcode == 0x26:
        cpu.ld_nn_n('H', cpu.pc())
    elif opcode == 0x2E:
        cpu.ld_nn_n('L', cpu.pc())

    elif opcode == 0x7F:
        cpu.ld_r1_r2('A', 'A')
    elif opcode == 0x78:
        cpu.ld_r1_r2('A', 'B')
    elif opcode == 0x79:
        cpu.ld_r1_r2('A', 'C')
    elif opcode == 0x7A:
        cpu.ld_r1_r2('A', 'D')
    elif opcode == 0x7B:
        cpu.ld_r1_r2('A', 'E')
    elif opcode == 0x7C:
        cpu.ld_r1_r2('A', 'H')
    elif opcode == 0x7D:
        cpu.ld_r1_r2('A', 'L')
    elif opcode == 0x7E:
        cpu.ld_r1_r2('A', 'HL')
    elif opcode == 0x7E:
        cpu.ld_r1_r2('A', 'HL')
    elif opcode == 0x40:
        cpu.ld_r1_r2('B', 'B')
    elif opcode == 0x41:
        cpu.ld_r1_r2('B', 'C')
    elif opcode == 0x42:
        cpu.ld_r1_r2('B', 'D')
    elif opcode == 0x43:
        cpu.ld_r1_r2('B', 'E')
    elif opcode == 0x44:
        cpu.ld_r1_r2('B', 'H')
    elif opcode == 0x45:
        cpu.ld_r1_r2('B', 'L')
    elif opcode == 0x46:
        cpu.ld_r1_r2('B', 'HL')
    elif opcode == 0x48:
        cpu.ld_r1_r2('C', 'B')
    elif opcode == 0x49:
        cpu.ld_r1_r2('C', 'C')
    elif opcode == 0x4A:
        cpu.ld_r1_r2('C', 'D')
    elif opcode == 0x4B:
        cpu.ld_r1_r2('C', 'E')
    elif opcode == 0x4C:
        cpu.ld_r1_r2('C', 'H')
    elif opcode == 0x4D:
        cpu.ld_r1_r2('C', 'L')
    elif opcode == 0x4E:
        cpu.ld_r1_r2('C', 'HL')
    elif opcode == 0x50:
        cpu.ld_r1_r2('D', 'B')
    elif opcode == 0x51:
        cpu.ld_r1_r2('D', 'C')
    elif opcode == 0x52:
        cpu.ld_r1_r2('D', 'D')
    elif opcode == 0x53:
        cpu.ld_r1_r2('D', 'E')
    elif opcode == 0x54:
        cpu.ld_r1_r2('D', 'H')
    elif opcode == 0x55:
        cpu.ld_r1_r2('D', 'L')
    elif opcode == 0x56:
        cpu.ld_r1_r2('D', 'HL')
    elif opcode == 0x58:
        cpu.ld_r1_r2('E', 'B')
    elif opcode == 0x59:
        cpu.ld_r1_r2('E', 'C')
    elif opcode == 0x5A:
        cpu.ld_r1_r2('E', 'D')
    elif opcode == 0x5B:
        cpu.ld_r1_r2('E', 'E')
    elif opcode == 0x5C:
        cpu.ld_r1_r2('E', 'H')
    elif opcode == 0x5D:
        cpu.ld_r1_r2('E', 'L')
    elif opcode == 0x5E:
        cpu.ld_r1_r2('E', 'HL')
    elif opcode == 0x60:
        cpu.ld_r1_r2('H', 'B')
    elif opcode == 0x61:
        cpu.ld_r1_r2('H', 'C')
    elif opcode == 0x62:
        cpu.ld_r1_r2('H', 'D')
    elif opcode == 0x63:
        cpu.ld_r1_r2('H', 'E')
    elif opcode == 0x64:
        cpu.ld_r1_r2('H', 'H')
    elif opcode == 0x65:
        cpu.ld_r1_r2('H', 'L')
    elif opcode == 0x66:
        cpu.ld_r1_r2('H', 'HL')
    elif opcode == 0x68:
        cpu.ld_r1_r2('L', 'B')
    elif opcode == 0x69:
        cpu.ld_r1_r2('L', 'C')
    elif opcode == 0x6A:
        cpu.ld_r1_r2('L', 'D')
    elif opcode == 0x6B:
        cpu.ld_r1_r2('L', 'E')
    elif opcode == 0x6C:
        cpu.ld_r1_r2('L', 'H')
    elif opcode == 0x6D:
        cpu.ld_r1_r2('L', 'L')
    elif opcode == 0x6E:
        cpu.ld_r1_r2('L', 'HL')
    elif opcode == 0x70:
        cpu.ld_r1_r2('HL', 'B')
    elif opcode == 0x71:
        cpu.ld_r1_r2('HL', 'C')
    elif opcode == 0x72:
        cpu.ld_r1_r2('HL', 'D')
    elif opcode == 0x73:
        cpu.ld_r1_r2('HL', 'E')
    elif opcode == 0x74:
        cpu.ld_r1_r2('HL', 'H')
    elif opcode == 0x75:
        cpu.ld_r1_r2('HL', 'L')
    elif opcode == 0x36:
        cpu.ld_r1_r2('HL', cpu.pc())

    elif opcode == 0x7F:
        cpu.ld_a_n('A')
    elif opcode == 0x78:
        cpu.ld_a_n('B')
    elif opcode == 0x79:
        cpu.ld_a_n('C')
    elif opcode == 0x7A:
        cpu.ld_a_n('D')
    elif opcode == 0x7B:
        cpu.ld_a_n('E')
    elif opcode == 0x7C:
        cpu.ld_a_n('H')
    elif opcode == 0x7D:
        cpu.ld_a_n('L')
    elif opcode == 0x0A:
        cpu.ld_a_n('BC')
    elif opcode == 0x1A:
        cpu.ld_a_n('DE')
    elif opcode == 0x7E:
        cpu.ld_a_n('HL')
    elif opcode == 0xFA:
        cpu.ld_a_n(cpu.pc(2))
    elif opcode == 0x3E:
        cpu.ld_a_n(cpu.pc(), True)

    elif opcode == 0x7F:
        cpu.ld_n_a('A')
    elif opcode == 0x47:
        cpu.ld_n_a('B')
    elif opcode == 0x4F:
        cpu.ld_n_a('C')
    elif opcode == 0x57:
        cpu.ld_n_a('D')
    elif opcode == 0x5F:
        cpu.ld_n_a('E')
    elif opcode == 0x67:
        cpu.ld_n_a('H')
    elif opcode == 0x6F:
        cpu.ld_n_a('L')
    elif opcode == 0x02:
        cpu.ld_n_a('BC')
    elif opcode == 0x12:
        cpu.ld_n_a('DE')
    elif opcode == 0x77:
        cpu.ld_n_a('HL')
    elif opcode == 0xEA:
        cpu.ld_n_a(cpu.pc(2))

    elif opcode == 0xF2:
        cpu.ld_a_c()

    elif opcode == 0xE2:
        cpu.ld_c_a()

    elif opcode == 0x3A:
        cpu.ldd_a_hl()

    elif opcode == 0X32:
        cpu.ldd_hl_a()

    elif opcode == 0x2A:
        cpu.ldi_a_hl()

    elif opcode == 0x22:
        cpu.ldi_hl_a()

    elif opcode == 0xE0:
        cpu.ldh_n_a(cpu.pc())

    elif opcode == 0xF0:
        cpu.ldh_a_n(cpu.pc())

    # 16-Bit Loads

    elif opcode == 0x01:
        cpu.ld_n_nn(cpu.pc(2), 'BC')
    elif opcode == 0x11:
        cpu.ld_n_nn(cpu.pc(2), 'DE')
    elif opcode == 0x21:
        cpu.ld_n_nn(cpu.pc(2), 'HL')
    elif opcode == 0x31:
        cpu.ld_n_nn(cpu.pc(2), 'SP')

    elif opcode == 0xF9:
        cpu.ld_sp_hl()

    elif opcode == 0xF8:
        cpu.ldhl_sp_n(cpu.pc())

    elif opcode == 0x08:
        cpu.ld_nn_sp(cpu.pc(2))

    elif opcode == 0xF5:
        cpu.push_nn('AF')
    elif opcode == 0xC5:
        cpu.push_nn('BC')
    elif opcode == 0xD5:
        cpu.push_nn('DE')
    elif opcode == 0xE5:
        cpu.push_nn('HL')

    elif opcode == 0xF1:
        cpu.pop_nn('AF')
    elif opcode == 0xC1:
        cpu.pop_nn('BC')
    elif opcode == 0xD1:
        cpu.pop_nn('DE')
    elif opcode == 0xE1:
        cpu.pop_nn('HL')

    # 8-Bit ALU

    elif opcode == 0x87:
        cpu.add_a_n('A')
    elif opcode == 0x80:
        cpu.add_a_n('B')
    elif opcode == 0x81:
        cpu.add_a_n('C')
    elif opcode == 0x82:
        cpu.add_a_n('D')
    elif opcode == 0x83:
        cpu.add_a_n('E')
    elif opcode == 0x84:
        cpu.add_a_n('H')
    elif opcode == 0x85:
        cpu.add_a_n('L')
    elif opcode == 0x86:
        cpu.add_a_n('HL')
    elif opcode == 0xC6:
        cpu.add_a_n(cpu.pc())

    elif opcode == 0x8F:
        cpu.adc_a_n('A')
    elif opcode == 0x88:
        cpu.adc_a_n('B')
    elif opcode == 0x89:
        cpu.adc_a_n('C')
    elif opcode == 0x8A:
        cpu.adc_a_n('D')
    elif opcode == 0x8B:
        cpu.adc_a_n('E')
    elif opcode == 0x8C:
        cpu.adc_a_n('H')
    elif opcode == 0x8D:
        cpu.adc_a_n('L')
    elif opcode == 0x8E:
        cpu.adc_a_n('HL')
    elif opcode == 0xCE:
        cpu.adc_a_n(cpu.pc())

    elif opcode == 0x9F:
        cpu.xor_n('A')
    elif opcode == 0x98:
        cpu.xor_n('B')
    elif opcode == 0x99:
        cpu.xor_n('C')
    elif opcode == 0x9A:
        cpu.xor_n('D')
    elif opcode == 0x9B:
        cpu.xor_n('E')
    elif opcode == 0x9C:
        cpu.xor_n('H')
    elif opcode == 0x9D:
        cpu.xor_n('L')
    elif opcode == 0x9E:
        cpu.xor_n('HL')
    elif opcode == 0xBEEFCAFE:
        cpu.xor_n(cpu.pc())
        
    elif opcode == 0xA7:
        cpu.and_n('A')
    elif opcode == 0xA0:
        cpu.and_n('B')
    elif opcode == 0xA1:
        cpu.and_n('C')
    elif opcode == 0xA2:
        cpu.and_n('D')
    elif opcode == 0xA3:
        cpu.and_n('E')
    elif opcode == 0xA4:
        cpu.and_n('H')
    elif opcode == 0xA5:
        cpu.and_n('L')
    elif opcode == 0xA6:
        cpu.and_n('HL')
    elif opcode == 0xE6:
        cpu.and_n(cpu.pc())

    elif opcode == 0xB7:
        cpu.or_n('A')
    elif opcode == 0xB0:
        cpu.or_n('B')
    elif opcode == 0xB1:
        cpu.or_n('C')
    elif opcode == 0xB2:
        cpu.or_n('D')
    elif opcode == 0xB3:
        cpu.or_n('E')
    elif opcode == 0xB4:
        cpu.or_n('H')
    elif opcode == 0xB5:
        cpu.or_n('L')
    elif opcode == 0xB6:
        cpu.or_n('HL')
    elif opcode == 0xF6:
        cpu.or_n(cpu.pc())

    elif opcode == 0xAF:
        cpu.xor_n('A')
    elif opcode == 0xA8:
        cpu.xor_n('B')
    elif opcode == 0xA9:
        cpu.xor_n('C')
    elif opcode == 0xAA:
        cpu.xor_n('D')
    elif opcode == 0xAB:
        cpu.xor_n('E')
    elif opcode == 0xAC:
        cpu.xor_n('H')
    elif opcode == 0xAD:
        cpu.xor_n('L')
    elif opcode == 0xAE:
        cpu.xor_n('HL')
    elif opcode == 0xEE:
        cpu.xor_n(cpu.pc())

    elif opcode == 0xBF:
        cpu.cp_n('A')
    elif opcode == 0xB8:
        cpu.cp_n('B')
    elif opcode == 0xB9:
        cpu.cp_n('C')
    elif opcode == 0xBA:
        cpu.cp_n('D')
    elif opcode == 0xBB:
        cpu.cp_n('E')
    elif opcode == 0xBC:
        cpu.cp_n('H')
    elif opcode == 0xBD:
        cpu.cp_n('L')
    elif opcode == 0xBE:
        cpu.cp_n('HL')
    elif opcode == 0xFE:
        cpu.cp_n(cpu.pc())

    elif opcode == 0x3C:
        cpu.inc_n('A')
    elif opcode == 0x04:
        cpu.inc_n('B')
    elif opcode == 0x0C:
        cpu.inc_n('C')
    elif opcode == 0x14:
        cpu.inc_n('D')
    elif opcode == 0x1C:
        cpu.inc_n('E')
    elif opcode == 0x24:
        cpu.inc_n('H')
    elif opcode == 0x2C:
        cpu.inc_n('L')
    elif opcode == 0x34:
        cpu.inc_n('HL')
    
    elif opcode == 0x3D:
        cpu.dec_n('A')
    elif opcode == 0x05:
        cpu.dec_n('B')
    elif opcode == 0x0D:
        cpu.dec_n('C')
    elif opcode == 0x15:
        cpu.dec_n('D')
    elif opcode == 0x1D:
        cpu.dec_n('E')
    elif opcode == 0x25:
        cpu.dec_n('H')
    elif opcode == 0x2D:
        cpu.dec_n('L')
    elif opcode == 0x35:
        cpu.dec_n('HL')
    
    # 16-Bit Arithmetic

    elif opcode == 0x09:
        cpu.add_hl_n('BC')
    elif opcode == 0x19:
        cpu.add_hl_n('DE')
    elif opcode == 0x29:
        cpu.add_hl_n('HL')
    elif opcode == 0x39:
        cpu.add_hl_n('SP')

    elif opcode == 0xE8:
        cpu.add_sp_n(cpu.pc())

    elif opcode == 0x03:
        cpu.inc_nn('BC')
    elif opcode == 0x13:
        cpu.inc_nn('DE')
    elif opcode == 0x23:
        cpu.inc_nn('HL')
    elif opcode == 0x33:
        cpu.inc_nn('SP')

    elif opcode == 0x0B:
        cpu.dec_nn('BC')
    elif opcode == 0x1B:
        cpu.dec_nn('DE')
    elif opcode == 0x2B:
        cpu.dec_nn('HL')
    elif opcode == 0x3B:
        cpu.dec_nn('SP')

    # Miscellaneous

    elif opcode == 0xCB:
        op_2 = cpu.pc()
        if op_2 == 0x37:
            cpu.swap_n('A')
        elif op_2 == 0x30:
            cpu.swap_n('B')
        elif op_2 == 0x31:
            cpu.swap_n('C')
        elif op_2 == 0x32:
            cpu.swap_n('D')
        elif op_2 == 0x33:
            cpu.swap_n('E')
        elif op_2 == 0x34:
            cpu.swap_n('H')
        elif op_2 == 0x35:
            cpu.swap_n('L')
        elif op_2 == 0x36:
            cpu.swap_n('HL')

    elif opcode == 0x27:
        cpu.daa()

    elif opcode == 0x2F:
        cpu.cpl()

    elif opcode == 0x3F:
        cpu.ccf()

    elif opcode == 0x37:
        cpu.scf()

    elif opcode == 0x00:
        cpu.nop()

    elif opcode == 0x76:
        cpu.halt()

    elif opcode == 0x10:
        if cpu.pc() == 0x00:
            cpu.stop()

    elif opcode == 0xF3:
        cpu.di()

    elif opcode == 0xFB:
        cpu.ei()

    # Rotates & Shifts

    elif opcode == 0x07:
        cpu.rlca()

    elif opcode == 0x17:
        cpu.rla()

    elif opcode == 0x0F:
        cpu.rrca()

    elif opcode == 0x1F:
        cpu.rra()

    elif opcode == 0xCB:
        op_2 = cpu.pc()
        if op_2 == 0x07:
            cpu.rlc_n('A')
        elif op_2 == 0x00:
            cpu.rlc_n('B')
        elif op_2 == 0x01:
            cpu.rlc_n('C')
        elif op_2 == 0x02:
            cpu.rlc_n('D')
        elif op_2 == 0x03:
            cpu.rlc_n('E')
        elif op_2 == 0x04:
            cpu.rlc_n('H')
        elif op_2 == 0x05:
            cpu.rlc_n('L')
        elif op_2 == 0x06:
            cpu.rlc_n('HL')
        
        elif op_2 == 0x17:
            cpu.rl_n('A')
        elif op_2 == 0x10:
            cpu.rl_n('B')
        elif op_2 == 0x11:
            cpu.rl_n('C')
        elif op_2 == 0x12:
            cpu.rl_n('D')
        elif op_2 == 0x13:
            cpu.rl_n('E')
        elif op_2 == 0x14:
            cpu.rl_n('H')
        elif op_2 == 0x15:
            cpu.rl_n('L')
        elif op_2 == 0x16:
            cpu.rl_n('HL')

        elif op_2 == 0x0F:
            cpu.rrc_n('A')
        elif op_2 == 0x08:
            cpu.rrc_n('B')
        elif op_2 == 0x09:
            cpu.rrc_n('C')
        elif op_2 == 0x0A:
            cpu.rrc_n('D')
        elif op_2 == 0x0B:
            cpu.rrc_n('E')
        elif op_2 == 0x0C:
            cpu.rrc_n('H')
        elif op_2 == 0x0D:
            cpu.rrc_n('L')
        elif op_2 == 0x0E:
            cpu.rrc_n('HL')

        elif op_2 == 0x1F:
            cpu.rr_n('A')
        elif op_2 == 0x18:
            cpu.rr_n('B')
        elif op_2 == 0x19:
            cpu.rr_n('C')
        elif op_2 == 0x1A:
            cpu.rr_n('D')
        elif op_2 == 0x1B:
            cpu.rr_n('E')
        elif op_2 == 0x1C:
            cpu.rr_n('H')
        elif op_2 == 0x1D:
            cpu.rr_n('L')
        elif op_2 == 0x1E:
            cpu.rr_n('HL')

        elif op_2 == 0x27:
            cpu.sla_n('A')
        elif op_2 == 0x20:
            cpu.sla_n('B')
        elif op_2 == 0x21:
            cpu.sla_n('C')
        elif op_2 == 0x22:
            cpu.sla_n('D')
        elif op_2 == 0x23:
            cpu.sla_n('E')
        elif op_2 == 0x24:
            cpu.sla_n('H')
        elif op_2 == 0x25:
            cpu.sla_n('L')
        elif op_2 == 0x26:
            cpu.sla_n('HL')

        elif op_2 == 0x2F:
            cpu.sra_n('A')
        elif op_2 == 0x28:
            cpu.sra_n('B')
        elif op_2 == 0x29:
            cpu.sra_n('C')
        elif op_2 == 0x2A:
            cpu.sra_n('D')
        elif op_2 == 0x2B:
            cpu.sra_n('E')
        elif op_2 == 0x2C:
            cpu.sra_n('H')
        elif op_2 == 0x2D:
            cpu.sra_n('L')
        elif op_2 == 0x2E:
            cpu.sra_n('HL')

        elif op_2 == 0x3F:
            cpu.srl_n('A')
        elif op_2 == 0x38:
            cpu.srl_n('B')
        elif op_2 == 0x39:
            cpu.srl_n('C')
        elif op_2 == 0x3A:
            cpu.srl_n('D')
        elif op_2 == 0x3B:
            cpu.srl_n('E')
        elif op_2 == 0x3C:
            cpu.srl_n('H')
        elif op_2 == 0x3D:
            cpu.srl_n('L')
        elif op_2 == 0x3E:
            cpu.srl_n('HL')

        # Bit Opcodes

        elif op_2 == 0x47:
            cpu.bit_b_r(cpu.pc(), 'A')
        elif op_2 == 0x40:
            cpu.bit_b_r(cpu.pc(), 'B')
        elif op_2 == 0x41:
            cpu.bit_b_r(cpu.pc(), 'C')
        elif op_2 == 0x42:
            cpu.bit_b_r(cpu.pc(), 'D')
        elif op_2 == 0x43:
            cpu.bit_b_r(cpu.pc(), 'E')
        elif op_2 == 0x44:
            cpu.bit_b_r(cpu.pc(), 'H')
        elif op_2 == 0x45:
            cpu.bit_b_r(cpu.pc(), 'L')
        elif op_2 == 0x46:
            cpu.bit_b_r(cpu.pc(), 'HL')

        elif op_2 == 0xC7:
            cpu.set_b_r(cpu.pc(), 'A')
        elif op_2 == 0xC0:
            cpu.set_b_r(cpu.pc(), 'B')
        elif op_2 == 0xC1:
            cpu.set_b_r(cpu.pc(), 'C')
        elif op_2 == 0xC2:
            cpu.set_b_r(cpu.pc(), 'D')
        elif op_2 == 0xC3:
            cpu.set_b_r(cpu.pc(), 'E')
        elif op_2 == 0xC4:
            cpu.set_b_r(cpu.pc(), 'H')
        elif op_2 == 0xC5:
            cpu.set_b_r(cpu.pc(), 'L')
        elif op_2 == 0xC6:
            cpu.set_b_r(cpu.pc(), 'HL')

        elif op_2 == 0x87:
            cpu.res_b_r(cpu.pc(), 'A')
        elif op_2 == 0x80:
            cpu.res_b_r(cpu.pc(), 'B')
        elif op_2 == 0x81:
            cpu.res_b_r(cpu.pc(), 'C')
        elif op_2 == 0x82:
            cpu.res_b_r(cpu.pc(), 'D')
        elif op_2 == 0x83:
            cpu.res_b_r(cpu.pc(), 'E')
        elif op_2 == 0x84:
            cpu.res_b_r(cpu.pc(), 'H')
        elif op_2 == 0x85:
            cpu.res_b_r(cpu.pc(), 'L')
        elif op_2 == 0x86:
            cpu.res_b_r(cpu.pc(), 'HL')

    # Jumps

    elif opcode == 0xC3:
        cpu.jp_nn(cpu.pc(2))

    elif opcode == 0xC2:
        cpu.jp_cc_nn('NZ', cpu.pc(2))
    elif opcode == 0xCA:
        cpu.jp_cc_nn('Z', cpu.pc(2))
    elif opcode == 0xD2:
        cpu.jp_cc_nn('NC', cpu.pc(2))
    elif opcode == 0xDA:
        cpu.jp_cc_nn('C', cpu.pc(2))

    elif opcode == 0xE9:
        cpu.jp_hl()

    elif opcode == 0x18:
        cpu.jr_n(cpu.pc())

    elif opcode == 0x20:
        cpu.jr_cc_n('NZ', cpu.pc())
    elif opcode == 0x28:
        cpu.jr_cc_n('Z', cpu.pc())
    elif opcode == 0x30:
        cpu.jr_cc_n('NC', cpu.pc())
    elif opcode == 0x38:
        cpu.jr_cc_n('C', cpu.pc())

    # Calls

    elif opcode == 0xCD:
        cpu.call_nn(cpu.pc(2))

    elif opcode == 0xC4:
        cpu.call_cc_nn('NZ', cpu.pc(2))
    elif opcode == 0xCC:
        cpu.call_cc_nn('Z', cpu.pc(2))
    elif opcode == 0xD4:
        cpu.call_cc_nn('NC', cpu.pc(2))
    elif opcode == 0xDC:
        cpu.call_cc_nn('C', cpu.pc(2))

    # Restarts

    elif opcode == 0xC7:
        cpu.rst_n(0x00)
    elif opcode == 0xCF:
        cpu.rst_n(0x08)
    elif opcode == 0xD7:
        cpu.rst_n(0x10)
    elif opcode == 0xDF:
        cpu.rst_n(0x18)
    elif opcode == 0xE7:
        cpu.rst_n(0x20)
    elif opcode == 0xEF:
        cpu.rst_n(0x28)
    elif opcode == 0xF7:
        cpu.rst_n(0x30)
    elif opcode == 0xFF:
        cpu.rst_n(0x38)

    # Returns

    elif opcode == 0xC9:
        cpu.ret()

    elif opcode == 0xC0:
        cpu.ret_cc('NZ')
    elif opcode == 0xC8:
        cpu.ret_cc('Z')
    elif opcode == 0xD0:
        cpu.ret_cc('NC')
    elif opcode == 0xD8:
        cpu.ret_cc('C')

    elif opcode == 0xD9:
        cpu.reti()


def print_registers(registers):
    to_print = ''
    for key in registers.keys():
        to_print += '\'%s\': %s  ' % (key, hex(registers[key]))
    return to_print

draw = False
cpu = CPU('/home/geko/gb-test-roms/cpu_instrs/individual/01-special.gb')

if draw:
    screen = Screen(cpu.memory)

while cpu.registers.PC <= 0x100:
    # print(cpu.registers.registers)
    print(
        count,
        hex(cpu.registers.PC),
        hex(cpu.memory[cpu.registers.PC]),
        hex(cpu.registers.SP),
        hex(cpu.memory[cpu.registers.SP] + (cpu.memory[cpu.registers.SP+1] << 8)),
        '-',
        print_registers(cpu.registers.registers)
    )
    do_next(cpu)
    count += 1
    if draw:
        screen.draw_sprites()

while draw:
    pass

print('boo')