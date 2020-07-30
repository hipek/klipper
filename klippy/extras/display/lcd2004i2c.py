import logging
from .drivers.I2C_LCD_driver import lcd

class LCD2004I2C:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.printer.register_event_handler("klippy:shutdown", self.handle_shutdown)
        self.lcd = lcd()

    def flush(self):
        pass

    def init(self):
        self.lcd.backlight(1)

    def write_text(self, x, y, data):
        #logging.info("LCD2004 %s %d %d" , data, x, y)
        self.lcd.lcd_display_string(data, y + 1, x)

    def set_glyphs(self, glyphs):
        pass

    def write_glyph(self, x, y, glyph_name):
        return 0

    def write_graphics(self, x, y, data):
        pass

    def clear(self):
        pass

    def get_dimensions(self):
        return (20, 4)

    def handle_shutdown(self):
        self.lcd.lcd_clear()
        self.lcd.backlight(0)
