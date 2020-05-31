import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class DisplayController:
    #https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/blob/master/examples/ssd1306_pillow_demo.py
    def __init__(self, address=0x3C, reset_pin=board.D4, border=5):
        self.oled_reset = digitalio.DigitalInOut(reset_pin)
        WIDTH = 128
        HEIGHT = 32
        self.BORDER = border
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=address, reset=self.oled_reset)
        self.clear_display()
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)


    def write_text(self, text_to_write, fill=255):
        font = ImageFont.load_default()
        (font_width, font_height) = font.getsize(text_to_write)
        self.draw.text((self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
            text_to_write,
            font=font,
            fill=fill,
        )

    def draw_rectangle(self):
        self.draw.rectangle((self.BORDER,self.BORDER, self.oled.width - self.BORDER - 1,
                            self.oled.height - self.BORDER - 1),
                            outline=0, fill=0)

    def draw_background(self, fill=255):
        self.draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=fill)

    def clear_display(self):
        self.oled.fill(0)
        self.oled.show()

    def update_display(self):
        self.oled.image(self.image)
        self.oled.show()


def main():
    display = DisplayController()
    display.clear_display()
    display.draw_background()
    display.draw_rectangle()
    display.write_text("hello display")
    display.update_display()


if __name__ == '__main__':
    main()

