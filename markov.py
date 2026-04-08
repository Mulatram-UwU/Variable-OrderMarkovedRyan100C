import random
class trie:
    def __init__(self):
        self.ptr=0
        self.next=[{}]
        self.weight=[0]
    def insert(self,s:str):
        cur=0
        for i in s:
            if i not in self.next[cur]:
                self.next[cur][i]=self.ptr+1
                self.next.append({})
                self.weight.append(0)
                self.ptr+=1
            cur=self.next[cur][i]
            self.weight[cur]+=1
    def find(self,s:str):
        cur=0
        for i in s:
            if i not in self.next[cur]:
                return 0
            cur=self.next[cur][i]
        return self.weight[cur]
    def get_node(self,s:str):
        cur=0
        for i in s:
            if i not in self.next[cur]:
                return -1
            cur=self.next[cur][i]
        return cur
class model:
    def __init__(self):
        self.trie=trie()
    def train(self,lines:list[str]):
        for line in lines:
            self.trie.insert(line)
    def run(self):
        s=""
        memory=""
        cur=0
        while True:
            if self.trie.next[cur]=={}:
                while not self.trie.find(memory):
                    memory=memory[1:]
                cur=self.trie.get_node(memory)
            next_char=random.choices(list(self.trie.next[cur].keys()),weights=list(self.trie.weight[self.trie.next[cur][i]] for i in self.trie.next[cur].keys()))[0]
            s+=next_char
            memory+=next_char
            print(next_char,end="")
            if next_char=='\n' or random.choices([0,1],weights=[0.9,0.1])[0]==1:
                break
        return s+'\n'
