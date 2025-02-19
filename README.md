# Ternary_plots - Ternary Phase Diagram Plotter 
This script generates a ternary phase diagram using experimental data from a CSV file. It plots the phase composition of a three-component system (compounds A, B, and C), including phase boundary, tie lines, and a plait point. The visualization helps in understanding phase separation and miscibility regions in the ternary system.

## Overview  
This Python script generates a ternary phase diagram using `mpltern`, `matplotlib`, and `pandas`. It reads phase composition data from a CSV file and visualizes:  
- The phase compositions of a three-component system (A, B, C).  
- The phase boundary and immiscibility region.  
- Tie lines connecting coexisting phases.  
- A plait point indicating the critical mixing composition.  

## Requirements  
Ensure you have the following Python packages installed:  
```bash
pip install numpy pandas matplotlib mpltern scipy
```

## Usage
1 - Prepare a CSV file named phase_composition_mol.csv containing mole fractions of the three compounds:
```bash
A,B,C
0.5,0.3,0.2
0.6,0.2,0.2
...
```
2 - Run the script:
```bash
python ternary_plot.py
```
3 - The script will generate and save the ternary phase diagram as diagram.png .

## Customization
Modify the CSV file to include your own composition data.
Adjust the plait_point or phantom_point values to refine the visualization.
Change boundary_points to update the immiscibility region.

## Output
The generated ternary diagram helps visualize phase behavior in three-component systems, useful for chemical and materials science applications.
