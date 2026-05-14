import pandas as pd

df = pd.read_csv("data.csv")

school_type_and_state_count_shool_name = (
    df[["state", "school_type", "school" ]].value_counts().reset_index(name="count")
)

print(school_type_and_state_count_shool_name)

# school_type_and_state_count_shool_name.to_csv("school_type_and_state_count_shool_name.csv", index=False)

# print("New CSV file created successfully!")
