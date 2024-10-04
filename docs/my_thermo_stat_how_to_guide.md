# How-to Guide: Switching the Thermostat to Different Modes

## Objective:
In this guide, we will review three different statuses of this thermostat.

### AC Mode:
```python
temp = 80
desired_temp = 70
status = my_thermo_stat(temp, desired_temp)
print(f'The thermostat status is: {status}')
```

### Heat Mode:
```python
temp = 70
desired_temp = 80
status = my_thermo_stat(temp, desired_temp)
print(f'The thermostat status is: {status}')
```

### Off Mode:
```python
temp = 77
desired_temp = 80
status = my_thermo_stat(temp, desired_temp)
print(f'The thermostat status is: {status}')
```