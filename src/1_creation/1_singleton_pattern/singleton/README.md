Singleton provides you with a mechanism to have one, and only one, object of a
given type and provides a global point of access. Hence, Singletons are typically
used in cases such as logging or database operations, printer spoolers, and many
others, where there is a need to have only one instance that is available across the
application to avoid conflicting requests on the same resource. For example, we may
want to use one database object to perform operations on the DB to maintain data
consistency or one object of the logging class across multiple services to dump log
messages in a particular log file sequentially.
In brief, the intentions of the Singleton design pattern are as follows:
• Ensuring that one and only one object of the class gets created
• Providing an access point for an object that is global to the program
• Controlling concurrent access to resources that are shared