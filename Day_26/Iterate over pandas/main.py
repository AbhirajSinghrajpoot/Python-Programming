import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
}

student_data_frame = pd.DataFrame(data)
print(student_data_frame)
# Iterate over the DataFrame using iterrows()
for index, row in student_data_frame.iterrows():
    if row.Age > 30:
        print(f"{row.Name} is {row.Age} years old.")