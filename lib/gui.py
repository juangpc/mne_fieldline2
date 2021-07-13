import curses
import threading

class MenuItem:
    def __init__(self, text, function_name):
        self.text = text
        self.callback = function_name

class Menu:
    def __init__(self, menu_items_list = []):
        self.menu_items = []
        for name, function_name in menu_items_list:
            self.menu_items.append(MenuItem(name, function_name))

class Gui:
    def __init__(self):
        self.__stdscr = curses.initscr()
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()

        self.__parse_user_input_flag = True
        self.__parse_user_input_flag_lock = threading.Lock()
        self.__user_input_parser_thread = threading.Thread(target=self.__parse_user_input, daemon=True)
        self.__start_parsing_user_inputs()

        self.__item_idx_selected = 0
        self.menu = Menu()
        
        self.__spawned_callback_calls_list = []

    def __del__(self):
        self.__stop_parsing_user_inputs()
        self.__stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def update(self, menu_items_list):
        self.menu = Menu(menu_items_list)
        self.__update_view()

    def exit_loop(self):
        self._exit_menu = True

    def __update_view(self):
        self.__stdscr.clear()
        self.__print_menu_items()
        self.__stdscr.refresh()

    def __parse_user_input(self):
        curses.wrapper(self.__user_input_parser)

    def __continue_parsing_user_input(self, *argv):
        if len(argv) == 0:
            self.__parse_user_input_flag_lock.acquire()
            out_state = self.__parse_user_input_flag
            self.__parse_user_input_flag_lock.release()            
        elif len(argv) == 1 and type(argv[0]) is bool:
            self.__parse_user_input_flag_lock.acquire()
            self.__parse_user_input_flag = argv[0]
            self.__parse_user_input_flag_lock.release()
            out_state = argv[0]
        return out_state

    def __user_input_parser(self, stdscr):
        while self.__continue_parsing_user_input(): 
            key = self.__stdscr.getch()
            # self.__stdscr.addstr(0, 0, str(key))
            if key in {curses.KEY_UP, 450, ord('k')}:
                if self.__item_idx_selected > 0:
                    self.__item_idx_selected -= 1
            elif key in {curses.KEY_DOWN, 456, ord('j')}:
                if self.__item_idx_selected < len(self.menu.menu_items) - 1:
                    self.__item_idx_selected += 1
            elif key in {curses.KEY_ENTER, 10, 13, 459}:
                self.__spawn_callback(self.__item_idx_selected)

    def __spawn_callback(self, fcn_idx):
        fcn = self.menu.menu_items[fcn_idx].callback
        self.__spawned_callback_calls_list.append(threading.Thread(target = fcn, daemon = True))
        self.__spawned_callback_calls_list[len(self.__spawned_callback_calls_list) -1].start()

    def __start_parsing_user_inputs(self):
        self.__continue_parsing_user_input(True)
        self.__user_input_parser_thread.start()

    def __stop_parsing_user_inputs(self):
        self.__continue_parsing_user_input(False)
        self.__user_input_parser_thread.join()

    def __print_menu_items(self):
        curses.init_pair(1, curses.COLOR_WHITE, 242)
        screen_height, screen_width = self.__stdscr.getmaxyx()
        for idx, item in enumerate(self.menu.menu_items):
            x = screen_width//2 - len(item.text)//2
            y = screen_height//2 - len(self.menu.menu_items)//2 + idx
            if idx == self.__item_idx_selected:
                self.__stdscr.addstr(y, x, item.text, curses.color_pair(1))
            else:
                self.__stdscr.addstr(y, x, item.text)

