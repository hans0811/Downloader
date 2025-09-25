import requests
from PIL import ImageFile
import numpy as np

from const import CalcType
from modules.base import BaseModule

class Downloader(BaseModule):
    """ downloader module"""
    def __init__(self):
        super(Downloader, self).__init__()
        
    
    def _process(self, url):
        print(f'Download url: {url}')
        response = requests.get(url)
        content  = response.content
        # pic convert to numpy
        parser = ImageFile.Parser()
        parser.feed(content)
        img = parser.close()
        img = np.array(img)
        return img
    
    def _process_singlethread(self, list_):
        response_list = []
        for url in list_:
            img = self._process(url)
            response_list.append(img)
        return response_list
    
    def process(self, list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_)
        else:
            pass
