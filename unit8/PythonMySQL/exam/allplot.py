import matplotlib.pyplot as plt

# Prepare the figure size
plt.figure(figsize=(12, 10))

# 🌟 1. Line Plot
plt.subplot(3, 2, 1)  # 3 rows, 2 columns, 1st plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.plot(x, y, marker="s", color="red", linestyle="--", label="Growth")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot with Style")
plt.grid(True)

# 🌟 2. Scatter Plot
plt.subplot(3, 2, 2)
xa = [11, 23, 45, 67, 89, 100]
ya = [2, 4, 6, 8, 10, 12]
plt.scatter(xa, ya, marker='o', color='purple', label="Data Points")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")
plt.title("Scatter Plot Magic")
plt.legend()
plt.grid(True)

# 🌟 3. Bar Chart
plt.subplot(3, 2, 3)
names = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 36]
plt.bar(names, values, color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.grid(axis='y')

# 🌟 4. Pie Chart
plt.subplot(3, 2, 4)
labels = ['Python', 'JavaScript', 'C++', 'Java']
sizes = [40, 25, 20, 15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie of Programming")

# 🌟 5. Histogram
plt.subplot(3, 2, 5)
hist_data = [12, 15, 13, 12, 15, 18, 17, 20, 21, 21, 25, 25, 27, 28, 29, 30]
plt.hist(hist_data, bins=8, color='orange', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)

# 🌟 6. Box Plot
plt.subplot(3, 2, 6)
box_data = [12, 15, 13, 18, 21, 21, 25, 30]
plt.boxplot(box_data)
plt.title("Box Plot")
plt.grid(True)

# Final Flourish 🌸
plt.tight_layout()
plt.show()
