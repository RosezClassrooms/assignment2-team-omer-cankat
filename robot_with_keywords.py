# In order to only give values for relevant attributes, you must
#   use some form of keyword argument initialization
# However, all of the attributes must be given default values
# Keep in mind that in a real application, these would be endless ...

# Is there any danger in having users decide which attributes to specify?
# What about organization and readability?  Should they all be in one place?
# Even if you didn't apply Builder, are there ways to improve this
#   keyword implementation?
from abc import ABC, abstractmethod

class Robot:
  def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []
  """"      
  def __init__(self, bipedal = None, quadripedal = None, wheeled = None,
             flying = None, traversal = [], detection_systems = []):
    self.bipedal = bipedal
    self.quadripedal = quadripedal
    self.wheeled = wheeled
    self.flying = flying
    self.traversal = traversal
    self.detection_systems = detection_systems
 """
  # This is still awful!  What should we do about it??
  def __str__(self):
    string = ""
    if self.bipedal:
      string += "BIPEDAL "
    if self.quadripedal:
      string += "QUADRIPEDAL "
    if self.flying:
      string += "FLYING ROBOT "
    if self.wheeled:
      string += "ROBOT ON WHEELS\n"
    else:
      string += "ROBOT\n"

    if self.traversal:
      string += "Traversal modules installed:\n"

    for module in self.traversal:
      string += "- " + str(module) + "\n"

    if self.detection_systems:
      string += "Detection systems installed:\n"

    for system in self.detection_systems:
      string += "- " + str(system) + "\n"

    return string

#---------------------------------------------------------------------------

# Concrete component classes
# If they are defined at this level, they would multiply like rabbits in a
#   real system, and would have an endless list of subcomponents also
# Are there better ways to manage all these components?
class BipedalLegs:
  def __str__(self):
    return "two legs"

class QuadripedalLegs:
  def __str__(self):
    return "four legs"

class Arms:
  def __str__(self):
    return "two arms"

class Wings:
  def __str__(self):
    return "wings"

class Blades:
  def __str__(self):
    return "blades"

class FourWheels:
  def __str__(self):
    return "four wheels"

class TwoWheels:
  def __str__(self):
    return "two wheels"

class CameraDetectionSystem:
  def __str__(self):
    return "cameras"

class InfraredDetectionSystem:
  def __str__(self):
    return "infrared"


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

    #elevated to the superclass
    def get_product(self):
        return self.product
        pass
  
  
class AndroidBuilder(RobotBuilder):
  
    def __init__(self):
      self.product = Robot()
  
    def reset(self):
      self.product = Robot()

# All of the concrete builders have this in common
# Should it be elevated to the superclass?
#Fixed elevated to the superclass RobotBuilder  

    def build_traversal(self):
      self.product.bipedal = True
      self.product.traversal.append(BipedalLegs())
      self.product.traversal.append(Arms())

    def build_detection_system(self):
      self.product.detection_systems.append(CameraDetectionSystem())     

class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
    # Fixed elevated to the superclass RobotBuilder 

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())

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
        self.product.traversal.append(Wings())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())
        self.product.detection_systems.append(CameraDetectionSystem())

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

# Constructing robots by providing only relevant attributes
# Note that when providing attributes via keyword, order doesn't matter!
# Is there a danger here??

