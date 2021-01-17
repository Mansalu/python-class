# Inheritance

"""
Consider the game Minecraft, which has many types of blocks
within the world. Minecraft is an incredibly extensible (easy to mod)
game, in part, because of inheritance. If a mod wants to add a new type of block
it can easily inherit Minecraft's base "block" class, and the core mechanics
of the world will "just work". Allowing the mod to focus on what it actually wants to add.
"""

# Files example
# A file has {path, created, }

class File:
    def __init__(self, path, created, modified):
        self.path = path
        self.created = created
        self.modified = modified
    def Open(self):
        print("Opened the file...")
    def __str__(self):
        return self.path
        
class PDF(File):
    def __init__(self, path, created, modified, text, metadata):
        super().__init__(self, path, created, modified)
        self.text = text
        self.metadata = metadata
    def Open(self):
        print("Opened the PDF...")

class VideoFile(File):
    def __init__(self, path, created, modified, content):
        super().__init__(self, path, created, modified)
        self.content = content
    def Open(self):
        print("Opened the Video...")

file = File("/some/path", 10501162020, 10501162020)
print(file)