
# custom exception handler 
class ExceptionHandler(Exception) : 
    def __init__(self, message, status_code = None):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        if self.status_code is None:
            error_info = f'{self.message}'
        else:
            error_info = f'{self.status_code} -> {self.message}'
        return error_info