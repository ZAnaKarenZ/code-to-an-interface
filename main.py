"""
Ana Karen Zetter
Code that generates a biome with animals. Each animal makes a different sound and this is achieved with polimorfism. 
The principle of "Programming to an interface, not an implementation." is applied in this project: 
    Instead of creating multiple concrete animal classes, each with their own method, 
    they all override the makeSound method of an abstract animal class.
"""

from abc import ABC, abstractmethod

#Abstract interface
class Animal:
    @abstractmethod
    def makeSound(self):
        pass

#Concrete classes
class Bird(Animal):
    def makeSound(self):
        print("Chirp, chirp!")

class Fish(Animal):
    def makeSound(self):
        print("Glub, glub")


#Abstract class
class Biome:
    @abstractmethod
    def getAnimals(self):
        pass

#Concrete classes
class TemperateDeciduousForest(Biome):
    def getAnimals(self):
        return [Bird(), Fish()]

class CoralReef(Biome):
    def getAnimals(self):
        return [Fish()]


#Main function

    #Forest
    forest = TemperateDeciduousForest()
    for animal in forest.getAnimals():
        animal.makeSound()
