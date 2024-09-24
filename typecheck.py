
def division(x:int, y:int) -> int:
    return (x//y)

a=division(10,2)
print (a)

b=division(5,2.5)
print (b)

c=division("Hello",10)
print (c)

x: int = 3
y: float = 3.14
my_name: str ='abc'
status: bool = False
names: list = ['a','b','c']
marks: tuple = (10, 20, 30)
marklist: dict = {'a':10,'b':20,'c':30}

from typing import List, Tuple, Dict

cities: List[str] = ['b','f']
employee: Tuple[str,int,float] = ('g',4,6.0)
markdict: Dict[str, int] = {'c':3,'w':5}
