class Queue:
    def __init__(self):
        self.customers: int = 0

    def add_customer(self):
        self.customers += 1

    def del_customer(self):
        self.customers -= 1

    def is_empty(self) -> bool:
        if self.customers > 0:
            return False
        return True
