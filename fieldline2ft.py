import mne_config_file_parser
import curses
import time
# import mne_device

config_file = 'fieldline2ft.ini'

stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.start_color()

menu_items = ["START", "STOP", "RESTART", "EXIT"]
item_idx_selected = 0

def greet_screen(text, vertical_position):
    screen_height, screen_width = stdscr.getmaxyx()
    stdscr.addstr(screen_height//2 - vertical_position, screen_width//2 - len(text)//2, text)

def load_config_file():
    parser = mne_config_file_parser.Parser(config_file)
    return parser.read()
   
def print_menu():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    global item_idx_selected
    global menu_items
    screen_height, screen_width = stdscr.getmaxyx()
    for idx, item in enumerate(menu_items):
        x = screen_width//2 - len(item)//2
        y = screen_height//2 - len(menu_items)//2 + idx
        if idx == item_idx_selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, item)

def start():
    config = load_config_file()
    print(config)
    
def stop():
    pass

def main(stdcr):
    global item_idx_selected
    
    stdscr.clear()
    greet_screen("Mellow greetings!!", 1)
    greet_screen("Hi, Let's do some kick-ass OPM work today!!", 0)
    stdscr.refresh()
    time.sleep(2)

    exit_application = False
    while not exit_application:
        stdscr.clear()
        print_menu()

        key = stdscr.getch()

        if key == curses.KEY_UP or key == 450 or key == ord('k'):
            if item_idx_selected > 0:
                item_idx_selected -= 1
        elif key == curses.KEY_DOWN or key == 456 or key == ord('j'):
            if item_idx_selected < len(menu_items) -1:
                item_idx_selected += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu_items[item_idx_selected] == "EXIT":
                exit_application = True
        
        stdscr.refresh()

curses.wrapper(main)