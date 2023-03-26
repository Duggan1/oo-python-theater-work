from .audition import Audition

class Role:
    
    def __init__(self,character_name:str):
        self.character_name = character_name
        self.approved = []

    @property
    def auditions(self):
        return [a for a in Audition.all if a.role == self]
    
    
    @property
    def actors(self):
        return [a.actor for a in self.auditions]
    
    @property
    def locations(self):
        return [a.location for a in self.auditions]
    
    #exits loop after we find the first match

    @property
    def lead(self):
        theChosenOne = "no actor has been hired for this role"
        for a in self.auditions:

            if a.hired == True:
                theChosenOne = a.actor
                return theChosenOne
            
        return theChosenOne
    

    #list of "hired" actors


    @property
    def ranks(self):
        return [a.actor for a in self.auditions if a.hired == True]
    
    #these two methods organize them based on the order/ line 
    # they are listed in the debug python file
    @property
    def leadOne(self):
        if len(self.ranks) == 0:
            return "no actor has been hired for this role"
        else:
            return self.ranks[0]
    
    @property
    def understudy(self):
        if len(self.ranks) >= 2:
            return self.ranks[1]
        else:
            print("no actor has been hired for understudy for this role")


    #these two methods organize them based on the order the
    # callback() happens in the ipdb


    @property
    def leadApproved(self):
        if len(self.approved) == 0:
            return "no actor has been hired for this role"
        else:
            return self.approved[0]

    @property
    def understudyApproved(self):
        if len(self.approved) >= 2:
            return self.approved[1]
        else:
            print("no actor has been hired for understudy for this role")

