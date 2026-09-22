import time

items={'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, 'dagger':1}

def display_inventory(inventory):
    dramatic_print("Your Inventory : ", 0.09)
    item_total=0
    for k,v in inventory.items():
        c=str(v)+k
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

def dramatic_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  


display_inventory(items)
dragon_loot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
user=input('There is a Dragon ahead! Do you want to fight the Dragon? (type anything to continue/leave blank to quit : ')
if user=='':
    print('Boys are not Brave')
else:
    dramatic_print("You fought the dragon bravely...", 0.09)
    items = add_to_inventory(items, dragon_loot)
    dramatic_print("After defeating dragon: ", 0.1)
    display_inventory(items)
    print('Men are Brave')