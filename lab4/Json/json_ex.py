import json

# read the JSON data from the file
with open('sample-data.json') as f:
    data = json.load(f)

# print the header
print('Interface Status')
print('=' * 80)
print('{:<50}{:<25}{:<8}{}'.format('DN', 'Description', 'Speed', 'MTU'))
print('-' * 80)

# loop over the data and print each row
for row in data['imdata']:
    dn = row['l1PhysIf']['attributes']['dn']
    desc = row['l1PhysIf']['attributes']['descr']
    speed = row['l1PhysIf']['attributes']['speed']
    mtu = row['l1PhysIf']['attributes']['mtu']
    print('{:<50}{:<25}{:<8}{}'.format(dn, desc, speed, mtu))
