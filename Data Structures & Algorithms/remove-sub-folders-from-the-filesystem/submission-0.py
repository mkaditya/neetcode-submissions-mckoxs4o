class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addFolder(self, path):
        segments = path.split("/")
        curr = self

        for segment in segments:
            if segment not in curr.children:
                curr.children[segment] = Trie()
            curr = curr.children[segment]
        curr.is_end = True
    
    def isSubFolder(self, path):
        segments = path.split("/")
        curr = self
        # We iterate through segments, skipping the first empty string from split
        for i in range(len(segments) - 1):
            segment = segments[i]
            curr = curr.children[segment]
            if curr.is_end:
                return True
        return False


class Solution:

    def removeSubfolders(self, folders: List[str]) -> List[str]:
        root = Trie()
        for folder_path in folders:
            root.addFolder(folder_path)
        
        return [path for path in folders if not root.isSubFolder(path)]