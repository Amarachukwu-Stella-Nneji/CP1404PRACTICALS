class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty members' collection."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({','.join([str(member) for member in self.members])})"

    def play(self):
        """Return a string showing the members' performance."""
        return "\n".join([member.play() for member in self.members])

    def add(self, member):
        """Add members."""
        self.members.append(member)
