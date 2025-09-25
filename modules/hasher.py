import hashlib

from scipy import signal
from PIL import Image, ImageFile
from modules.base import BaseModule


class Hasher(BaseModule):
    
    def _process(self, item):
        
        cov = [[[0.1], [0.05], [0.1]]]
        img = signal.convolve(item, cov)
        img = Image.fromarray(img.astype('uint8')).convert('RGB')
        
        #hash
        md5 = hashlib.md5(str(img).encode('utf-8')).hexdigest()
        
        return md5
    
    
    def _process_singlethread(self, lists_):
        md5_list = []
        for img in lists_:
            md5 = self._process(img)
            md5_list.append(md5)
        return md5_list
    