import abc


class AbsAuto(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start_sequence(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

