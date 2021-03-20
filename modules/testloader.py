from loadbase import LoadBase
from datetime import datetime

class TestLoader(LoadBase):

    def run(self):
        self.ShowHelloWorld()

    
    def ShowHelloWorld(self):
        print(f"{datetime.now()} => Hello World!")