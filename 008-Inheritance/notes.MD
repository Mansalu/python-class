# Inheritance and Polymorphism

**Inheritance** allows us to define a class that inherits the **attributes** and **methods** of another class often called the **parent class** or the **base class**.

The class that inherits from another class is called the **child class**.

Example: A class Student that inherits from a class called person.

## Creating a Child Class

Imagine there is a class called `Person`, we can create a more specific type of person,
a `Student` that inherits all of the attributes and methods a `Person` has:

    class Person:
        def __init__(self, name, age, genderIdentity):
            self.name = name
            self.age = age
            self.generIdentity = genderIdentity

    class Student(Person):
        def __init__(self, name, age, genderIdentity, major, GPA):
            Person.__init__(self, name, age, genderIdentity)
            self.major = major
            self.GPA = GPA

## Super() 

The parent class of a child class is also called its **Superclass**. In Python, we can use the `super()` to refer to the parent of a child and its attributes/methods. For example within `Student`, we can call the constructor of the parent class with ``super()` instead:

    class Student(Person):
        def __init__(self, name, age, genderIdentity, major, GPA):
            super().__init__(self, name, age, genderIdentity)
            self.major = major
            self.GPA = GPA

The result is the same here.

## Polymorphism

The idea that you can refer to a subclass as its superclass. Because the subclass inherits everything from its superclass, we can treat it the same. We won't deal with code examples of this just yet.