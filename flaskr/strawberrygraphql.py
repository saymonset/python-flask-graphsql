import strawberry
from typing import List
 

@strawberry.type
class TodoType:
    name: str
    done: bool
    
     
todos = [
  TodoType(name="Todo #1", done=False),
  TodoType(name="Todo #2", done=False),
  TodoType(name="Todo #3", done=True)
]

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Query:
    @strawberry.field
    def todos(self, info, done: bool = None) -> List[TodoType]:
        if done is not None:
            return filter(lambda todo: todo.done == done, todos)
        else:
            return todos
    
    
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)
 


 
    



    
    
schema = strawberry.Schema(query=Query)