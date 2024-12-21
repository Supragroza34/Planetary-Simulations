"""class Pokemon:

    def __init__(self, name, type1, type2, height, weight, sound, cry, attack):
        #All of these attributes will be public since there is no need to restrict these attributes within this class.
        #If attributes such as unique identification number of each pokemon was provided, that could be justified as a private attribute since we would not want it to be retrievable outside this class.
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.height = height
        self.weight = weight
        self.sound = sound
        self.cry = cry
        self.attack = attack

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_type1(self):
        return self.type1

    def set_type1(self, y):
        self.type1 = y

    def get_type2(self):
        return self.type2

    def set_type2(self,x):
        self.name = x

    def get_height(self):
        return self.height

    def set_height(self,x):
        self.name = x

    def get_weight(self):
        return self.weight

    def set_weight(self,x):
        self.weight = x

    def get_sound(self):
        return self.sound

    def set_sound(self,x):
        self.sound = x

    def get_cry (self):
        return self.cry

    def set_cry(self,x):
        self.cry = x

    def get_attack(self):
        return self.attack

    def set_attack(self,x):
        self.attack = x

# create an instance of the Pokemon
toxtricity = Pokemon("Toxtricity", "Electric", "Poison", 1.6, 40.0, "Zap Sound", "Cry Sound", "Thunderbolt")

# Example of using getters and setters:
#Name:
print(toxtricity.get_name())

#Change name and get it:
toxtricity.set_name("Pikachu")
print(toxtricity.get_name())


#all other attrubutes presented
print(toxtricity.get_cry(), ":this is cry")
print(toxtricity.get_weight(), ":this is weight")
print(toxtricity.get_attack(), ":this is attack")
print(toxtricity.get_sound(), ":this is sound")
print(toxtricity.get_type1(), ":this is type1")
print(toxtricity.get_type2(), ":this is type 2")
print(toxtricity.get_height(), ":this is height")"""











# Forming this into a super class
class Pokemon:

    def __init__(self, name, type1, type2): #Only chosen 3 attributes but I could have chosen all.
        #All of these attributes will be public since there is no need to restrict these attributes within this class.
        #If attributes such as unique identification number of each pokemon was provided, that could be justified as a private attribute since we would not want it to be retrievable outside this class.
        self.name = name
        self.type1 = type1
        self.type2 = type2

class Evolvable(Pokemon):
    #Once again nothing necessarily needs to be made private but some attributes like Evolvable could have been made private so that, that information is not retrievable.
    def __init__(self, name, type1, type2, evolvable): #Without specifying some attributes like evolvable, they will be automatically set to true
        super().__init__(name,type1, type2) # Here we inherit the attributes from the super clas which is 'Pokemon'
        self.evolvable = evolvable

    def get_evolve(self):
        return self.evolvable
    def set_evolve(self, x):
        self.evolvable = x


Pikachu = Evolvable("Pikachu","Electric", None, True)
print(Pikachu.get_evolve()) #Should output True
Pikachu.set_evolve(False)
print(Pikachu.get_evolve()) #Should print out false

