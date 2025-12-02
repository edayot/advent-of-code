

class Dial():
    def __init__(self) -> None:
        self._dial = 50
        self.zero_counter = 0

    def rotate(self, rotate: str):
        direction = {"L": -1, "R": 1}[rotate[0]]
        amount = int(rotate[1:])
        while amount > 0:
            self._dial += direction
            amount -= 1

            if self._dial == 100:
                self._dial = 0
            if self._dial == -1:
                self._dial = 99

            if self._dial == 0:
                self.zero_counter += 1
        


    
    def __repr__(self) -> str:
        return f"dial = {self._dial}, {self.zero_counter}"
    
    def __str__(self) -> str:
        return f"dial = {self._dial}, {self.zero_counter}"




dial = Dial()
print(dial)
with open("2025/day1/input.txt", "r") as f:
    data = f.readlines()

for line in data:
    instruction = line.strip()
    if instruction:
        dial.rotate(instruction)
        print(dial, instruction)


print(dial)