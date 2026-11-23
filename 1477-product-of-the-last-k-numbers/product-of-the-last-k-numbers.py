class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 as a neutral base for multiplication
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any range including this 0 will have a product of 0,
            # so reset the prefix array to start fresh after the zero.
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is >= len(self.prefix), the last k numbers include
        # the most recent 0 that caused a reset.
        if k >= len(self.prefix):
            return 0
        
        # Divide total prefix product by the prefix product right before the last k elements
        return self.prefix[-1] // self.prefix[-1 - k]