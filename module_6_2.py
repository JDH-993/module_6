class Vehicle:
	__COLOR_VARIANTS = ['Indigo ', 'red', 'Orange', 'black', 'white']

	def __init__(self, owner, __model, __color, __engine_power):
		self.owner = owner
		self.__model = __model
		self.__color = __color
		self.__engine_power = __engine_power

	def print_info(self):
		print(f"Модель: {self.__model}")
		print(f"Мощность двигателя: {self.__engine_power}")
		print(f"Цвет: {self.__color}")
		print(f"Владелец: {self.owner}")
		pass

	def get_model(self, __model):
		print(f"Модель: {self.__model}")

	def get_horsepower(self, __engine_power):
		print(f"Мощность двигателя:{self.__engine_power}")

	def get_color(self, __color):
		print(f"Цвет: {self.__color}")

	def set_color(self, new_color):
		g = new_color.upper()
		u = []
		for i in self.__COLOR_VARIANTS:
			i = i.upper()
			u.append(i)
		if g in u:
			self.__color = new_color
		else:
			print(f"Нельзя сменить цвет на {new_color}")

	pass


class Sedan(Vehicle):
	__PASSENGERS_LIMIT = 5
	pass


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'Violet', 500)
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Green ')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()