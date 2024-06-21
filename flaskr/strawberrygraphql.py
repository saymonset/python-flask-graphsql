import strawberry
from typing import List
import random
from typing import Optional
 

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
class Hello:
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def todos(self, info, done: bool = None) -> List[TodoType]:
        if done is not None:
            return filter(lambda todo: todo.done == done, todos)
        else:
            return todos
    
    @strawberry.field(name="randomFromZeroTo", description="From zero to argument TO (default 6)")
    def get_random_from_zero_to(self, to: Optional[int] = 6) -> int:
        return random.randint(0, to)

    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

    @strawberry.field
    def helloWorld(self) -> Hello:
        return Hello(name="Hola mundo")

    @strawberry.field(name="helloWorldSimon", description="Hola Mundo es lo que retorna")
    def hello(self) -> str:
        return "Hola mundo"
 


 
    



    
    
schema = strawberry.Schema(query=Query)