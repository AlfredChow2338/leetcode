from abc import ABC, abstractmethod

# The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Truck()
