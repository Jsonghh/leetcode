from collections import defaultdict

class unionFind:
    def __init__(self, n):
        self.father = {i : i for i in range(n)}
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.father[rb] = ra
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.uf = unionFind(len(accounts))
        email_accid = self.get_email_accid(accounts)
        for email, accids in email_accid.items():
            uid = accids[0]
            for accid in accids[1:]:
                self.uf.union(uid, accid)
        uid_email = self.get_uid_email(accounts)
        ans = []
        for uid, emails in uid_email.items():
            ans.append([accounts[uid][0]] + sorted(emails))
        return ans
    
    def get_email_accid(self, accounts):
        email_accid = defaultdict(list)
        for idx, accs in enumerate(accounts):
            for email in accs[1:]:
                email_accid[email].append(idx)
        return email_accid
    
    def get_uid_email(self, accounts):
        uid_email = defaultdict(set)
        for idx, accs in enumerate(accounts):
            uid = self.uf.find(idx)
            for email in accs[1:]:
                uid_email[uid].add(email)
        return uid_email
        