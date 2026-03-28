import library_item


class DVD(library_item):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
       

    def get_duration(self):
        return self.duration
    
    def __str__ (self):
        return f"{super().__str__()}, duration: {self.duration} minutes"