# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:39:57 2024

@author: JJED0001
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the dataset
file_path = 'C:/PhD Files/Milestones/Confirmation report/2nd paper/Simulation files/Optimisation/OPTimisation Result 24-06-2024V2.xlsx'
data_corrected = pd.read_excel(file_path, skiprows=3)


# Filter the data within the specified ranges
data_filtered_corrected = data_corrected[(data_corrected['TOP (bar)'] >= 20) & (data_corrected['TOP (bar)'] <= 50) &
                                         (data_corrected['COT ©'] >= 1050) & (data_corrected['COT ©'] <= 1250) &
                                         (data_corrected['COP (bar)'] >= 200) & (data_corrected['COP (bar)'] <= 400)]

# Extract relevant columns
x_corrected = data_filtered_corrected['COT ©']
y_corrected = data_filtered_corrected['TOP (bar)']
z_corrected = data_filtered_corrected['COP (bar)']
c_corrected = data_filtered_corrected['Overall system efficiency']

# Determine marker shapes based on TOP (bar) ranges
markers = []
for top in y_corrected:
    if 20 <= top < 30:
        markers.append('o')  # circle
    elif 30 <= top < 40:
        markers.append('s')  # square
    elif 40 <= top <= 50:
        markers.append('^')  # triangle

# Create the 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points with different markers for TOP (bar) ranges
for i, marker in enumerate(set(markers)):
    idx = [j for j, m in enumerate(markers) if m == marker]
    sc = ax.scatter(x_corrected[idx], z_corrected[idx], y_corrected[idx], c=c_corrected[idx], cmap='viridis', marker=marker, s=40, edgecolors='w', linewidth=0.5, label=f'TOP (bar) {20 + 10 * i}-{30 + 10 * i}')

# Set color limits for the scatter plot
sc.set_clim(65.34, 68.14)

# Adding labels and title
ax.set_xlabel('COT (C)', labelpad=15)
ax.set_ylabel('COP (bar)', labelpad=15)
ax.set_zlabel('TOP (bar)', labelpad=15)
ax.set_title('Effect of COT (C), COP (bar), and TOP (bar) on Overall System Efficiency with TOP (bar) Ranges', pad=20)

# Adding a color bar to indicate the efficiency values with specified limits
cb_corrected_swapped = plt.colorbar(sc, ax=ax, pad=0.1, shrink=0.8, aspect=15)
cb_corrected_swapped.set_label('Overall System Efficiency')

# Adding the labels 65.34 and 68.14 to the color bar
cb_corrected_swapped.set_ticks([65.34, 66, 67, 68, 68.14])
cb_corrected_swapped.set_ticklabels(['65.34', '66', '67', '68', '68.14'])

# Adding legend to specify marker shapes
ax.legend(title='TOP (bar) Range')

# Improve the viewing angle
ax.view_init(elev=30, azim=120)

# Save the plot with high resolution
plt.savefig('3D_plot_high_resolution.png', dpi=300, bbox_inches='tight')

plt.show()
