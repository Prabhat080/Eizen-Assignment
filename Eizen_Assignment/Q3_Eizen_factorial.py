
from threading import Thread

class Factorial(Thread):
    def __init__(self,n):
        self.n = n
        self.factorial_value = None
        Thread.__init__(self)
    def factorial(self,n):
        if n <= 1:
            return 1
        return n * (self.factorial(n - 1))

    def run(self):
        self.factorial_value = self.factorial(self.n)


if __name__ == '__main__':

    n = int(input())
    thread = Factorial(n)
    thread.start()
    result = thread.factorial_value
    print(result)