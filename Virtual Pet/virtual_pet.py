class Pet():
    
    def __init__(self, name):
        self.name = name
        self.energy = 7 
        self.is_alive = True
        
    def sleep(self):
        if self.is_alive == False:
            print(self.name + ' cant sleep if theyre dead.')
        print(self.name + "': zzzzz'")
        self.energy = 10
        
    def eat(self):
        if self.is_alive == False:
            print(self.name + ' cant eat if theyre dead.')
        if self.energy <= 8:
            self.energy += 2
            print(self.name + ": 'nom nom nom'")
        elif self.energy == 9:
            self.energy += 1
            print(self.name + ": 'nom nom nom'")
        elif self.energy == 10:
            print(self.name + ' is not hungry right now.')
            
    def play(self):
        if self.is_alive == False:
            print(self.name + ' cant play if theyre dead.')
        if self.is_alive == True:
            print(self.name + ' is running around')
            self.energy -= 1
        if self.energy == 1:
            print(self.name + ' is becoming lethargic, it needs some food.')
        if self.energy <= 0:
            self.die()

    def die(self):
        print(self.name + ' has died.')
        self.is_alive = False

    def battle(self, other):
        print(self.name + " murders " + other.name + ".")
        other.die()

