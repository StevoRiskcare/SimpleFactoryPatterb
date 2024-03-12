from auto_factory import AutoFactory

factory = AutoFactory()

for carname in "Chinook", "SpaceX", "BMW_Unknown":
    car = factory.create_instance(carname)
    car.start_sequence()
    car.stop()