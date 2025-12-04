import random #För att möjligöra så att det blir "dicethrow" på hur mycket skada attacken kommer göra
class spell:
        def __init__(self, name, spell_type, min_range, max_range):
            self.name = name
            self.spell_type = spell_type
            self.min_range = min_range
            self.max_range = max_range
        
        def cast(self):
            return random.randint(self.min_range, self.max_range)
    
flame = spell("Flame", "damage", 18, 25)
risky_flame = spell ("Risky flame", "damage", 10, 35)
heal = spell("Heal", "heal", 18, 25)
