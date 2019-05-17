from bs4 import BeautifulSoup
import requests

# Lookup DPCI using BrickSeek Target Inventory Checker
# 
# The DPCI is passed as a URL parameter. The item name is the 'title' of the
# resulting HTML.
# 
# input: dpci - string in format 123-45-6789
# output: Item name on success, None on failure
def get_name(dpci):
  try:
    res = requests.get('https://brickseek.com/target-inventory-checker/?sku=' + dpci)
  except requests.exceptions.RequestException as e:
    print(e)
    return None

  data = res.text
  # Use Beautiful Soup to parse the HTML for 'title'
  soup = BeautifulSoup(data, features="html.parser")

  item_name = soup.title.string

  # Remove extra info from item name
  extra_name = ' – Target Inventory Checker – BrickSeek'
  if item_name.endswith(extra_name):
    item_name = item_name[:-(len(extra_name))]
  else:
    # Item not found
    item_name = None

  return item_name

# Demo for DPCI lookup
if __name__ == "__main__":
  dpci = input("Enter DPCI: ")
  name = get_name(dpci)
  if name:
    print(name)
  else:
    print("Error retrieving item name.")
