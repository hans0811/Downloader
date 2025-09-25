from const import CalcType


class BaseModule:
    """abstract
    """
    def __init__(self):
        self.calc_type = CalcType.SingleThread
        
    def set_clac_type(self, type_):
        self.set_clac_type = type_
    
    def _process(self, url):
        raise NotImplementedError
        
    
    
    def _process_singlethread(self, list_):
        raise NotImplementedError
    
    def process(self, list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_)
        else:
            pass
