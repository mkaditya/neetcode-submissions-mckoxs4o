class TrieNode(object):
    def __init__(self, name=""):
        self.map = {}
        self.name = name
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")
        curr = self.root

        for idx in range(1, len(components)):
            name = components[idx]
            if name not in curr.map:
                if idx == len(components) - 1:
                    curr.map[name] = TrieNode(name)
                else:
                    return False     
            curr = curr.map[name]
        if curr.value != -1:
            return False
        
        curr.value = value
        return True

    def get(self, path: str) -> int:
        curr = self.root
        components = path.split("/")
        for idx in range(1, len(components)):
            name = components[idx]
            if name not in curr.map:
                return -1
            curr = curr.map[name]
        return curr.value