dynasties = { 1: "Smith" }
f = open("..\Crisis of the Confederation\common\dynasties\\00_dynasties.txt", 'r')
lines = f.readlines()
f.close()

for num, line in enumerate(lines):
    if "name = " in line:
        name = line.split('=')[1].strip()[1:-1]
        id = int(lines[num-1].split('=')[0].strip())
        culture = lines[num+1].split('=')[1].strip()
print(dynasties)

class Person:
    name = None
    dynasty = None
    def __init__(self, name="John", dynasty=1):
        self.name = name
        self.dynasty = dynasty

    def __str__(self):
        return self.name + ' ' #+ dynasties[self.dynasty]

if __name__ == "__main__":
    print(Person())
