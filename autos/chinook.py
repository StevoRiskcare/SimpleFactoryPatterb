from autos.abs_auto import AbsAuto


class Chinook(AbsAuto):

    def start_sequence(self):
        print("Start sequence for {}".format(self.__class__.__name__))
        print("1. motor interllock “low”, arm the copter → rsc goes from off to idle")
        print("2. hit the turbinestart switch → rsc goes from idle to full power, then back to idle")
        print("3. turbine starting. 4)once up and running switch motor interlock to “high”, turbine should ramp up to flight regime")
        print("*"*20)
    def stop(self):
        print("1. Move Bater Switch up to off and Generator switch to center off")
        print("2. Depress Detent Buton")
        print("3. Twist throtle clockwise where off aligns to mark")
        print("4. DPull lever forward The aircraft is now safe so work around and extricate")
        print("*" * 20)