
from PIL import Image

from modules.base import BaseModule


class Storager(BaseModule):
    """
        Save module
    """
    
    
    def _process(self, item):
        content, path = item
        print('save path: {}'.format(path))
        content = Image.fromarray(content.astype('uint8')).convert('RGB')
        content.save(path)
    
    
    def _process_singlethread(self, list_):
        # item = (content, path4)
        for item in list_:
            self._process(item)
            
        return super()._process_singlethread(list_)