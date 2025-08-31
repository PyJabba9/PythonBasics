#Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory
#is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has.
#For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.



inv = {}
print('Weary traveller, list your inventory items:')
while True:
    print('Your item is:')
    i = input()
    if i =='':
        break
    print('And how many of ' + str(i) + '"s do you have?')
    q = input()
    q = int(q) # took me a while to understand why 1+2 of the same items gives 12 :D but i managed
    if q == '':
        break
    if i in inv:
        inv[i] += q # actually it was kind of hard to google, and I wasnt asking AI to help so got to it by myself, very proud :D
    inv.setdefault(i,q)


print('Weary traveller, your inventory now looks like that:')

for i, q in inv.items():
    print('Item:' + str(i) + ' Quantity: ' + str(q))
