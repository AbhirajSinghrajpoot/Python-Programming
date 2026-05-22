class CoffeeMaker:
	"""Simulate the coffee machine's resource handling."""

	def __init__(self, water=300, milk=200, coffee=100):
		self.resources = {"water": water, "milk": milk, "coffee": coffee}

	def report(self):
		"""Return a string report of current resources."""
		return (
			f"Water: {self.resources['water']}ml\n"
			f"Milk: {self.resources['milk']}ml\n"
			f"Coffee: {self.resources['coffee']}g"
		)

	def is_resource_sufficient(self, drink):
		"""
		Check if there are enough resources to make the requested drink.
		`drink` is expected to have an `ingredients` dict.
		"""
		for item, required in drink.ingredients.items():
			if self.resources.get(item, 0) < required:
				print(f"Sorry, there is not enough {item}.")
				return False
		return True

	def make_coffee(self, drink):
		"""
		Deduct the required ingredients from the resources and return a success message.
		`drink` is expected to have an `ingredients` dict and `name`.
		"""
		for item, amount in drink.ingredients.items():
			self.resources[item] = self.resources.get(item, 0) - amount
		return f"Here is your {drink.name}. Enjoy!"

