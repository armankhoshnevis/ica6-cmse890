# Tutorial: Checking for Digits in a String Using `have_digits`

## Objective
In this tutorial, you will learn how to use the `have_digits` function to check whether a string contains any digits.

## Step-by-Step Guide

### Step 1: Define a string
```python
s = "Hello123"
```

### Step 2: Call the `have_digits` function
```python
has_digit = have_digits(s)
```

### Step 3: Print the results
```python
if has_digit:
    print("The string contains digits.")
else:
    print("The string does not contain digits.")
```