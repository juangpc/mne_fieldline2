import lib.application
import lib.mne_fieldline as mne

config = 'fieldline2ft.ini'

app = lib.application.App()

# def exit():
#     mne.disconnect
#     app.exit

# menu_item_connect = lib.gui.Menu_Item('Connect to Fieldline', mne.connect)
# menu_item_disconnect = lib.gui.Menu_Item('Disconnect from Fieldline', mne.disconnect)

# menu_item_start = lib.gui.Menu_Item('Start to Fieldline', mne.start_measurement)
# menu_item_stop = lib.gui.Menu_Item('Connect to Fieldline', mne.stop_measurement)

# menu_item_tune_sensors = lib.gui.Menu_Item('Tune Fieldline sensors', mne.tune_sensors)
# menu_item_stop_tuning_sensors = lib.gui.Menu_Item('Stop tuning sensors', mne.stop_tune_sensors)

# menu_item_use_phantom = lib.gui.Menu_Item('Use Phantom', mne.phantom_on)
# menu_item_dont_use_phantom = lib.gui.Menu_Item('Use Real Device', mne.phantom_off)

# menu_item_exit = lib.gui.Menu_Item('Exit', exit)

# menu = [menu_item_connect]

# app.gui_model.menu_items = menu + app.gui_model.menu_items

app.start()

# # app.gui_model.menu_items[]
# # app.gui_model.callback_list[]
