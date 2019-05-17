# DPCI Lookup - Find Target items using [BrickSeek](https://brickseek.com/target-inventory-checker/)

A DPCI lookup designed for Target items

## Dependencies

- Beautiful Soup 4
  - install:

    ```bash
    pip3 install beautifulsoup4
    ```

- Requests
  - install:

    ```bash
    pip3 install requests
    ```

## Usage

```python
import dpci_lookup

name = dpci_lookup.get_name("123-45-6789")
if name:
  print(name)
else:
  print("Error retrieving item name.")
```

## Demo

Run the demo with:

```bash
python3 dpci_lookup
```
