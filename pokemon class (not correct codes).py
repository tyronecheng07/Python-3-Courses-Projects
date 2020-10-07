class Pokemon:
  def __init__(self, name, level, element_type, max_health, health, is_knock_out):
    self.name = name
    self.level = level
    self.element_type = element_type
    self.max_health = max_health
    self.health = health
    self.is_knock_out = is_knock_out
  
  def __repr__(self):
    return "{name} now has {health} health".format(name=self.name, health=self.health)
  
  def type_to_number(element_type):
    return {'grass':0, 'fire':1, 'water':2}[self.element_type]
  
  def attack(self, element_type, other_pokemon):
    my_element_type = type_to_number[element_type]
    other_element_type = type_to_number[other_pokemon]
    if (my_element_type - other_element_type) % 3 ==1:
        damage = (0.5*self.level)
    elif  my_element_type == other_element_type:
        damage = (0*self.level)
    else:
        damage = (2*self.level)
    return damage
  
  def lose_health(self, damage):
    return self.health - damage
  
  def gain_health(self, health_point):
    if  self.health > self.max_health:
      self.health = self.max_health
    else:
      return self.health + health_point
  
  def knock_out(self, health):
    if self.health <= 0:
      self.is_knock_out == True
      return "{name} got knocked out!".format(name=self.name, health=self.health)
    return self.is_knock_out
  
  class Trainer:
    def __init__(self, pokemons, name, portions, active_pokemon):
      self.pokemons = pokemons
      self.name = name
      self.portions = portions
      self.active_pokemon = active_pokemon
      
    def current_pokemon(self, pokemons, active_pokemon):
      current_pokemon = []
      for pokemon in self.pokemons:
        if self.active_pokemon == pokemon:
          current_pokemon.append(pokemon)
      return current_pokemon
      
     def attack_other_trainer(self, other_pokemon):
       if self.potions == 'healing':
          if self.active_pokemon.health >= 0 and other_pokemon.active_pokemon.health >= 0:
            self.active_pokemon.health += 10
          elif self.active_pokemon.health > self.active_pokemon.max_health:
            self.active_pokemon.health = self.active_pokemon.health
       print('{my_pokemon} got healed by trainer {name}.'.format(my_pokemon=self.active_pokemon.health, name=self.name))
       return self.active_pokemon.health
  
       if self.potions == 'reviving':
         if self.active_pokemon.health >= 0 and other_pokemon.active_pokemon.health >= 0:
          self.active_pokemon.health = (self.active_pokemon.health * 0.20)
       print('{my_pokemon} got revived by trainer {name}.'.format(my_pokemon=self_pokemon.health, name=self.name))
       return self.active_pokemon.health
      
       if self.potions == 'damaging':
          if other_pokemon.active_pokemon.health >= 0 and self.active_pokemon.health >= 0:
            other_pokemon.active_pokemon.health = other_pokemon.active_pokemon.health - 10
       print('{other_pokemon} got damaged by trainer {name}'.format(other_pokemon=other_pokemon.active_pokemon, name=self.name))
       return other_pokemon.active_pokemon.health
   
    

fire_pok = Pokemon("Pokemon fire", 2, 'fire', 100, 50, False)

water_pok = Pokemon("Pokemon water", 3, 'water', 100, 45, False)

grass_pok = Pokemon("Pokemon grass", 1, 'grass', 100, 40, False)


trainer_yoda = Trainer([fire_pok, water_pok, grass_pok], "Yoda", 3, fire_pok)

trainer_luke = Trainer([fire_pok, grass_pok], "Luke", 2, grass_pok)

trainer_obivan = Trainer([water_pok, grass_pok], "Obivan", 0, water_pok)
          
