# How-to Guide: Determining the Number of Digits in a String

## Objective:
In this guide, we will review two cases for a string: containing and not containing a digit.

### No Digit Case
```python
s = "HelloWorld"
has_digit = have_digits(s)
if has_digit:
    print("The string contains digits.")
else:
    print("The string does not contain digits.")
```

### Digit Case
```python
s = "Hello123"
has_digit = have_digits(s)
if has_digit:
    print("The string contains digits.")
else:
    print("The string does not contain digits.")
```