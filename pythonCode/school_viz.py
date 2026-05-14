import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# =========================
# File Paths
# =========================

BASE_DIR = Path(__file__).resolve().parent

file_path = BASE_DIR / "data.csv"
output_image = BASE_DIR / "school_analysis.png"

if not file_path.exists():
    print(f"Error: File not found: {file_path}")
    exit(1)


# =========================
# Read Data
# =========================

df = pd.read_csv(file_path)

# Basic validation
required_columns = ["state", "school_type"]

for column in required_columns:
    if column not in df.columns:
        print(f"Error: Missing required column: {column}")
        exit(1)


# =========================
# Prepare Data
# =========================

state_counts = df["state"].value_counts().head(10)
school_type_counts = df["school_type"].value_counts().sort_values()


# =========================
# Chart Design
# =========================

plt.style.use("seaborn-v0_8-whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(18, 8))
fig.patch.set_facecolor("#f8fafc")

ax1, ax2 = axes


# =========================
# Plot 1: Top 10 States
# =========================

bars1 = ax1.bar(
    state_counts.index,
    state_counts.values,
    color="#2563eb",
    edgecolor="#1e3a8a",
    linewidth=1.2
)

ax1.set_title(
    "Top 10 States by School Count",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax1.set_xlabel("State", fontsize=12, fontweight="bold")
ax1.set_ylabel("Number of Schools", fontsize=12, fontweight="bold")
ax1.tick_params(axis="x", rotation=35)
ax1.grid(axis="y", linestyle="--", alpha=0.4)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        int(height),
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )


# =========================
# Plot 2: School Type Distribution
# =========================

bars2 = ax2.barh(
    school_type_counts.index,
    school_type_counts.values,
    color="#16a34a",
    edgecolor="#14532d",
    linewidth=1.2
)

ax2.set_title(
    "School Type Distribution",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax2.set_xlabel("Number of Schools", fontsize=12, fontweight="bold")
ax2.set_ylabel("School Type", fontsize=12, fontweight="bold")
ax2.grid(axis="x", linestyle="--", alpha=0.4)

# Add value labels
for bar in bars2:
    width = bar.get_width()
    ax2.text(
        width + 5,
        bar.get_y() + bar.get_height() / 2,
        int(width),
        va="center",
        fontsize=10,
        fontweight="bold"
    )


# =========================
# Main Title and Footer
# =========================

fig.suptitle(
    "Student Loan Dataset Analysis",
    fontsize=22,
    fontweight="bold",
    y=1.03
)

fig.text(
    0.5,
    0.01,
    "Day 6: Exploratory Data Analysis using Pandas and Matplotlib",
    ha="center",
    fontsize=12,
    color="#334155"
)


# =========================
# Save and Show
# =========================

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

plt.savefig(output_image, dpi=300, bbox_inches="tight")
print(f"Chart saved successfully: {output_image}")

plt.show()