The Monostate pattern can be achieved in a very simple way in Python. In the
following code, we assign the __dict__ variable (a special variable of Python) with
the __shared_state class variable. Python uses __dict__ to store the state of every
object of a class. In the following code, we intentionally assign __shared_state to
all the created instances. So when we create two instances, 'b' and 'b1', we get two
different objects unlike Singleton where we have just one object. However, the object
states, b.__dict__ and b1.__dict__ are the same. Now, even if the object variable
x changes for object b, the change is copied over to the __dict__ variable that is
shared by all objects and even b1 gets this change of the x setting from one to four: