from dataclasses import dataclass , field
import numpy as np

@dataclass
class datapoint:
    x: float
    y: float
    z: float
    name: str

    def get_array(self):
        return np.array([self.x , self.y ,self.z] , dtype=float)

    def get_array_string(self):
        return (f"X {self.name} = {self.x} ; Y {self.name} = {self.y} ; Z {self.name } = {self.z}")

class Body:
    def __init__(self, ID ,  position_list , velocity_list = None , acceleration_list = None , mass = (7.3 * np.power(10.0, 22))):
        self.ID = ID
        self.mass = mass
        self.position_list = datapoint(position_list[0] , position_list[1] , position_list[2] , "Position")

        if velocity_list is None:
            self.velocity_list = datapoint(0,0,0 , "Velocity")
        else:
            self.velocity_list = datapoint(velocity_list[0] , velocity_list[1] , velocity_list[2] , "Velocity")

        if acceleration_list is None:
            self.acceleration_list = datapoint(0,0,0 , "Acceleration")
        else:
            self.acceleration_list = datapoint(acceleration_list[0], acceleration_list[1] , acceleration_list[2] , "Acceleration")

        self.force_list = datapoint(0,0,0, "Force")




class System:
    def __init__(self):
        self.G = 6.674 * np.power(10.0, -11)



    def calculate_force(self, body_list):
        body_count = (len(body_list))
        all_force = np.eye(body_count)
        for row in range(0, body_count - 1):
            for column in range(1 , body_count):
                print(row, column)





    def calculate_acceleration(self, body_list: Body):
        pass

    def step(self , timestep):
        pass

n1 = Body(1 , [0, 0, 0])
n2 = Body(2 , [1, 1, 1])
n3 = Body(3 , [2, 2, 2])

Sys = System()

Sys.calculate_force([n1, n2, n3])






print(n1.position_list.get_array_string())
print(n1.position_list.get_array())
print(n1.position_list.x)