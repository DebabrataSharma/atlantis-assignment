from wifi import Cell, Scheme
from config import *

class Wifi:
    def __init__(self):
        pass

    def search_wifi_networks(self):
        '''
            returns all the available networks
        '''
        return list(Cell.all(interface))
    
    def get_best_signals(self,networks):
        '''
            sorts the wifi networks based on signal strength and returns maximum 3 
        '''
        networks = sorted(networks, key=lambda i: i.quality)
        if len(networks)>=3:
            return networks[:3]
        return networks
    
    def connect_wifi(self,network_name,password):
        '''
            connects to the selected wifi
        '''
        try:
            scheme = Scheme.for_cell(interface, 'home', network_name, password)
            scheme.save()
            scheme.activate()
            return True
        except Exception as e:
            print(e)
            return False

