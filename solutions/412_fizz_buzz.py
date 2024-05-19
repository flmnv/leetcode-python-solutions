class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.create_string(i) for i in range(1, n + 1)]

    @staticmethod
    def create_string(i: int):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"

        return str(i)
