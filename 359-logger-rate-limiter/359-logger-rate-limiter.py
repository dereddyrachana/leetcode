class Logger:

    def __init__(self):
        self.messages = {}  

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # print(self.messages)
        if message not in self.messages:
            self.messages[message] = timestamp + 10
            return True
        else:
            if(self.messages[message] > timestamp):
                return False
            else:
                self.messages[message] = timestamp + 10
                return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)