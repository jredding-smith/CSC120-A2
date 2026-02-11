class Computer: 
    # What attributes will it need?
    description : str = "" 
    processor_type : str = "" 
    hard_drive_capacity : int = 0 
    memory : int = 0
    operating_system : str = "" 
    year_made : int = 0 
    price : float = 0.0 

    # How will you set up your constructor?

    # Remember: in python, all constructors have the same name (__init__) 
    def __init__ (self, disc : str, processor : str, hard_drive : int, mem: int , OS: str, year : int, amt : float): 
       self.description = disc 
       self.processor_type = processor
       self.hard_drive_capacity = hard_drive
       self.memory = mem
       self.operating_system = OS 
       self.year_made = year
       self.price = amt 

    

    # What methods will you need?

    # manually update the price of the computer of choice 
    def updatePrice(self, amt: float): 
        self.price = amt 
        return(f"{self.description} price is now {amt}")
    
    # manually update the OS of the computer of choice 
    def updateOS(self, OS: str): 
        self.operating_system = OS
        return(f"{self.description} new updated OS is now {OS}")
    
def main(): 

    # All below hastash's were for checking code : 
        # mycomputer:Computer  = Computer("2019 MacBook Pro", "Intel", 256, 16, "Sequoia", 2019, 1000.00)
        # print(mycomputer.price)
        # print(mycomputer.updatePrice(20000.00))
        # print(mycomputer.price) 
        # print(mycomputer.updateOS("MacOS Monterey"))
        # print(mycomputer.operating_system)
        #mycomputer:Computer  = Computer("2019 MacBook Pro", "Intel", 256, 16, "Sequoia", 2019, 1000.00)
        #print(mycomputer.price)
    pass



print("-"*20)
