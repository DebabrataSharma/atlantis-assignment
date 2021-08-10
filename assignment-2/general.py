from config import *
import requests

class DictionarySearch:
    def __init__(self, query_str):
        self.url = dictionary_url+query_str

    def get_meaning(self):
        self.meaning_arr = []
        response = requests.get(self.url)
        if response.status_code==200:
            json_res = response.json()
            self.meaning_arr.append(json_res[0]["word"])
            for each_meaning in json_res[0]["meanings"]:
                pos = each_meaning["partOfSpeech"]
                definition = each_meaning["definitions"]
                for each_def in definition:
                    self.meaning_arr.append(pos)
                    self.meaning_arr.append(each_def["definition"])
            return ". ".join(self.meaning_arr)
        else:
            return None




        
        

