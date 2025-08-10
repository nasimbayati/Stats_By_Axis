# Stats by Axis — NumPy Showcase

This project demonstrates how to compute **mean**, **sum**, and **median** by **row** and by **column** for a 2D NumPy array.  
It includes an option to generate either deterministic arrays or random integer arrays.

---

## Features
- Generates a 2D NumPy array (either sequential numbers or random integers).
- Computes:
  - Mean by row and column
  - Sum by row and column
  - Median by row and column
- Command-line arguments for customization:
  - Number of rows and columns
  - Random seed for reproducibility
  - Integer value range for random arrays

---

## Installation
This project requires Python 3 and NumPy.

```bash
pip install numpy
```

## Usage
**Run with default parameters:**

```bash
python stats_by_axis.py
```

**Run with custom parameters:**
```bash
python stats_by_axis.py --rows 5 --cols 4 --seed 7 --low 10 --high 99
```

## Example Output
Input array (shape (4, 3)):
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]] 
 

Means by row:    [ 2.,  5.,  8., 11.]

Means by col:    [5.5, 6.5, 7.5]

Sums by row:     [ 6, 15, 24, 33]

Sums by col:     [22, 26, 30]

Medians by row:  [ 2.,  5.,  8., 11.]

Medians by col:  [5.5, 6.5, 7.5]


