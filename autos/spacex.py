from autos.abs_auto import AbsAuto


class SpaceX(AbsAuto):

    def start_sequence(self):
        print("1. Launch Phase")
        print("2. Cruise Phase")
        print("3. Encounter Phase")
        print("4. Extended Operations Phase")
        print("*"*20)
    def stop(self):
        print("1. Orbiter is cooling and noxious gases ejected")
        print("2. Orbiter is powered down")
        print("3. Crew exits the vehicle")
        print("*" * 20)