
import uuid

class Item:
    

# Wave 02
    def __init__(self, id=0):
        # self.id = id  -- wave 03 ?? -- no
        if id is 0:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__

# Wave 03
    def __str__(self):
        return f"An object of type Item with id {self.id}."