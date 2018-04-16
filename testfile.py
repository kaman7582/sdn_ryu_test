

from ryu.base import app_manager

class my_traffic(app_manager.AppManager):
    def __init__(self,*args,**kwargs):
        super(my_traffic,self).__init__(*args,**kwargs)
        print "my traffic class init"

