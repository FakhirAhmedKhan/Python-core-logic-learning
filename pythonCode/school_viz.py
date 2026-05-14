import matplotlib.pyplot as plt
import pandas as pd
import os

# Define absolute file path
file_path = r'c:\Users\Dell\OneDrive\Desktop\Programs\Python-core-logic-learning\DataScienceDay3\data.csv'

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found.")
    exit(1)

# Read the data
df = pd.read_csv(file_path)

# Set a modern style
plt.style.use('ggplot') 

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot 1: Top 10 States by School Count
state_counts = df['state'].value_counts().head(10)
state_counts.plot(kind='bar', ax=ax1, color='#3498db', edgecolor='black')
ax1.set_title('Top 10 States by School Count', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('State', fontsize=12)
ax1.set_ylabel('Number of Schools', fontsize=12)
ax1.tick_params(axis='x', rotation=0)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Plot 2: Distribution of School Types
type_counts = df['school_type'].value_counts()
colors = ['#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6']
type_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=140, 
                colors=colors, wedgeprops={'edgecolor': 'white', 'linewidth': 2},
                textprops={'fontsize': 12})
ax2.set_title('Distribution of School Types', fontsize=14, fontweight='bold', pad=15)
ax2.set_ylabel('') # Remove y-label for pie chart

# Overall Layout
plt.suptitle('US School Dataset Analysis', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()

# Save the figure to the artifacts directory so I can show it
output_image = r'c:\Users\Dell\OneDrive\Desktop\Programs\Python-core-logic-learning\DataScienceDay3\school_analysis.png'
plt.savefig(output_image, dpi=300, bbox_inches='tight')
print(f"Chart saved to: {output_image}")

# Show the plot
plt.show()