test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
def paint_calc(height, width, cover):
    area = height * width
    rounded_num_of_cans = round(area / cover)
    print(f"You'll need {rounded_num_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)