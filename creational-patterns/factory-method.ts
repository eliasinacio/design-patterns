/*
 * Factory Method *

  Is a creational design pattern that provides an interface for creating objects in a superclass,
  but allows subclasses to alter the type of objects that will be created.

  Problem:

  Imagine that you are creating a logistic management app and all your deliveries are made by trucks,
  so yout code lives inside a "Truck" class.
  After a while, you want to introduce sea delivery in your application and must create a "Ship" class,
  and now you need to change all your code and add conditions to decide how to behave with each one class.

  Solution:

  The Factory Method pattern suggests you to replace the direct object construction calls with calls to a special
  factory method call. The "new" operator will be called from within the factory method.

  Pros:

  - Prevents a hard coupling between the creator (Factory) and the products (subclasses).
  - Single Responsability Principle - We can move the creational code to a local facilitating the code support.
  - Open/Closed Principle - We can introduce new types of products in our program without breaking or hard changing old code.

  Cons:

  - The code can turn more complicated, cause we need to introduce very new subclasses to implements the pattern. The best way is 
    to introduce the pattern into an existing class creatin hierarchy.
 */

/** 
 * Example: 
 * 
 * A class that creates orders in a website.
 */

class Book {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }

  private id: number;
  private name: string;
  private pages: number;
  
  getId = () => { return this.id }
  getName = () => { return this.name }

  setPages = (quantity: number) => {
    this.pages = quantity;
  }

  createBook(type: string) {
   return null;
  }
}

class PhisicalBook extends Book {
  constructor (id, name, weight) {
    super(id, name);

    this.weight = weight;
  }

  private weight: number;
} 

class DigitalBook extends Book {
  constructor (id, name, size) {
    super(id, name);

    this.size = size;
  }

  private size: number;
} 