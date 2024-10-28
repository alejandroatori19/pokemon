# It´s the class that manage the movements of the pokemons

class Movement:
    
    # ============================================
    # Attributes of the movement class
    # ============================================
    nameMovement = None
    descriptionMovement = None
    powerMovement = None
    accuracyMovement = None
    typeMovement = None
    categoryMovement = None
    powerPointsMovement = None
    priorityMovement = None
    
    # ============================================
    # Constructor of the movement class
    # ============================================
    def __init__ (self, nameM, descriptionM, powerM, accuracyM, typeM, categoryM, powerPointsM, priorityM):
        self.nameMovement = nameM
        self.descriptionMovement = descriptionM
        self.powerMovement = powerM
        self.accuracyMovement = accuracyM
        self.typeMovement = typeM
        self.categoryMovement = categoryM
        self.powerPointsMovement = powerPointsM
        self.priorityMovement = priorityM
        
        return
    
    # ============================================
    # Printer of information
    # ============================================
    def generic_printer_testing (self):
        print ("----- START MOVEMENT INFORMATION -----")
        print (f"\tName: {self.nameMovement}")
        print (f"\tDescription: {self.descriptionMovement}")
        print (f"\tPower: {self.powerMovement}")
        print (f"\tAccuracy: {self.accuracyMovement}")
        print (f"\tType: {self.typeMovement}")
        print (f"\tPP: {self.powerPointsMovement}")
        print (f"\tPriority: {self.priorityMovement}")
        
    # ============================================
    # Getters
    # ============================================  
    def get_movementName (self):
        return self.nameMovement
    
    def get_movementDescription (self):
        return self.descriptionMovement
    
    def get_movementPower (self):
        return self.powerMovement
    
    def get_accuracyMovement (self):
        return self.accuracyMovement
    
    def get_movementType (self):
        return self.typeMovement
    
    def get_movementCategory (self):
        return self.categoryMovement
    
    def get_movementPowerPoints (self):
        return self.powerPointsMovement
    
    def get_movementPriority (self):    
        return self.priorityMovement
    
    # ============================================
    # Logic behind movements
    # ============================================
    def reduce_power_points (self):
        self.powerPointsMovement -= 1
        
        return
        
    def could_be_used_movement (self):
        if self.powerPointsMovement > 0:
            return True
        else:
            return False