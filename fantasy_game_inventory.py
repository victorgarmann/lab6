def display_inventory(d):
    inventory = "Inventory:"
    total = 0  
    for key, value in d.items():
        phrase = ("\n" + str(value) + " " + str(key))
        inventory = inventory + phrase
    for key, value in d.items():
        total += int(value)
    inventory += ("\n\n" + "Total number of items: " + str(total))
    
    return (inventory)
        

