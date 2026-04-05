# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

class HelloGenLayer(gl.Contract):
    """Simple Intelligent Contract example for GenLayer"""
    
    greeting: str
    counter: int

    def __init__(self):
        self.greeting = "Welcome to GenLayer - AI Native Blockchain!"
        self.counter = 0

    @gl.public.view
    def get_greeting(self) -> str:
        """Returns the current greeting message"""
        return self.greeting

    @gl.public.write
    def update_greeting(self, new_greeting: str):
        """Updates the greeting message"""
        self.greeting = new_greeting

    @gl.public.write
    def increment_counter(self):
        """Increments the counter (demonstrates state change)"""
        self.counter += 1

    @gl.public.view
    def get_counter(self) -> int:
        """Returns the current counter value"""
        return self.counter
