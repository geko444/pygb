import pygame

LCDC_ADDRESS = 0xFF40

COLOUR_0 = (0xFF, 0xFF, 0xFF)
COLOUR_1 = (0xAA, 0xAA, 0xAA)
COLOUR_2 = (0x66, 0x66, 0x66)
COLOUR_3 = (0x00, 0x00, 0x00)

colour_map = {
    0: COLOUR_0,
    1: COLOUR_1,
    2: COLOUR_2,
    3: COLOUR_3
}

class Screen(object):
    def __init__(self, memory):
        self.memory = memory
        pygame.init()
        self.screen = pygame.display.set_mode((160*4, 144*4))
        self.screen.fill(COLOUR_0)
        pygame.display.update()

    def lcdc(self):
        lcdc = LDCD(self.memory[LCDC_ADDRESS])

    def get_tile_pixels(self, tile_data):
        tile_pixels = []
        for i in range(0, len(tile_data), 2):
            tile_pixels.append(self.get_line_pixels(tile_data[i], tile_data[i+1]))
        return tile_pixels

    def get_line_pixels(self, byte1, byte2):
        line_pixels = []
        for i in range(7, -1, -1):
            msb = (byte1 >> i) & 1
            lsb = (byte2 >> i) & 1
            line_pixels.append((msb << 1) + lsb)
        return line_pixels

    def draw_tile(self, xpos, ypos, pixels):
        xpos = xpos * 4 - 8
        ypos = ypos * 4 - 16
        for j in range(len(pixels)):
            for i in range(len(pixels[j])):
                pygame.draw.rect(self.screen, colour_map[pixels[j][i]], pygame.Rect(xpos + i*4, ypos + j*4, 4, 4))

    def draw_sprite(self, sprite_data):
        tile_start = 0x8000 + sprite_data[2] << 4
        self.draw_tile(sprite_data[1], sprite_data[0], self.get_tile_pixels(self.memory[tile_start:tile_start+16]))

    def draw_sprites(self):
        self.screen.fill(COLOUR_0)
        for i in range(0xFE00, 0xFF00, 4):
            self.draw_sprite(self.memory[i:i+4])
        pygame.display.update()



class LDCD(object):
    def __init__(self, value):
        set(value)

    def set(self, value):
        self.value = value

        self.lcd_enable = value & (1 << 7)
        self.window_tile_map_display_select = value & (1 << 6)
        self.window_display_enable = value & (1 << 5)
        self.bg_window_tile_data_select = value & (1 << 4)
        self.bg_tile_map_display_select = value & (1 << 3)
        self.obj_size = value & (1 << 2)
        self.obj_display_enable = value & (1 << 1)
        self.lcd_enable = value & (1 << 0)


# screen = Screen("")
#
# smile1 = [
#   0x0F,0x0F,0x30,0x30,0x40,0x40,0x40,0x40,
#   0x84,0x84,0x84,0x84,0x84,0x84,0x84,0x84,
#   0x84,0x84,0x84,0x84,0x80,0x80,0x80,0x80,
#   0x44,0x44,0x43,0x43,0x30,0x30,0x0F,0x0F
# ]
# smile2 = [
#     0xF0,0xF0,0x0C,0x0C,0x02,0x02,0x02,0x02,
#     0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21,
#     0x21,0x21,0x21,0x21,0x01,0x01,0x01,0x01,
#     0x22,0x22,0xC2,0xC2,0x0C,0x0C,0xF0,0xF0
# ]
# smile3 = [
#     0x0F,0x0F,0x30,0x30,0x40,0x40,0x40,0x40,
#     0x84,0x84,0x84,0x84,0x84,0x84,0x84,0x84,
#     0x84,0x84,0x84,0x84,0x80,0x80,0x80,0x80,
#     0x44,0x44,0x43,0x43,0x30,0x30,0x0F,0x0F
# ]
# smile4 = [
#     0xF0,0xF0,0x0C,0x0C,0x02,0x02,0x02,0x02,
#     0x01,0x01,0x01,0x01,0x01,0x01,0xF9,0xF9,
#     0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,
#     0x22,0x22,0xC2,0xC2,0x0C,0x0C,0xF0,0xF0
# ]
#
# screen.draw_tile(20, 20, screen.get_tile_pixels(smile1))
# screen.draw_tile(28, 20, screen.get_tile_pixels(smile2))
# screen.draw_tile(20, 36, screen.get_tile_pixels(smile3))
# screen.draw_tile(28, 36, screen.get_tile_pixels(smile4))
# pygame.display.update()
#
# while True:
#     pass