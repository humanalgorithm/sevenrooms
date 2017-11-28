

class Logger(object):
    def log(self, key, data):
        func = {
            "reservation_added": False,
            "reservation_blocked": False
        }

        if func[key]:
            getattr(self, key)(data)

    def reservation_added(self, data):
        print "Reservation has been added: {}".format(data)

    def reservation_blocked(self, data):
        print "Reservation was unable to be added: {}".format(data)
