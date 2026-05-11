import pandas as pd

df = pd.read_csv("data.csv")

# school_type_and_state_count = df["state","school_type"].value_counts().reset_index()

# school_type_and_state_count.columns = ["school_type", "count" ,"state" ,"count"]
school_type_and_state_count = (
    df[["state", "school_type"]]
    .value_counts()
    .reset_index(name="count")
)

print(school_type_and_state_count.head())

school_type_and_state_count.to_csv(
    "school_type_and_state_count.csv",
    index=False
)
# print(school_type_and_state_count.head())

# school_type_and_state_count.to_csv("school_type_and_state_count.csv", index=False)

print("New CSV file created successfully!")