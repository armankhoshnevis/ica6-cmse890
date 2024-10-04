# Reference: Thermostat Status with `my_thermo_stat`

## Function signiture
```python
def my_thermo_stat(temp: int, desired_temp: int) -> str:
```
## Description:
The `my_thermo_stat` function takes the current temperature and desired temperature as inputs and returns the status of the thermostat as a string. The function determines whether the thermostat should turn on the heat, activate the air conditioning, or remain off based on the difference between the two temperatures.

## Parameters:
- `temp (int)`: The current temperature.
- `desired_temp (int)`: The desired temperature to reach.

## Returns:
- status (str): The status of the thermostat, which can be one of the following:
    - "Heat": If the current temperature is more than 5 degrees lower than the desired temperature.
    - "AC": If the current temperature is more than 5 degrees higher than the desired temperature.
    - "off": If the current temperature is within 5 degrees of the desired temperature.