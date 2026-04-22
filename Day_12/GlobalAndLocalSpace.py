# Local variable
def drink_water():
    print("Drinking water")

drink_water()
print("Washing face")

# Global variable
player_strength = 10

def brush_teeth():
    print("Brushing teeth")
    def morning_routine():
        drink_water()
        morning_routine()
        potion_strength = 2
        print("Potion strength:", potion_strength)
brush_teeth()

print("Finished morning routine: " + str(player_strength))

