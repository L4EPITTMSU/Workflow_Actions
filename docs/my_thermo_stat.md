::: functions.my_thermo_stat

# My Thermostat Function

The function `my_thermo_stat` adjusts the thermostat based on the current temperature compared to a desired temperature.

## Parameters

- `temp` (int): The current temperature.
- `desired_temp` (int): The desired temperature.

## Returns

- str: The status of the thermostat. It can be 'Heat', 'AC', or 'off'.

## Example

```python
print(my_thermo_stat(20, 25))  # Output: 'Heat'
