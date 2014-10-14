import pykka

from mopidy import core

class AlarmFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(AlarmFrontend, self).__init__()
        self.core = core
        print ("Yo Nigger !")