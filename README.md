# DPCI Lookup - Find Target items using BrickSeek
A DPCI lookup designed for Target items

## Dependencies
- Beautiful Soup 4
  - install:
    ```
    $ pip3 install beautifulsoup4
    ```
- Requests
  - install:
    ```
    $ pip3 install requests
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
```
$ python3 dpci_lookup
```