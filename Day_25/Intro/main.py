import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["Temp"].to_list()
print(temp_list)
print(len(temp_list))


print(data["Temp"].mean())

print(data["Temp"].max())

print(data["Condition"])
print(data.Condition)

monday = data[data.Day == "Monday"]
print(monday)

monday_temp_fahrenheit = monday["Temp"] * 9/5 + 32
print(f"Monday's temperature in Fahrenheit: {monday_temp_fahrenheit}")

print(data[data.Temp == data.Temp.max()])



data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
} 
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")