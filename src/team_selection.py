class TeamSelection(object):
    def __init__(self):
        self.white = []
        self.black = []
        self.rating = None

    def __str__(self):
        return "white team: % s\nblack team: %s" % (self.white, self.black)
