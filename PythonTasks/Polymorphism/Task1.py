class AirCastle:
    def __add__(self, n):
        self.cloud_count += n // 5
        self.height += n // 5
        return self

    def __init__(self, height, cloud_count, color):
        self.height = height
        self.cloud_count = cloud_count
        self.color = color

    def change_height(self, value):
        self.height = max(0, self.height + value)

    def __call__(self, transparency):
        return self.height // transparency * self.cloud_count

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.cloud_count} clouds"

    def __lt__(self, other):
        return (self.cloud_count, self.height, self.color) < (other.cloud_count, other.height, other.color)

    def __le__(self, other):
        return (self.cloud_count, self.height, self.color) <= (other.cloud_count, other.height, other.color)

    def __eq__(self, other):
        return (self.cloud_count, self.height, self.color) == (other.cloud_count, other.height, other.color)

    def __ne__(self, other):
        return (self.cloud_count, self.height, self.color) != (other.cloud_count, other.height, other.color)

    def __gt__(self, other):
        return (self.cloud_count, self.height, self.color) > (other.cloud_count, other.height, other.color)

    def __ge__(self, other):
        return (self.cloud_count, self.height, self.color) >= (other.cloud_count, other.height, other.color)

# Reading castles.txt and creating a list of AirCastle objects
castles_list = []
with open("castles.txt") as file:
    for line in file:
        values = line.split()
        try:
            height, cloud_count, color = map(int, values[:2]), int(values[2]), values[3]
            castles_list.append(AirCastle(height, cloud_count, color))
        except ValueError:
            print(f"Invalid line in castles.txt: {line}")

# Sorting the castles_list
castles_list.sort()

# Performing operations from operations.txt
with open("operations.txt", "r") as file:
    for line in file:
        values = line.split()
        if values:
            try:
                castle_num, operation, param = int(values[0]), values[1], int(values[2]) if len(values) > 2 else None
                if 0 <= castle_num < len(castles_list):
                    current_castle = castles_list[castle_num]

                    if operation == "change_height":
                        current_castle.change_height(param)
                    elif operation == "add":
                        current_castle.__add__(param)
                    elif operation == "call":
                        result = current_castle(param)
                        print(f"Result of calling castle {castle_num}: {result}")
                    elif operation == "print":
                        print(current_castle)
                else:
                    print(f"Invalid castle_num in line: {line}")
            except ValueError:
                print(f"Invalid line in operations.txt: {line}")