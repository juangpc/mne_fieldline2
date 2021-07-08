import mne_config_file_parser
# import mne_device

config_file = 'fieldline_to_ft_buffer.ini'

def load_config_file():
    parser = mne_config_file_parser.Parser(config_file)
    return parser.read()
   
def start():
    config = load_config_file()
    print(config)
    
def stop():
    pass

if __name__ == "__main__":

    continue_loop = True

    while(continue_loop):
        print("Commands:")
        print("\tStart Measurment - start")
        print("\tStop Measurement - stop")
        print("\tDisconnect and exit - exit")
        command = input("Select command: ")
        if command == 'start':
            print("Starting measurement...")
            start()
        elif command == 'stop':
            print("Stopping measurement...")
            stop()
        elif command == 'exit':
            print("Exiting program.")
            continue_loop = False
