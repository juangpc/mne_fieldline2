import mne_config_file_parser
import mne_fieldline_device


config_file = "fieldline_to_ft_buffer_config.py"

if __name__ == "__main__":

    opm = mne_device.Device()

    continue_loop = True

    while(continue_loop):
        print("Commands:")
        print("\tStart Measurment - start")
        print("\tStop Measurement - stop")
        print("\tDisconnect and exit - exit")
        command = input("Select command: ")
        if command == "start":
            print("Starting measurement...")
            opm.start()
        elif command == "stop":
            print("Stopping measurement...")
            opm.stop()
        elif command == "exit":
            print("Exiting program.")
            continue_loop = False
