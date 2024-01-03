## Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
#  but allows subclasses to alter the type of objects that will be created.

## Problem:
#  Imagine that you are creating a logistic management app and all your deliveries are made by trucks,
#  so yout code lives inside a "Truck" class.
#  After a while, you want to introduce sea delivery in your application and must create a "Ship" class,
#  and now you need to change all your code and add conditions to decide how to behave with each one class.

## Solution:
#  The Factory Method pattern suggests you to replace the direct object construction calls with calls to a special
#  factory method call. The "new" operator will be called from within the factory method.