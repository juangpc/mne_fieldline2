
app = None
exit = None

def set_global_app(_app):
    global app
    global exit
    app = _app
    exit = _app.exit

def get_global_app():
    global app
    return app

def switch_to_menu(new_menu):
    global app
    app.set_gui_menu(new_menu)

