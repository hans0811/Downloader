import os

import utils
from modules.downloader import Downloader
from modules.hasher import Hasher
from modules.storage import Storager

class Scheduler:
    """_summary_
    """
    
    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storager = Storager()
        
    def _warp_path(self, md5):
        filename = '{}.jpg'.format(md5)
        STORAGE_PATH = os.path.join('.', 'images')
        path = os.path.join(STORAGE_PATH, filename)
        return path
    
    def process(self):
        # 1. loading photo URL
        url_list = utils.urllist()
        # 2. schedule downloading module
        content_list = self.downloader.process(url_list)
        # 3. use hash module
        md5_list = self.hasher.process(content_list)
        
        for md5 in md5_list:
            print(md5)
        # 4. Call save module
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._warp_path(md5)
            item = (content, path)
            item_list.append(item)
        self.storager.process(item_list)
        
        
if __name__ == '__main__':
    Scheduler().process()
    