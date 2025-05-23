import matplotlib.pyplot as plt

# Data
categories = ["Category A", "Category B", "Category C"]
values = [10, 25, 7]

# Create horizontal bar chart
plt.barh(categories, values)

# Add labels and title
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart")

# Show the chart
plt.show()
