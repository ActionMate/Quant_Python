all_guests = {'Diwakar':{'apples':5, 'cold_drink':10},
             'Sophina':{'cups':4, 'cookies':12},
             'Ryvex':{'sandwiches':8,'chocolate':6},
             'Zincc':{'air':1,'coin':2}}

def total_brought(guest,item):
    num_brought=0
    for k,v in all_guests.items():
        num_brought = num_brought + v.get(item,0)
    return num_brought


print('Number of things being brought:')
print(' - Apples      ' + str(total_brought(all_guests, 'apples')))
print(' - Cold Drinks ' + str(total_brought(all_guests, 'cold_drink')))
print(' - Cups        ' + str(total_brought(all_guests, 'cups')))
print(' - Sandwiches  ' + str(total_brought(all_guests, 'sandwiches')))
print(' - Cookies     ' + str(total_brought(all_guests, 'cookies')))
print(' - Chocolates  ' + str(total_brought(all_guests, 'chocolate')))
print(' - Nothing     ' + str(total_brought(all_guests, 'air')))
print(' - Coins       ' + str(total_brought(all_guests, 'coin')))