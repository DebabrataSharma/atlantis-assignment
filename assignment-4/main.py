'''
    Write a python class that is able to find three available WiFi networks with the strongest signal and connect to the one where the password is provided. 

    Expected output: 
    $ python wifi.py
    > Your available wifi networks are: 
    > [1] Wifi_network 1
    > [2] Wifi_network 2
    > [3] Wifi_network 3
    > Your choice? 3
    > Password: *******
    > connected! 

'''


from general import *

if __name__=="__main__":
    connect_to_wifi = Wifi()
    available_network = connect_to_wifi.search_wifi_networks()
    get_best_signal = connect_to_wifi.get_best_signals(available_network)
    print("Your available wifi networks are:")
    for num,each_network in enumerate(get_best_signal,1):
        print("[{}] {}".format(num,each_network.ssid))
    try:
        network_choice = int(input("Your choice? "))
        if network_choice<=len(get_best_signal) and network_choice>0:
            password=input("Password: ")
            print("Connecting to network {}. Please wait...".format(get_best_signal[network_choice-1].ssid))
            connect = connect_to_wifi.connect_wifi(get_best_signal[network_choice-1],password)
            if connect:
                print("Successfully connected to network {}")
            else:
                print("Couldn't connect. Please try again.")
        else:
            print("Invalid choice. Please provide a valid number.")
    except:
        print("Invalid choice. Please provide a valid number.")    
