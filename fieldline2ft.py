import mne_cpp.application

config = 'fieldline2ft.ini'
app = mne_cpp.application.App(config_file = config)
app.start()
