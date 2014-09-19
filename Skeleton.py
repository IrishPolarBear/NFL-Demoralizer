
class Skeleton:

    def __init__(self):
        self.Error = "None"

    def body(self, msg):
        main_menu = "Welcome to the beta version of the NFL demoralizer. Stay tuned " + \
                    "for more updates, including a GUI version, eventually.\nPlease choose " + \
                    " from one of the following options:\n1)Load Schedule\n2)Update Database" + \
                    "\n3)Select Team"
        if (msg == "Success"):
            print (main_menu)
        else:
            print ("Demoralizer Error: " + msg)
            options = 0
            return "Error"
        options = int(input("Which option would you like? "))
        while (options < 1 or options > 3):
            print ("Please enter a valid value between 1 and 3!")
            options = int(input("Which option would you like? "))
        
        print ("Success")
        
