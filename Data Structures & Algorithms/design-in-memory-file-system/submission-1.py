class File:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = File()

    def get_file(self, path):
        curr_file = self.root

        if path == "/":
            return curr_file
        
        for name in path.split("/")[1:]:
            if name not in curr_file.children:
                return None
            curr_file = curr_file.children[name]
        return curr_file

    def ls(self, path: str) -> List[str]:
        file = self.get_file(path)
        if file.is_file:
            return [path.split("/")[-1]]
        return sorted(file.children.keys())

    def mkdir(self, path: str) -> None:
        curr_file = self.root
        for name in path.split("/")[1:]:
            if name not in curr_file.children:
                curr_file.children[name] = File()
            curr_file = curr_file.children[name]        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        file = self.get_file(filePath)
        file.is_file = True
        file.content += content

    def readContentFromFile(self, filePath: str) -> str:
        file = self.get_file(filePath)
        if file is not None and file.is_file:
            return file.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
