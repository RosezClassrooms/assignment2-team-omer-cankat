from abc import ABC, abstractmethod  # For Builder classes
from enum import Enum
Components =Enum('','two_legs four_legs two_arms wings blades four_wheels two_wheels cameras infrared')

# Doesn't need an endless list of arguments when initialized
class Robot:
    # Uses a lot of flag logic here:  Is that necessary?
    # Does the use of this flag logic create other problems?
    def __init__(self,bipedal='',quadripedal='',wheeled='',flying='',traversal=[],detection_systems=[]):
        self.bipedal = bipedal
        self.quadripedal = quadripedal
        self.wheeled = wheeled
        self.flying = flying
        self.traversal = traversal
        self.detection_systems = detection_systems

    # Huge decision statement: why is this not good?
    # Can we improve this?
    def __str__(self):
      string = ""
      string += 'BIPEDAL' if self.bipedal else '' 
      string += 'QUADRIPEDAL' if self.quadripedal else '' 
      string += 'FLYING' if self.flying else '' 
      string += 'ROBOT ON WHEELS' if self.wheeled else '' 

      traversal = 'Traversal modules installed:\n' if self.traversal else '' 

      for module in self.traversal:
        traversal += "- " + str(module) + "\n"

      detection = 'Detection systems installed:\n' if self.detection_systems else ''

      for system in self.detection_systems:
        detection += "- " + str(system) + "\n" 

      info = (f'{string} ROBOT\n',f'{traversal}',f'{detection}') 
      return '\n'.join(info)



#----------------------------------------------------------------------------
# Note that this code was place at the top of this program for visibility
#from abc import ABC, abstractmethod


# The abstract superclass for all the builders
# We're using inheritence, but it's shallow
class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass
    
    def get_product(self):
      return self.product
      pass


# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
   

    def build_traversal(self):
        self.product.bipedal = True
        components = (Components.two_legs, Components.two_arms)
        self.product.traversal.append([t for t in components])
       

    def build_detection_system(self):
        self.product.detection_systems.append(Components.cameras)


# Concrete Builder class:  there would be many of these
class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
      self.product = Robot() 
    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
  

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(Components.four_wheels)

    def build_detection_system(self):
        self.product.detection_systems.append(Components.infrared)

class FlyingMonkeyRobotBuilder(RobotBuilder):
    def __init__(self):
       self.product = Robot()

    def reset(self):
       self.product = Robot()

    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
    # Fixed elevated to the superclass RobotBuilder

    def build_traversal(self):
        self.product.flying = True
        self.product.traversal.append(Components.wings)
        self.product.traversal.append(Components.two_arms)

    def build_detection_system(self):
        self.product.detection_systems.append(Components.cameras)
        self.product.detection_systems.append(Components.infrared)
#-------------------------------------------------------------------------
# Remove # in line above to comment out this section when using Director

# Using the builders to create different robots
#builder = AndroidBuilder()
#builder.build_traversal()
#builder.build_detection_system()
#print(builder.get_product())

#builder = AutonomousCarBuilder()
#builder.build_traversal()
#builder.build_detection_system()
#print(builder.get_product())

#-------------------------------------------------------
#  Keep line below whether testing builders or director
#-------------------------------------------------------


# Diretor manages all of the Builders
# Do we need separate make methods?
class Director:
    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_flying_monkey_robot(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()        


director = Director()

builder = AndroidBuilder()
print(director.make_android(builder))

builder = AutonomousCarBuilder()
print(director.make_autonomous_car(builder))

builder = FlyingMonkeyRobotBuilder()
print(director.make_flying_monkey_robot(builder))
# comment out line below when testing director
