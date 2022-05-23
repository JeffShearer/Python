#basically - set a template for how the object should be construct it - note "class" is a protected word in python.

class PartyAnimal:
    x = 0
    #Then define a method using "def", in this case, increment X by 2 and print. 
    def party(self):
        self.x = self.x + 2
        print(self.x)
# then construct that object into a new variable so it can be called later. 
an = PartyAnimal()
#then call that new variable and the party method you defined above. 
an.party()
an.party()



#example with distinct objects in their own variables

class PartyAnimal:
    x = 0
    name = ''
    # the def statement below is a "constructor" that initializes the self & name parameters.
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

#When you dewfine your variables, you can create independence instances of the object. 
q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()


# And finally there's inheritance with subclasses for more granular use cases.

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

#This subclass inherits all the properties of Party Animal, and adds more.
class FootballFan(PartyAnimal) :
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)


j = FootballFan("Jim")
# Then when you call this class for Jim's instance, both the party method fires as well as the new touchdown method in the subclass
j.party()
j.touchdown()