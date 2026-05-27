class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = "", ""
            idx, l = 0, len(email)
            while idx < l and email[idx] != "@":
                if email[idx] == "+":
                    while idx < l and email[idx] != "@":
                        idx += 1
                    continue
                if email[idx] == ".":
                    idx += 1
                    continue
                local += email[idx]
                idx += 1
            
            domain = email[idx+1:]
            unique.add((local, domain))
        return len(unique)