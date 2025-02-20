# Ternary plot mol fraction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import mpltern
from scipy.interpolate import make_interp_spline

ax = plt.subplot(projection="ternary", ternary_sum=1)

# Axis labels
ax.set_tlabel("B")
ax.set_llabel("C")
ax.set_rlabel("A")

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')

# Axis tick marks
ax.taxis.set_major_locator(MultipleLocator(0.10))
ax.laxis.set_major_locator(MultipleLocator(0.10))
ax.raxis.set_major_locator(MultipleLocator(0.10))

# Grid
ax.grid()

# Load mole fractions from CSV
data = pd.read_csv('phase_composition_mol.csv')

# Extract mole fractions
mole_frac_b = data['B']
mole_frac_c = data['C']
mole_frac_a = data['A']

pc = ax.scatter(mole_frac_b, mole_frac_c, mole_frac_a, s=20, color='black', zorder=4)
ax.scatter([0], [1], [0], color='black', marker='o', s=20, zorder=4, label="(0, 1, 0) C")

# Manually specified plait point
plait_point_b = 0.241
plait_point_c = 0.747
plait_point_a = 0.012

plait_point = pd.DataFrame({'B': [plait_point_b], 'C': [plait_point_c], 'A': [plait_point_a]})

# Add the plait point to the plot
ax.scatter(plait_point_b, plait_point_c, plait_point_a, color='red', marker='o', s=20, label="Plait Point", zorder=3)

# Tie-lines
def plot_tie_lines(ax, mole_fraction_data):
    num_pairs = len(data) // 2
    for i in range(num_pairs):
        t1, l1, r1 = mole_fraction_data.iloc[i]['B'], mole_fraction_data.iloc[i]['C'], mole_fraction_data.iloc[i]['A']
        t2, l2, r2 = mole_fraction_data.iloc[i + num_pairs]['B'], mole_fraction_data.iloc[i + num_pairs]['C'], mole_fraction_data.iloc[i + num_pairs]['A']
        ax.plot([t1, t2], [l1, l2], [r1, r2], color='black', ls=':', linewidth=1)

mole_fraction_data = pd.DataFrame({'B': mole_frac_b, 'C': mole_frac_c, 'A': mole_frac_a})
plot_tie_lines(ax, mole_fraction_data)

# Boundary points for immiscibility region
boundary_points = mole_fraction_data.loc[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 21, 23]]

# Phantom points for boundary line
phantom_point_b = 0.368
phantom_point_c = 0.422
phantom_point_a = 0.210

phantom_point = pd.DataFrame({'B': [phantom_point_b], 'C': [phantom_point_c], 'A': [phantom_point_a]})

# Append plait and phantom points to boundary points
total_boundary_points = pd.concat([boundary_points, phantom_point, plait_point])

# Sort by A content
boundary_points_sorted = total_boundary_points.sort_values(by='A')

# Extract sorted boundary points
t_points = boundary_points_sorted['B'].values
l_points = boundary_points_sorted['C'].values
r_points = boundary_points_sorted['A'].values

# Spline interpolation
num_points = 100
t_param = np.linspace(0, 1, len(t_points))
r_smooth = np.linspace(0, 1, num_points)

t_spline = make_interp_spline(t_param, t_points, k=3)
l_spline = make_interp_spline(t_param, l_points, k=3)
r_spline = make_interp_spline(t_param, r_points, k=3)

t_smooth_vals = t_spline(r_smooth)
l_smooth_vals = l_spline(r_smooth)
r_smooth_vals = r_spline(r_smooth)

sum_smooth = t_smooth_vals + l_smooth_vals + r_smooth_vals
t_smooth_normalized = t_smooth_vals / sum_smooth
l_smooth_normalized = l_smooth_vals / sum_smooth
r_smooth_normalized = r_smooth_vals / sum_smooth

ax.plot(t_smooth_normalized, l_smooth_normalized, r_smooth_normalized, color='black', linestyle='-', linewidth=1.5, label='Guide Curve')
ax.fill(t_smooth_normalized, l_smooth_normalized, r_smooth_normalized, facecolor='gray', alpha=0.5)

plt.savefig('ternary_diagram_mole.png')
plt.show()
