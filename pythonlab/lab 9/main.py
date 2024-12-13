# Lab 9-10: PANDAS & File operations:
# Election Data:
# State
# Party
# Seats_Won
# Total_Seats
# Voter_Turnout (%)
# Madhya Pradesh
# BJP
# 163
# 230
# 72.1
# Madhya Pradesh
# INC
# 66
# 230
# 72.1
# Madhya Pradesh
# BSP
# 0
# 230
# 72.1
# Madhya Pradesh
# Others
# 1
# 230
# 72.1
# Rajasthan
# BJP
# 115
# 200
# 74.2
# Rajasthan
# INC
# 69
# 200
# 74.2
# Rajasthan
# BSP
# 2
# 200
# 74.2
# Rajasthan
# Others
# 13
# 200
# 74.2


# And perform the following tasks:
# Check if the file `election_data.csv` exists in the directory. If not, create the file and write the election data into it. Handle file-related exceptions gracefully.
# Read the data into a Pandas DataFrame and calculate the percentage of seats won by each party. Add this as a new column named Seats_Percentage.
# Determine the party with the highest number of seats in each state and display their names.
# Create a bar chart showing the number of seats won by each party in each state using Matplotlib or Seaborn.
# Ensure your script includes exception handling for file reading, writing, and any potential calculation errors.

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Election data and file name
election_data = [
    {"State": "Madhya Pradesh", "Party": "BJP", "Seats_Won": 163, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "INC", "Seats_Won": 66, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "BSP", "Seats_Won": 0, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Madhya Pradesh", "Party": "Others", "Seats_Won": 1, "Total_Seats": 230, "Voter_Turnout (%)": 72.1},
    {"State": "Rajasthan", "Party": "BJP", "Seats_Won": 115, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "INC", "Seats_Won": 69, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "BSP", "Seats_Won": 2, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
    {"State": "Rajasthan", "Party": "Others", "Seats_Won": 13, "Total_Seats": 200, "Voter_Turnout (%)": 74.2},
]
file_name = "election_data.csv"

# Step 1: Ensure the file exists
if not os.path.exists(file_name):
    pd.DataFrame(election_data).to_csv(file_name, index=False)
    print(f"{file_name} created successfully!")

# Step 2: Read data
try:
    df = pd.read_csv(file_name)
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Step 3: Add Seats_Percentage
df["Seats_Percentage"] = (df["Seats_Won"] / df["Total_Seats"]) * 100

# Step 4: Identify top parties per state
top_parties = df.loc[df.groupby("State")["Seats_Won"].idxmax(), ["State", "Party", "Seats_Won"]]
print("\nParties with the highest seats in each state:\n", top_parties)

# Step 5: Plot results
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="State", y="Seats_Won", hue="Party")
plt.title("Seats Won by Each Party in Each State")
plt.ylabel("Seats Won")
plt.xlabel("State")
plt.legend(title="Party")
plt.tight_layout()
plt.show()
