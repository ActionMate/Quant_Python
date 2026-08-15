items={'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, 'dagger':1}

def display_inventory(inventory):
    print('Inventory : ')
    item_total=0
    for k,v in inventory.items():
        print(v,k)
        item_total=item_total+v
    print('Total items ',item_total)
def add_to_inventory(items, added_items):
    for item in added_items:
        items[item] = items.get(item, 0) + 1
    return items
display_inventory(items)
dragon_loot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
items = add_to_inventory(items, dragon_loot)
print('\nAfter defeating the dragon:')
display_inventory(items)