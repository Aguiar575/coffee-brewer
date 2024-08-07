# Pour Over Coffee Script

This Python script simulates pour-over coffee brewing. It guides you through the coffee brewing process by calculating the water amounts for each pour and timing the intervals between pours.

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python coffee_brewing.py
   ```

## Parameters

- `coffee_amount`: Amount of coffee in grams (default: 20g).
- `ratio`: Water-to-coffee ratio (default: 1:16).
- `delay_seconds`: Delay in seconds between each pour step (default: 45 seconds).

## Example

```python
coffee_amount = 20  # Coffee amount in grams
ratio = 16  # Water-to-coffee ratio (e.g., 1:16)
delay_seconds = 45  # Delay in seconds between pours

tetsu_kasuya_pour(coffee_amount, ratio, delay_seconds)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
