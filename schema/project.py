class Project:
    def __init__(self, name):
        self.id = None
        self.name = name

    def __repr__(self):
        return f"Project(id={self.id}, name={self.name})"

    def get_metadata(self):
        return {
            "id": self.id,
            "name": self.name
        }