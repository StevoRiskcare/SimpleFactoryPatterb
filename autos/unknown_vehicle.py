from autos.abs_auto import AbsAuto


class UnknownVehicle(AbsAuto):
    def __init__(self, carname):
        self._carname = carname

    def start_sequence(self):
        print("Unknown Vehicle selected: {}".format(self._carname))

    def stop(self):
        pass