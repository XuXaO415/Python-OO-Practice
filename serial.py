"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    
    __underscores__ are dunder methods -- allows you to customize the representation of a given object
    """
    
    def __init__(self, start=0):
        """Initializes serial generator"""
        self.start = self.next = start
        
    def __repr__(self):
        """__repr__ is a representation method"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
        
    def generate(self):
        """Generate next serial"""
        self.next +=1
        return self.next - 1
        
    def reset(self):
        """Resets serial generator to zero"""
        self.next = self.start

