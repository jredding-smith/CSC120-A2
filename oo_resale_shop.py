from computer import *

    # What attributes will it need?
class ResaleShop:
    inventory : list = [ ]





    # How will you set up your constructor?

    # Remember: in python, all constructors have the same name (__init__)
    def __init__ (self, shop_inventory : list): 
        self.inventory = shop_inventory

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

   #  # You'll remove this when you fill out your constructor

    # What methods will you need?

    # This method allows for the computer object, when bought for inventory in the shop, to be appened in the inventory list
    def buy(self, computer): 
        self.inventory.append(computer)

    # This method allows for the computer object, when selected to be sold from inventory, to be sold and removed from the inventory list. If the computer being sold doesnt exsist, the shop will inform you that it couldnt be found in the inverntory 
    def sell(self, computer): 
        if computer in self.inventory: 
            self.inventory.remove(computer)
        else:
          print("Computer could not be found. How about you try to buy a different computer?")


    def refurbish(self, computer, new_OS = None):
        if int(computer.year_made) < 2000: 
            computer.price = 0.0 
        elif int(computer.year_made) < 2012: 
            computer.price = 250.0
        elif int(computer.year_made) < 2018:
            computer.price = 550.0 
        else:
            computer.price = 1500.0 
        
            if new_OS is not None: 
                computer.operating_system = new_OS #update details after installing new OS 
            else:
                print("Computer not found. Please select another item to referbish")



    #prints and checks the inventory of the shop 
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for item in self.inventory:
            # Print its details
                print(f'{item.description} -- Processor Type: {item.processor_type} Hard Drive Capacity: {item.hard_drive_capacity} Memory: {item.memory} Operating System: {item.operating_system} Year Made: {item.year_made} price:  {item.price}')
        else:
            print("No inventory to display.")



def TestingIfWorks():

    mycomputer: Computer  = Computer("2019 MacBook Pro", "Intel", 256, 16, "Sequoia", 2019, 1000.00)
    othercomputer: Computer = Computer("2000 MacBook Air", "Intel", 256, 16, "High Sierra", 2010, 500.00)
    shop: ResaleShop = ResaleShop([])
    
    # Buying two computers for inventory 
    print(f"Buying, {mycomputer.description}")
    print("Adding to inventory...")
    shop.buy(mycomputer)
    print("Done.\n")

    print(f"Buying, {othercomputer.description}")
    print("Adding to inventory...")
    shop.buy(othercomputer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")


    # Updating price for other computer 
    print(f"lets update the price for {othercomputer.description}")
    othercomputer.updatePrice(1050.00)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")


    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing... updating OS to", new_OS)
    print("Updating inventory...")
    othercomputer.updateOS(new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    print("refurbishing computer/updating price based on age")
    shop.refurbish(mycomputer)
    print("Done.\n")
    
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling computer...")
    shop.sell(mycomputer)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")











      # Now, let's sell it!
    print("Selling computer...")
    shop.sell(mycomputer)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")




print("-"*20)
TestingIfWorks()
