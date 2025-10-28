"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Khal Dogan
Date: 10/28/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
level = 1
user = input("What is your name and class(Warrior, Mage, Rogue, or Cleric)? separate with a comma: ")
characterInfo = user.split(",")
name = characterInfo[0].strip()
character_class = characterInfo[1].strip()

def calculate_stats(character_class, level):
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    if character_class == "Warrior":
        strength = 20 + (level * 5)
        magic = 5 + (level * 1)
        health = 120 + (level * 10)

    elif character_class == "Mage":
        strength = 6 + (level * 3)
        magic = 20 + (level * 9)
        health = 100 + (level * 4)

    elif character_class == "Rogue":
        strength = 14 + (level * 3)
        magic = 15 + (level * 4)
        health = 40 + (level * 1)

    elif character_class == "Cleric":
        strength = 2 + (level * 2)
        magic = 20 + (level * 8)
        health = 100 + (level * 11)
        
    return (strength, magic, health)
    pass

def create_character(name, character_class):
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    stats = calculate_stats(character_class, level)
    
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 150
    }
    
    return character
    pass

def save_character(character, filename):
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    
    with open(filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        return True
    pass

def load_character(filename):
    # TODO: Implement this function
    # Remember to handle file not found errors
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        character = {}
        
        for line in lines:
            key, value = line.strip().split(": ")
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
        return character
    pass

def display_character(character):
    # TODO: Implement this function
    
    with open(filename, 'r') as file:
        print("=== CHARACTER SHEET ===")
        print(f"Name: {character['name']}")
        print(f"Class: {character['class']}")
        print(f"Level: {character['level']}")   
        print(f"Strength: {character['strength']}")
        print(f"Magic: {character['magic']}")
        print(f"Health: {character['health']}")
        print(f"Gold: {character['gold']}")
    pass

def level_up(character):
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    
    for key in character:
        if key == "level":
            character[key] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength   
    character["magic"] = magic
    character["health"] = health
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")