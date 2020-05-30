import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306


class DisplayController:
    def __init__(self, address):
        if address is None:
            raise Exception("None address")

        displayio.release_displays()
        self.i2c = board.I2C()
        display_bus = displayio.I2CDisplay(i2c, device_address=address)
        self.WIDTH = 128
        self.HEIGHT = 32  # Change to 64 if needed
        self.BORDER = 5
        self.display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=self.WIDTH, height=self.HEIGHT)
        self.splash = displayio.Group(max_size=10)
        self.display.show(self.splash)

        color_bitmap = displayio.Bitmap(self.WIDTH, self.HEIGHT, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self.splash.append(bg_sprite)

    def write_text(self, text_to_write):
        text_area = label.Label(
            terminalio.FONT, text=text_to_write, color=0xFFFFFF, x=28, y=self.HEIGHT // 2 - 1
        )
        self.splash.append(text_area)
