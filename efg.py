class Accio(Spell): 
    def __init__(self): 
    Spell.__init__(self, 'Accio', 'Summoning Charm') 
    
    def get_description(self): 
        return 'This charm summons an object to the caster, potentially over a significant distance'
