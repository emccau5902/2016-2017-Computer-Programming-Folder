import random

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, catch_rate, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.catch_rate = catch_rate
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file
        

        self.fainted = False
        self.current_health = health

    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                    
        return result

    def execute_move(self, move, target):
        available = self.get_available_moves()
        
        if self.fainted:
            print("Error: " + self.name + " is fainted!")
        elif move not in available:
            print("Error: " + move.name + " is not available.")
        else:
            r = random.randint(1, 100)

            if r <= move.accuracy:
                damage = move.calculate_damage(self, target)
                print(self.name + " hits " + target.name + " with " + move.name  + " for " + str(damage) + ".")
                target.take_damage(damage)
            else:
                print(move.name + "missed!")

            move.remaining_power -= 1

    def take_damage(self, amount):
        self.current_health -= amount
        
        if self.current_health <= 0:
            self.faint()

    def faint(self):
        self.current_health == 0
        self.fainted = True
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not to more than the base health.
        """
        self.current_health += amount

        if self.current_health > self.health:
            self.current_health = self.health
            print("Your pokemann was fully healed. Health is now " + self.current_health + "/" + self.health)

        self.fainted = False

    def restore(self):
        """
        Restores all health and resets powerpoint for all moves.
        """
        self.heal(self.health)
        remaining_power = powerpoint
    
    def draw(self):
        pass


class Move:
    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5
        
    effectiveness = {
            ('student' ,'administrator'): STRONG,
            ('student' ,'student'): NORMAL,
            ('student', 'teacher'): WEAK,
            ('teacher', 'student'): STRONG,
            ('teacher' ,'teacher'): NORMAL,
            ('teacher' ,'administrator'): WEAK,
            ('administrator' ,'teacher'): STRONG,
            ('administrator', 'administrator'): NORMAL,
            ('administrator', 'student'): WEAK
          }
                 
    def __init__(self, name, kind, powerpoint, power, accuracy):
        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = powerpoint

    def calculate_damage(self, attacker, target):

        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]

        return int(p * a / d * e)

    def restore(self):
        """
        Resets remaing_power to starting powerpoint.
        """
        self.heal(self.health)
        print("health restored")
        for m in self.moves:
            m.restore()
        print("Power restored")

class Character:
    
    def __init__(self, name, pokemann, image):
        self.name = name
        self.pokemann = pokemann
        self.image = image

    def get_available_pokemann(self):
        """
        Returns a list of all unfainted Pokemann belonging to a character.
        """
        output = []
        for n in self.pokemann:
            if n.fainted == False:
                output.append(n.name)
        print (output)
    
    def get_first_pokemann(self):
        """
        Returns the first [0] unfainted character in the pokemann list.
        """
        pass
    
    def set_first_pokemann(self, swap_pos):
        """
        Moves pokemann to first position [0] in the pokemann list by exchanging it with
        pokemann located at swap_pos.
        """
        pass
    
    def draw(self):
        pass

    
class Player(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)

        self.collection = []
        self.pokeballs = 0
        self.pokemann = pokemann

    def catch(self, target):
        """
        Can only be applied to wild pokemann. Determine a catch by generating a random
        value based on the target health. If a catch is successful, add the target to the
        player's collection. Decrease the player's pokeball count by 1 regardless of success.
        (Perhaps pokeballs kind could be incorporated into the probability at some point.)
        """
        r = random.randint(1, 100)

        if self.pokeballs!= 0:
            self.pokeballs -= 1
            if r <= target.catch_rate:
                if len(self.pokemann) > 6:
                    self.collection.append(target)
                    for n in self.collection:
                        n.restore()
                        print(target.name + " was added to your computer!")
                else:
                    self.pokemann.append(target)
                    print(target.name + " was added to your party!")
            else:
                print("It got away!")
        else:
            print("No pokeballs remaining!")

    def run(self, target):
        """
        Can only be applied in the presence of a wild pokemann. Success is determined by
        comparing speeds of the player's active pokemann and the wild pokemann. Incoroporate
        randomness so that speed is not the only factor determining success.
        Return True if the escape is successful and False otherwise.
        """
        r = random.randint(1,100)
        
        if self.pokemann.speed > target.speed and r <= 75:
            print("Ran away successfully")
        elif Player.pokemann.speed == target.speed and r <= 50:
            print("Ran away successfully")
        elif Player.pokemann.speed < target.speed and r <= 35:
            print("Ran away successfully")
        else:
            print("You tripped.")
    
class Opponent(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)
      

class Game:

    def __init__(self):
        pass

    def select_pokemann(self, character):
        """
        1) Generate a menu which shows a numbered list of all characters along with status (health).
        2) Have the player select a character.
        3) Move the selected character to position [0] in the characters list.
        """
        pass

    def select_random_pokemann(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        available_moves = pokemann.get_available_moves()
        return random.choice(available_moves)
    
    def select_move(self, pokemann):
        """
        1) Generate a menu which shows a numbered list all available moves for a pokemann.
        2) Have the player select a move.
        3) Return the selected move.
        """

        available = pokemann.get_available_moves()
        
        print("Select a move:")
        
        for i, move in enumerate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)
        
        return available[n]

    def select_random_move(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        pass

    def fight(self, player_pokemann, target_pokemann):
        """
        This controls the logic for a single round in a fight whether in context of a battle
        or with a wild pokemann.
        
        1. Select player_move (use select_move)
        2. Select target_move (use select_random_move)
        3. Compare speeds of player_pokemann and target_pokemann
            If player_pokemann.speed > target_pokemann.speed, set first = player_pokemann,
            second = target_pokemann. Otherwise, set first = target_pokemann, second = player_pokemann
            If speeds are equal, assign first and second randomly.
        4. Call
            first.execute_move(move, second)
        5. If second is still unfainted, call
            second.execute_move(move, first)

        (Once we have an actual game, we'll need to devise a way to remove fainted targets.)
        """
        pass

    def encounter(self, player, target):
        """
        This function controls all logic when encountering a wild pokemann. Options are to
        fight, catch, or ignore.

        Use a loop so that this continues until a pokemann is fainted, caught, or the
        target is ignored.
        """
        pass
    
    def battle(self, player, opponent):
        """
        This function controls all battle logic including decisions to reorder pokemann,
        fight, use potions, and whatever else happens in Pokebattles.

        Use a loop so that this continues until all characters for either the player or
        opponent are fainted.
        """
        pass
    
    def loop(self):
        pass
    
        # get input

        # do logic stuff

        # draw stuff


if __name__ == '__main__':
    
    # Make some moves
    homework = Move("Homework", "teacher", 30, 40, 100)
    pop_quiz = Move("Pop quiz", "teacher", 30, 40, 100)
    lecture = Move("Lecture", "teacher", 30, 40, 100)
    dress_code = Move("Dress Code", "administrator", 30, 50, 95)
    id_violation = Move("ID Violation", "administrator", 30, 50, 95)
    excessive_talking = Move("Excessive Talking", "student", 30, 40, 100)
    disruptive_behavior = Move("Disruptive Behavior", "student", 30, 40, 100)
    test_01 = Move("Null", "administrator", 100, 100, 100)

    # Create some Pokemann
    coopasaur = Pokemann("Coopasaur", "teacher", 30, 20, 50, 100, 40, [homework, pop_quiz, id_violation], "coopasaur.png")
    cookmander = Pokemann("Cookmander", "teacher", 30, 20, 50, 100, 40, [lecture, id_violation, homework], "cookmander.png")
    vincolairy = Pokemann("Vincolairy", "teacher", 30, 20, 50, 120, 40, [lecture, id_violation, homework], "vincolairy.png")
    mayfieldarow = Pokemann("Mayfieldarow", "administrator", 30, 20, 50, 90, 40, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("Andrewag", "student", 30, 20, 50, 150, 40, [excessive_talking, disruptive_behavior, homework], "andrewag.png")
    caseypuff = Pokemann("Caseypuff", "student", 30, 20, 50, 170, 40,[excessive_talking, disruptive_behavior, homework], "caseypuff.png")
    colboreon = Pokemann("Colboreon", "student", 30, 20, 50, 80, 40, [excessive_talking, disruptive_behavior, homework], "colboreon.png")
    blakachu = Pokemann("Blakachu", "student", 30, 20, 50, 130, 40, [excessive_talking, disruptive_behavior, homework], "blakachu.png")
    zoeotto = Pokemann("Zoeotto", "student", 30, 20, 50, 100, 40, [excessive_talking, disruptive_behavior, homework], "zoeotto.png")
    morganyta = Pokemann("Morganyta", "student", 30, 20, 50, 160, 40, [excessive_talking, disruptive_behavior, homework], "morganyta.png")
    katlevee = Pokemann("Katlevee", "student", 30, 20, 50, 140, 40, [excessive_talking, disruptive_behavior, homework], "katlevee.png")
    marcelax = Pokemann("Marcelax", "student", 30, 20, 50, 30, 40, [excessive_talking, disruptive_behavior, homework], "marcelax.png")
    place_holder = Pokemann("Place Holder", "administrator", 100, 100, 100, 100, 71, [id_violation, lecture, test_01], "place_holder.png")

    # Create Player
    pat = Player("Pat Riotum", [coopasaur, andrewag, caseypuff, blakachu], "pat.png")
    yaint = Player("You all are not", [place_holder, coopasaur, mayfieldarow], "yaint.png")

    # Create Opponents
    rocket = Opponent("Team Rocket", [colboreon, zoeotto, morganyta, cookmander], "rocket.png")
    jessie = Opponent("Jessie", [vincolairy, mayfieldarow, katlevee, marcelax], "jessie.png")

    # Create a game
    g = Game()
 
