# Longest Increasing and Decreasing Subsequence Finder

This project takes a permutation of unique integers and finds:

1. **The Longest Increasing Subsequence (LIS)**
2. **The Longest Decreasing Subsequence (LDS)**

## Problem Description
Given a positive integer `n (\leq 10000)` followed by a permutation `\pi` of length `n`, the task is to compute:
- One of the longest increasing subsequences of `\pi`
- One of the longest decreasing subsequences of `\pi`

### Example
**Input**
```
5
5 1 4 2 3
```

**Output**
```
1 2 3
5 4 2
```

## Approach
We use a dynamic programming approach:
- For LIS: we find the longest sequence where each number is greater than the previous
- For LDS: we find the longest sequence where each number is smaller than the previous

We also store the previous index for each element to reconstruct the actual subsequence.

## Files
- `main.py`: Python implementation to find LIS and LDS from the input sequence.
- `README.md`: Project documentation.

## How to Run
1. Ensure Python 3 is installed.
2. Run the script:
```bash
python main.py
```
3. Input the value of `n` followed by `n` integers.

## License
This project is open-source and free to use.

