class MoneyMachine:
	"""Handle coin processing and payments."""

	DENOMINATIONS = [
		("500 rupee notes", 500),
		("200 rupee notes", 200),
		("100 rupee notes", 100),
		("50 rupee notes", 50),
		("20 rupee notes", 20),
		("10 rupee notes", 10),
		("5 rupee coins", 5),
		("2 rupee coins", 2),
		("1 rupee coins", 1),
	]

	def __init__(self):
		self.profit = 0.0

	def report(self):
		"""Return current profit as a formatted string."""
		return f"Money: Rs. {self.profit:.0f}"

	def process_coins(self) -> float:
		"""Prompt user for coins and return the total monetary value inserted."""
		print("Please insert rupees.")
		total = 0.0
		for label, value in self.DENOMINATIONS:
			while True:
				try:
					count = int(input(f"How many {label}? ").strip())
					break
				except ValueError:
					print("Please enter an integer.")
			total += count * value
		return round(total, 0)

	def make_payment(self, cost: float) -> bool:
		"""
		Process a payment for `cost`. Returns True if payment successful,
		handles change and updates profit; otherwise refunds and returns False.
		"""
		total_received = self.process_coins()
		if total_received < cost:
			print("Sorry that's not enough money. Money refunded.")
			return False
		change = round(total_received - cost, 0)
		if change > 0:
			print(f"Here is Rs. {change:.0f} in change.")
		self.profit += cost
		return True

