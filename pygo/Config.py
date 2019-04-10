class ConfigStruct:
    def __init__(self):
        self.x_window_size = 1000
        self.y_window_size = 1000
        self.resize_window_x = 0
        self.resize_window_y = 0

        self.bg_color = "ghost white"
        self.fg_color = "black"

        self.border_color = "black"
        self.border_thick = 5
        self.border_thin = 1

        self.relief = "flat"

        self.home_icon = "../media/home.png"
        self.home_button_size = 40

        self.font_family = "Noto Mono"
        self.desc_font_size = 12
        self.query_font_size = 15
        self.start_font_size = 20
        self.title_font_size = 70

        self.dim_options = ["9x9", "13x13", "17x17", "19x19"]
        self.DEFAULT_COLORS = ["black", "white", "red", "green", "blue", "violet"]


config = ConfigStruct()
