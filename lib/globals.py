import logging

log = logging.getLogger(__name__)

app = None
exit = None

def set_global_app(_app):
    global app
    global exit
    app = _app
    exit = _app.exit
    log.info("app settled correctly as global.")

def get_global_app():
    global app
    return app

def switch_to_menu(menu):
    global app
    log.info("switching to new menu")
    app.set_gui_menu(menu)



