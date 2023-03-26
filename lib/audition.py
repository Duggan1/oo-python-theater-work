
# Auditions should have an actor (string), location (string), hired (boolean) and belong to a role.

class Audition:
    all = []


    def __init__(self, actor:str, location:str, role):
        self.actor = actor
        self.location = location
        self.hired = False
        self._role = role
        Audition.all.append(self)


    @property
    def role(self):
        return self._role
    
    def call_back(self):
        self.hired = True
        self.role.approved.append(self.actor)


    # i append to approved list to control the order 
    # inside ipdb rather than order of debug.py file