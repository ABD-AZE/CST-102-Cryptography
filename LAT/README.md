# Linear Approximation Table (LAT)

This repository contains a Python implementation for generating a Linear Approximation Table (LAT) . The code evaluates the relationships between input coefficients (`a`) and output coefficients (`b`) based on specific transformations defined by the functions `y1`, `y2`, `y3`, and `y4`.

## Overview

The primary goal of this implementation is to compute the LAT, which helps in analyzing the behavior of a cryptographic function under linear attacks. The LAT is constructed by iterating over all possible input-output coefficient pairs and calculating the corresponding transformations.

## Functions

### y1(x)
Calculates a specific transformation based on a 4-bit input `x`.

#### Parameters:
- `x`: A string representing a 4-bit binary number.

#### Returns:
- An integer representing the result of the transformation.

### y2(x)
Calculates another transformation similar to `y1`.

#### Parameters:
- `x`: A string representing a 4-bit binary number.

#### Returns:
- An integer representing the result of the transformation.

### y3(x)
Calculates yet another transformation.

#### Parameters:
- `x`: A string representing a 4-bit binary number.

#### Returns:
- An integer representing the result of the transformation.

### y4(x)
Calculates a final transformation.

#### Parameters:
- `x`: A string representing a 4-bit binary number.

#### Returns:
- An integer representing the result of the transformation.

## Linear Approximation Table (LAT)

The main script constructs a 16x16 Linear Approximation Table (LAT). The LAT is filled based on the relationships between the coefficients of the input (`a`) and output (`b`) as well as transformations applied to the binary input `x`.

### Key Variables
- `LAT`: A 2D list initialized to zero, representing the LAT.
- `bo`: The output coefficient (binary output).
- `ao`: The input coefficient (binary input).
- `xo`: The binary input value.

### Logic Overview
The script iterates over all possible values of input coefficients (`ao`), output coefficients (`bo`), and their corresponding transformed input values (`xo`). For each combination, it computes the transformations and updates the LAT based on specific conditions involving the coefficients and transformations.

## Output
The script prints the LAT and computes the maximum and minimum values found in the table.

