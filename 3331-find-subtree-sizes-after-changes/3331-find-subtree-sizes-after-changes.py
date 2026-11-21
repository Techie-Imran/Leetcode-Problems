class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for kid in range(1, n):
            boss = parent[kid]
            children[boss].append(kid)
        
        new_parent = list(parent)
        last_seen = {}

        def find_new_parent(u):
            char = s[u]
            if char in last_seen:
                new_parent[u] = last_seen[char]
            prev_boss = last_seen.get(char)
            last_seen[char] = u

            for v in children[u]:
                find_new_parent(v)
            
            if prev_boss is None:
                del last_seen[char]
            else:
                last_seen[char] = prev_boss

        find_new_parent(0)

        new_children = [[] for _ in range(n)]
        for kid in range(1, n):
            boss = new_parent[kid]
            new_children[boss].append(kid)
        
        answer = [0]*n

        def count_sizes(u):
            size = 1
            for v in new_children[u]:
                size += count_sizes(v)
            answer[u] = size
            return size

        count_sizes(0)

        return answer