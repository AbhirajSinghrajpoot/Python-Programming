import pandas
from pathlib import Path

# auto-detect CSV file in the script directory
base = Path(__file__).parent
candidates = list(base.glob('2018_Central_Park_Squirrel_Census*.csv'))
if not candidates:
    available = [p.name for p in base.glob('*.csv')]
    raise FileNotFoundError(
        "Squirrel CSV not found. Expected a file starting with '2018_Central_Park_Squirrel_Census'.\n"
        f"Available CSV files: {available}"
    )
data = pandas.read_csv(candidates[0])
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"Grey squirrels count: {grey_squirrels_count}")
print(f"Red squirrels count: {red_squirrels_count}")
print(f"Black squirrels count: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")