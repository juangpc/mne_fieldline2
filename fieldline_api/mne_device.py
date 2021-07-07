import mne_device_lib

       
if __name__ == "__main__":

    opm = mne_device_lib.Device()

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
