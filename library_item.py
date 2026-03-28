class library_item:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checkedOut = False

    def get_title(self):
        return self.title

    def get_item_id(self):
        return self.item_id

    def is_checked_out(self):
        return self.checkedOut

    def check_out(self):
        if not self.checkedOut:
            self.checkedOut = True
            return True
        return False

    def return_item(self):
        if self.checkedOut:
            self.checkedOut = False
            return True
        return False
    
    def __str__ (self):
        return (f"title: {self.title}, item_id: {self.item_id}, checkedOut: {self.checkedOut}")