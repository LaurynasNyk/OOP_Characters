class Character:
  name = None
  health = None
  MP = None
  def __init__(self,name,health,MP):
    self.name = name
    self.health = health
    self.MP = MP
class Player(Character):
  Lives = None
  def __init__(self,name,health,MP,Lives):
    self.name = name
    self.health = health
    self.MP = MP
    self.Lives = Lives
  def alive(self,health):
    if self.health <= 0:
      return "No"
    else:
      return "Yes"
  def Print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.MP}\nLives: {self.Lives}")
    if self.alive(self.health) =="Yes":
      print("Alive?: Yes")
    else:
      print("Alive?: No")
class Enemy(Character):
  Type = None
  Strength = None
  def __init__(self,name,health,MP, Type, Strength):
    self.name = name
    self.health = health
    self.MP = MP
    self.Type = Type
    self.Strength = Strength
class Orc(Enemy):
  Speed = None
  def __init__(self,name,health,MP, Type, Strength, Speed):
    self.name = name
    self.health = health
    self.MP = MP
    self.Type = Type
    self.Strength = Strength
    self.Speed = Speed
  def Print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.MP}\nType: {self.Type}\nStrength: {self.Strength}\nSpeed: {self.Speed}")
class Vampire(Enemy):
  DayNight = None
  def __init__(self,name,health,MP, Type, Strength, DayNight):
    self.name = name
    self.health = health
    self.MP = MP
    self.Type = Type
    self.Strength = Strength
    self.DayNight = DayNight
  def Print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.MP}\nType: {self.Type}\nStrength: {self.Strength}\nDay/Night?: {self.DayNight}")

Play = Player("John", 50,50,3)
Play.Print()
print()
Or = Orc("OGRE", 60,70,"Water","Fire",20)
Or.Print()
print()
Vam = Vampire("Drac",20,30,"Fire","Water","Night")
Vam.Print()