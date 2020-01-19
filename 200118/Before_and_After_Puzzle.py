from collections import defaultdict
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        if not phrases:
            return []
        
        d = defaultdict(list)
        
        for idx, phrase in enumerate(phrases):
            phrase = phrase.split(' ')
            head, rest = phrase[0], phrase[1:]
            d[head].append([idx] + rest)
            
        ans = []
        for idx, phrase in enumerate(phrases):
            phrase = phrase.split(' ')
            tail, rest = phrase[-1], phrase[:-1]
            
            if tail in d:
                other_phrases = d[tail]
                
                for other_phrase in other_phrases:
                    if other_phrase[0] == idx:
                        continue
                    conbined = ' '.join(phrase + other_phrase[1:])
                    if conbined in ans:
                        continue
                    ans.append(conbined)
                
        return sorted(ans)
        