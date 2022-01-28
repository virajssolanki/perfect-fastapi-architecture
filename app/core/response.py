
class ResponseInfo:
    
    def __init__(self, data, message, success, status):
        self.data = data
        self.message = message
        self.success = success
        self.status = status

    def custom_success_payload(self):
        temp_custom_success = {
            "data": self.data,
            "message": self.message,
            "success": self.success,
            "status": self.status
        }
        return temp_custom_success