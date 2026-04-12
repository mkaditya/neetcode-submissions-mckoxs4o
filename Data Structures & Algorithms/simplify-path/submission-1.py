class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split("/")
        result = []
        
        for segment in segments:
            if segment == "" or segment == ".":
                continue
            elif segment == "..":
                if result:
                    result.pop()
            else:
                result.append(segment)
        
        return "/" + "/".join(result)