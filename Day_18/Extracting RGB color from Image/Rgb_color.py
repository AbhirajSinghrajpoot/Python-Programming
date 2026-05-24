import colorgram

# Extract 10 colors from an image
rgb_colors = []
colors = colorgram.extract(r"D:\Python 100 Days.worktrees\Day_18\Extracting RGB color from Image\images.jpg", 30)

# Get RGB values of each color
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(254, 254, 254), (146, 177, 153), (49, 38, 45), (162, 144, 157), (168, 153, 43), (155, 176, 193), (226, 236, 231), (81, 147, 128), (54, 123, 93), (229, 223, 224), (146, 17, 20), (74, 26, 20), (193, 164, 128), (196, 92, 74), (56, 94, 121), (107, 128, 154), (211, 219, 223), (154, 74, 53), (20, 55, 72), (137, 16, 10), (10, 95, 67), (167, 100, 103), (229, 176, 166), (183, 204, 172), (9, 66, 59), (18, 86, 89), (26, 68, 102), (104, 92, 94), (211, 205, 156)]