class Task:
    def __init__(self, title: str, description: str, complexity: int):
        self.title = title
        self.description = description
        self.complexity = complexity
        self.completed = False

    def __repr__(self):
        return self.title

    def complete(self):
        self.completed = True
        print(f'{self} completed')
