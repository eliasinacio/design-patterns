## Factory Method 

#  Is a creational design pattern that provides an interface for creating objects in a superclass,
#  but allows subclasses to alter the type of objects that will be created.

## Problem:
#  Imagine that you are creating a logistic management app and all your deliveries are made by trucks,
#  so yout code lives inside a "Truck" class.
#  After a while, you want to introduce sea delivery in your application and must create a "Ship" class,
#  and now you need to change all your code and add conditions to decide how to behave with each one class.

## Solution:
#  The Factory Method pattern suggests you to replace the direct object construction calls with calls to a special
#  factory method call. The "new" operator will be called from within the factory method.

## Pros:
#  - Prevents a hard coupling between the creator (Factory) and the products (subclasses).
#  - Single Responsability Principle - We can move the creational code to a local facilitating the code support.
#  - Open/Closed Principle - We can introduce new types of products in our program without breaking or hard changing old code.

## Cons:
#  - The code can turn more complicated, cause we need to introduce very new subclasses to implements the pattern. The best way is 
#    to introduce the pattern into an existing class creatin hierarchy.

## Example:
from abc import ABC, abstractmethod
from typing import Dict

class DatabaseInterface(ABC):
    @abstractmethod
    def select_one(self):
        pass

class MySqlRepository(DatabaseInterface):
    def select_one(self) -> Dict:
        return {
            'success': True,
            'data': 'hello world'
        }
    
class UseCase:

    def __init__(self, repository):
        pass