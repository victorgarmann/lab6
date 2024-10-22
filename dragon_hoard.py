from fantasy_game_inventory import display_inventory 

def add_to_inventory(inventory,added_items):
    new_inventory = inventory.copy()
    
    for item in added_items:
        if item in new_inventory:
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1   
    return new_inventory


inv = {"gold coin": 42, "rope": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "dagger", "gold coin", "ruby"]
updated_inv = add_to_inventory(inv, dragon_loot)
print(display_inventory(updated_inv))

        
        