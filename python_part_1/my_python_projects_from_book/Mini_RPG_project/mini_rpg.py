import time

items={'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, 'dagger':1}

def display_inventory(inventory):
    print('Your Inventory : ')
    time.sleep(.2)
    item_total=0
    for k,v in inventory.items():
        print(v,k)
        time.sleep(.5)
        item_total=item_total+v
    print('Total items ',item_total)
    
def add_to_inventory(items, added_items):
    for a in added_items:
        if a in items:
            items[a] += 1
        else:
            items[a] = 1
    return items
        
display_inventory(items)
dragon_loot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
user=input('There is a Dragon ahead! Do you want to fight the Dragon? (type anything to continue/leave blank to quit : ')
if user=='':
    print('Boys are not Brave')
else:
    print('You fought the dragon bravely', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    items = add_to_inventory(items, dragon_loot)
    print('After defeating dragon: ')
    time.sleep(.5)
    display_inventory(items)
    print('Men are Brave')