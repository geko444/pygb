screen = Screen("")

smile1 = [
  0x0F,0x0F,0x30,0x30,0x40,0x40,0x40,0x40,
  0x84,0x84,0x84,0x84,0x84,0x84,0x84,0x84,
  0x84,0x84,0x84,0x84,0x80,0x80,0x80,0x80,
  0x44,0x44,0x43,0x43,0x30,0x30,0x0F,0x0F
]
smile2 = [
    0xF0,0xF0,0x0C,0x0C,0x02,0x02,0x02,0x02,
    0x21,0x21,0x21,0x21,0x21,0x21,0x21,0x21,
    0x21,0x21,0x21,0x21,0x01,0x01,0x01,0x01,
    0x22,0x22,0xC2,0xC2,0x0C,0x0C,0xF0,0xF0
]
smile3 = [
    0x0F,0x0F,0x30,0x30,0x40,0x40,0x40,0x40,
    0x84,0x84,0x84,0x84,0x84,0x84,0x84,0x84,
    0x84,0x84,0x84,0x84,0x80,0x80,0x80,0x80,
    0x44,0x44,0x43,0x43,0x30,0x30,0x0F,0x0F
]
smile4 = [
    0xF0,0xF0,0x0C,0x0C,0x02,0x02,0x02,0x02,
    0x01,0x01,0x01,0x01,0x01,0x01,0xF9,0xF9,
    0x01,0x01,0x01,0x01,0x01,0x01,0x01,0x01,
    0x22,0x22,0xC2,0xC2,0x0C,0x0C,0xF0,0xF0
]

screen.draw_tile(20, 20, screen.get_tile_pixels(smile1))
screen.draw_tile(28, 20, screen.get_tile_pixels(smile2))
screen.draw_tile(20, 36, screen.get_tile_pixels(smile3))
screen.draw_tile(28, 36, screen.get_tile_pixels(smile4))
pygame.display.update()