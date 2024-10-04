# Tutorial: Adjusting the Thermostat Settings with `my_thermo_stat`

## Objective
In this tutorial, you will learn how to use the `my_thermo_stat` function to automatically change the thermostat status based on the current temperature and the desired temperature.

## Step-by-Step Guide

### Step 1: Define the current and desired temperatures
```python
temp = 60
desired_temp = 70
```

### Step 2: Call the `my_thermo_stat` function
```python
status = my_thermo_stat(temp, desired_temp)
```

### Step 3: Print the results
```python
print(f'The thermostat status is: {status}')
```