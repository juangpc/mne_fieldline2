import lib.application

config = 'fieldline2ft.ini'
app = lib.application.App(config_file = config)
app.start()

def do_thing_2():
    pass

app.gui_model.callback_list[2] = do_thing_2