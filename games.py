class AboutMe():
    def __init__(self, name, age, school, Email, color ):
        self.name = name
        self.age = age
        self.school = school
        self.Email = Email
        self.color = color

class Clocked(AboutMe):
    def __init__(self, name, age, school, Email, color):
        super().__init__(name, age, school, Email, color)
        self.Email = Email

Me_1 = Clocked("Tyreese Lewis", 19, "Frankin Cummings Institution of Technology", "tybankss05@gmail.com", "blue")
print('My name:', Me_1.name)
print('My age:', Me_1.age)
print('My school:', Me_1.school)
print('My email:', Me_1.Email)
print('My fav color is:', Me_1.color)