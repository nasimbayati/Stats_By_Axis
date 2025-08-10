# stats_by_axis.py
"""
Stats by Axis — NumPy Showcase
Computes mean, sum, and median by row and by column for a 2D NumPy array.

Usage examples:
  python stats_by_axis.py
  python stats_by_axis.py --rows 5 --cols 4 --seed 7 --low 10 --high 99
"""

from __future__ import annotations
import argparse
import numpy as np


def compute_stats(arr: np.ndarray) -> dict[str, np.ndarray]:
    """Return means, sums, and medians by row and by column."""
    if arr.ndim != 2:
        raise ValueError("Input array must be 2D.")
    stats = {
        "mean_by_row":   arr.mean(axis=1),
        "mean_by_col":   arr.mean(axis=0),
        "sum_by_row":    arr.sum(axis=1),
        "sum_by_col":    arr.sum(axis=0),
        "median_by_row": np.median(arr, axis=1),
        "median_by_col": np.median(arr, axis=0),
    }
    return stats


def make_array(rows: int, cols: int, seed: int | None, low: int, high: int) -> np.ndarray:
    """Create a rows×cols integer array for demo purposes."""
    if seed is not None:
        rng = np.random.default_rng(seed)
        return rng.integers(low=low, high=high + 1, size=(rows, cols))
    # Deterministic example (matches many classroom demos)
    return np.arange(1, rows * cols + 1, dtype=int).reshape(rows, cols)


def print_stats(arr: np.ndarray, stats: dict[str, np.ndarray]) -> None:
    print("Input array (shape {}):\n{}".format(arr.shape, arr), "\n")
    print("Means by row:   ", np.array2string(stats["mean_by_row"], separator=", "))
    print("Means by col:   ", np.array2string(stats["mean_by_col"], separator=", "))
    print("Sums by row:    ", np.array2string(stats["sum_by_row"], separator=", "))
    print("Sums by col:    ", np.array2string(stats["sum_by_col"], separator=", "))
    print("Medians by row: ", np.array2string(stats["median_by_row"], separator=", "))
    print("Medians by col: ", np.array2string(stats["median_by_col"], separator=", "))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compute mean, sum, and median by axis for a 2D array.")
    p.add_argument("--rows", type=int, default=4, help="number of rows (default: 4)")
    p.add_argument("--cols", type=int, default=3, help="number of cols (default: 3)")
    p.add_argument("--seed", type=int, default=None, help="random seed (optional)")
    p.add_argument("--low",  type=int, default=1,  help="min integer value for random data (default: 1)")
    p.add_argument("--high", type=int, default=12, help="max integer value for random data (default: 12)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    arr = make_array(args.rows, args.cols, args.seed, args.low, args.high)
    stats = compute_stats(arr)
    print_stats(arr, stats)


if __name__ == "__main__":
    main()
