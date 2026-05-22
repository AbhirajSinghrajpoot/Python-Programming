class MenuItem:
	"""Represent a drink on the menu."""

	def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
		self.name = name
		self.cost = cost
		self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
	"""Manage available drinks."""

	def __init__(self):
		self.menu = [
			MenuItem("espresso", water=50, milk=0, coffee=18, cost=125),
			MenuItem("latte", water=200, milk=150, coffee=24, cost=208),
			MenuItem("cappuccino", water=250, milk=100, coffee=24, cost=249),
		]

	def get_items(self) -> str:
		"""Return a string of available drink names, e.g. 'espresso/latte/cappuccino'."""
		return "/".join(item.name for item in self.menu)

	def find_drink(self, order_name: str):
		"""Return the MenuItem matching order_name or None if not found."""
		order_name = order_name.lower()
		for item in self.menu:
			if item.name == order_name:
				return item
		return None

