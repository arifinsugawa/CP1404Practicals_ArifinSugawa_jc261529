class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self,name,ptype,reflection,year):
        self.name = name
        self.ptype = ptype
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.ptype.lower() == "static":
            return False
        else:
            return True

    def __str__(self):
        return "{},{} typing,reflection={},First appeared in {}".format(self.name,self.ptype,self.reflection,self.year)

