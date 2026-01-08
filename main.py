import random
import time

GRID_SIZE = 20
EMPTY = "."
PREDATOR = "D"
MONSTER = "M"


class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [[EMPTY for _ in range(size)] for _ in range(size)]

    def clear(self):
        for y in range(self.size):
            for x in range(self.size):
                self.cells[y][x] = EMPTY

    def place(self, x, y, symbol):
        self.cells[y][x] = symbol

    def display(self):
        for row in self.cells:
            print(" ".join(row))
        print()


class Agent:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def move(self):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.x = (self.x + dx) % GRID_SIZE
        self.y = (self.y + dy) % GRID_SIZE


class Predator(Agent):
    def __init__(self, x, y):
        super().__init__(x, y, health=100)

    def attack(self, monster):
        damage = random.randint(10, 25)
        monster.health -= damage
        print(f"Dek attacks monster for {damage} damage!")


class Monster(Agent):
    def __init__(self, x, y):
        super().__init__(x, y, health=150)

    def attack(self, predator):
        damage = random.randint(5, 20)
        predator.health -= damage
        print(f"Monster attacks Dek for {damage} damage!")


class Simulation:
    def __init__(self):
        self.grid = Grid(GRID_SIZE)
        self.predator = Predator(
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1)
        )
        self.monster = Monster(
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1)
        )

    def update_grid(self):
        self.grid.clear()
        self.grid.place(self.predator.x, self.predator.y, PREDATOR)
        self.grid.place(self.monster.x, self.monster.y, MONSTER)

    def run(self, turns=50):
        print("Starting Predator: Badlands Simulation\n")

        for turn in range(turns):
            print(f"--- Turn {turn + 1} ---")

            self.predator.move()
            self.monster.move()

            if self.predator.x == self.monster.x and self.predator.y == self.monster.y:
                self.predator.attack(self.monster)
                if self.monster.health > 0:
                    self.monster.attack(self.predator)

            self.update_grid()
            self.grid.display()

            print(f"Dek Health: {self.predator.health}")
            print(f"Monster Health: {self.monster.health}\n")

            if self.predator.health <= 0:
                print("Dek has been defeated. Simulation over.")
                return

            if self.monster.health <= 0:
                print("Dek defeated the monster and restored his honour!")
                return

            time.sleep(0.3)

        print("Simulation ended after maximum turns.")


if __name__ == "__main__":
    sim = Simulation()
    sim.run()
