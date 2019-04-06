class Interface:
	def __init__(self, root):

		self.root = root

		# Configure root
		self.root.geometry('{}x{}'.format(cfg.x_window_size, cfg.y_window_size))
		self.root.resizable(cfg.resize_window_x, cfg.resize_window_y)
		self.root.configure(background=cfg.bg_color)
		self.root.title('Py-Go')

	def home(self):

	def saved_games(self):

	def new_game(self):

	def play(self):