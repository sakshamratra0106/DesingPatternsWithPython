[//]: # (https://www.geeksforgeeks.org/strategy-method-python-design-patterns/)

#Advantages

1. Open/Closed principle: Its always easy to introduce the new strategies without changing the client’s code.
2. Isolation: We can isolate the specific implementation details of the algorithms from the client’s code.
3. Encapsulation: Data structures used for implementing the algorithm are completely encapsulated in Strategy classes. Therefore, the implementation of an algorithm can be changed without affecting the Context class
4. Run-time Switching: It is possible that application can switch the strategies at the run-time.


#Dis-Advantages

5. Creating Extra Objects: In most cases, the application configures the Context with the required Strategy object. Therefore, the application needs to create and maintain two objects in place of one.
6. Awareness among clients: Difference between the strategies should be clear among the clients to able to select a best one for them.
7. Increases the complexity: when we have only a few number of algorithms to implement, then its waste of resources to implement the Strategy method.