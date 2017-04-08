class Vehicle(object):
	num_wheels = None
	def __init__(self, name, vehicle_type):
		self.name = name
		self.vehicle_type = vehicle_type

	def __str__(self):
			return "I am {} the {}!".format(self.name, self.vehicle_type)

	def vroom(self):
		raise notImplementedError("A generic car doesn't make a sound!")

	class Car(Vehicle):
		def __init__(self, name, vehicle_type)
			super(Car, self).__init__(name, vehicle_type)
			self.num_wheels = 4

		def vroom(self):
			return "Nyoom!"

	if __name__ == '__main__':
		my_car = Car("Princess", "Saturn")
		print(str(my_car))
		print(my_car.vroom())
		