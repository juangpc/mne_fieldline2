import lib.application
import lib.ini_file_parser as parser

import time

config_file = 'fieldline2ft.ini'
config = parser.parse_file(config_file)

app = lib.application.App()
class Menu1:
    def __init__(self, app):
        self.menu_list = [('Func1 - Menu1', self.func1),
                          ('Change state to Menu2', self.func2),
                          ('Exit', app.exit) ]
    
    def func1(self):
        with open('bli1.txt','w') as file_out:
            file_out.write('blablabla')
            file_out.write('\n\nfunc1 in Menu1')
    
    def func2(self):
        app.set_gui_menu(Menu2(app)) 

class Menu2:
    def __init__(self, app):
        self.menu_list = [('func1 - Menu2', self.func1),
                          ('Exit', app.exit) ]

    def func1(self):
        with open('bli2.txt','w') as file_out:
            file_out.write('blobloblo')
            file_out.write('\n\nfunc1 in Menu2')


app.set_gui_menu(Menu1(app))

app.start()



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
