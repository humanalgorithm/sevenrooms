

class TimeBlock(object):
    def __init__(self, start, end, *args, **kwargs):
        self.start = start
        self.end = end

    def __repr__(self):
        return "start: {} end: {}".format(self.start.strftime('%H:%M'), self.end.strftime('%H:%M'))

class Reservation(TimeBlock):
    def __init__(self, start, end, party_size, *args, **kwargs):
        super(Reservation, self).__init__(start, end, args, kwargs)
        self.party_size = party_size

    def __repr__(self):
        return "party size: {}, start: {} end: {}".format(
            self.party_size, self.start.strftime('%H:%M'), self.end.strftime('%H:%M'))