import tools

class memory_t(object):
    def __init__(self):
        self.anchor  = ""
        self.date    = ""
        self.details = ""
        self.color   = -1

    def set_memory(self, anchor, details, color):
        self.anchor = anchor
        self.date = tools.time_formatted()
        self.details = details
        self.color = color

    def save(self):
        return {
            "anchor"  : self.anchor,
            "date"    : self.date,
            "details" : self.details,
            "color"   : self.color
        }

    def load(self, data):
        pass