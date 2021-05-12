class DataError(Exception):
    def __init__(self):
        self.message = "Error loading data"
