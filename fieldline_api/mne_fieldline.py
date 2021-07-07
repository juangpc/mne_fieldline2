import mne_fieldline_lib as fl

       
if __name__ == "__main__":
    opm = fl.FieldlineDevice()
    
    continue_loop = True
    
    while(continue_loop):
        print("Commands:")
        print("\tStart Measurment - start")
        print("\tStop Measurement - stop")
        print("\tDisconnect and exit - exit")
        command = input("Select command: ")
        if command == "start":
            print("Starting measurement...")
            opm.start_measurement()
        elif command == "stop":
            print("Stopping measurement...")
            opm.stop_measurement()
        elif command == "exit":
            print("Exiting program.")
            continue_loop = False
