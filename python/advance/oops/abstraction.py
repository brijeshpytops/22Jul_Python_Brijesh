from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class dog(animal):
    def voice(self):
        return "Bho Bho"
    
class cat(animal):
    def voice(self):
        return "meow meow"
    
obj = dog()
print(obj.voice())
obj = cat()
print(obj.voice())