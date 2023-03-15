class Person:
  height = 15
  age = 6
  name = "Кіт"
  is_Cat = True
  
  def __init__(self, surname):
    self.surname = surname
    print(self.name)
  
me = Person("Cat")
you = Person("Lol")

print(me.surname)
print(you.surname)