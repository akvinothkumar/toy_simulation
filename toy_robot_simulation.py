class ToyRobot():
    toy_placed = False
    initial_action, x_axis, y_axis, face, action = '',0,0,'',''

    def get_inputs(self):
        n = int(input("Enter the n value for iteration: "))
        initial_action, x_axis, y_axis, face = input("Enter an input:  ").split(',')
        self.x_axis = int(x_axis)
        self.y_axis = int(y_axis)
        self.face = face.upper()
        self.initial_action = initial_action.upper()

        for i in range(n):   
            self.iteration = i
            if self.initial_action == 'PLACE':
                self.action = input("Enter action:").upper()
                self.toy_move_action()
            else:
                print("Initial command should have a keyword 'PLACE'")    

    def toy_move_action(self):
        # print("Reached function!!!!", self.initial_action, self.x_axis, self.y_axis, self.face, self.action)
        # if self.iteration == 0:
        if self.initial_action == 'PLACE' and not self.toy_placed:
            self.toy_placed = True

        if self.toy_placed:            
            if self.face == 'NORTH':
                if self.action == 'MOVE':
                    if self.x_axis < 4 and self.y_axis < 4:
                        self.y_axis = self.y_axis + 1

                if self.action == 'LEFT':
                    self.face = 'WEST'

                if self.action == 'RIGHT':
                    self.face = 'EAST'

            elif self.face == 'SOUTH':
                if self.action == 'MOVE':
                    if self.x_axis >= 0 and self.y_axis > 0:
                        self.y_axis = self.y_axis - 1

                if self.action == 'LEFT':
                    self.face = 'WEST'

                if self.action == 'RIGHT':
                    self.face = 'EAST'

            elif self.face == 'EAST':
                if self.action == 'MOVE':
                    if self.x_axis <= 4 and self.y_axis <=4:
                        self.x_axis = self.x_axis + 1

                if self.action == 'LEFT':
                    self.face = 'NORTH'

                if self.action == 'RIGHT':
                    self.face = 'SOUTH'

            elif self.face == 'WEST':
                if self.action == 'MOVE':
                    if self.x_axis > 0 and self.y_axis <=4:
                        self.x_axis = self.x_axis - 1

                if self.action == 'LEFT':
                    self.face = 'SOUTH'

                if self.action == 'RIGHT':
                    self.face = 'NORTH'

            if self.action == 'REPORT':
                print(f"OUTPUT:{self.x_axis},{self.y_axis},{self.face}") 
        
toy_robot = ToyRobot()
toy_robot.get_inputs()