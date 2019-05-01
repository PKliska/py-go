def make_smaller(obj, name):
    def smaller(n):
        return int(round(n * 0.7))

    attr_list = [
        "x_window_size",
        "y_window_size",
        "border_thin",
        "border_thick",
        "home_button_size",
        "desc_font_size",
        "query_font_size",
        "start_font_size",
        "title_font_size",
    ]
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith("__"):
            if attr in attr_list:
                exec("{0}.{1} = smaller({0}.{1})".format(name, attr))


class ConfigStruct:
    def __init__(self):
        self.x_window_size = 1000
        self.y_window_size = 1000
        self.resize_window_x = 0
        self.resize_window_y = 0

        self.bg_color = "ghost white"
        self.fg_color = "black"
        self.board_color = self.bg_color

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
        self.saved_font_size = 30
        self.title_font_size = 70

        self.dim_options = ["9x9", "13x13", "17x17", "19x19"]
        self.DEFAULT_COLORS = [
            "#000000",
            "#ffffff",
            "#ff0000",
            "#008000",
            "#0000ff",
            "#ee82ee",
        ]

        self.games_dir = "../games/"


config = ConfigStruct()
# make_smaller(config, "config")
