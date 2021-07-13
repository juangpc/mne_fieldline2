import lib.fieldline
import lib.log
import lib.application
import lib.ini_file_parser
import lib.menus
import logging

log = logging.getLogger('main')

if __name__ == '__main__':
    log.info("Starting fieldline2ft application.")
    log.info("Creating main app.")
    app = lib.application.App()

    log.info("Parsing input file.")
    config = lib.ini_file_parser.parse_file('fieldline2ft.ini')
    log.debug(config)

    if lib.fieldline.fieldline_correctly_installed():
        app.set_gui_menu(lib.menus.Menu1(app))
    else:
        app.set_gui_menu(lib.menus.IncorrectInstallation(app))

    app.start()

# opm = FieldLineDevice(config.fieldline)

# ft_client = FieldTrip.Client()
# ft_IP = config.ft_IP
# ft_port = config.ft_port
# ft_data_type = FieldTrip.DATATYPE_FLOAT32

# data_stream_multiplier = 1

# def connect_to_fieldtrip_buffer():
#     ft_client.connect(ft_IP, ft_port)
#     if ft_client.isConnected:
#         print("Fieldtrip Client connected")

# def init_ft_header():
#     if ft_client.isConnected:
#         ft_client.putHeader(num_working_sensors(), default_sample_freq, ft_data_type)
#         header = ft_client.getHeader()
#         if header.nChannels == num_working_sensors():
#             print("Fieldtrip header initialized")

# def test_data_to_ft():
#     arr_data = nunmpy.zeros((200,num_working_sensors()), dtype=numpy.single)
#     ft_client.putData(arr_data)
    
# def init_fieldtrip_connection():
#     connect_to_fieldtrip_buffer()
#     init_ft_header()                


# def exit():
#     mne.disconnect
#     app.exit

# menu_item_connect = lib.gui.MenuItem('Connect to Fieldline', mne.connect)
# menu_item_disconnect = lib.gui.MenuItem('Disconnect from Fieldline', mne.disconnect)

# menu_item_start = lib.gui.MenuItem('Start to Fieldline', mne.start_measurement)
# menu_item_stop = lib.gui.MenuItem('Connect to Fieldline', mne.stop_measurement)

# menu_item_tune_sensors = lib.gui.MenuItem('Tune Fieldline sensors', mne.tune_sensors)
# menu_item_stop_tuning_sensors = lib.gui.MenuItem('Stop tuning sensors', mne.stop_tune_sensors)

# menu_item_use_phantom = lib.gui.MenuItem('Use Phantom', mne.phantom_on)
# menu_item_dont_use_phantom = lib.gui.MenuItem('Use Real Device', mne.phantom_off)

# menu = [menu_item_connect]

# app.gui_model.menu_items = menu + app.gui_model.menu_items


# # app.gui_model.menu_items[]
# # app.gui_model.callback_list[]
