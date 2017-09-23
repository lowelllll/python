class Map():
    def __init__(self):
        self.map = [[] for _ in range(16)]
    def push(self,key,value):
        index = abs(hash(key))%16
        check = True
        if len(self.map[index]) > 0:
            for i, entry in enumerate(self.map[index]):
                if entry[0] == key :
                    self.map[index][i] = [key,value]
                    check = False
                    break

            if check:
                self.map[index].append([key, value])
        else:
            self.map[index].append([key,value])

    def get(self,key):
        index = abs(hash(key))%16
        for i,entry in enumerate(self.map[index]):
            if entry[0] == key :
                return self.map[index][i][1]
            return 0



map = Map()
map.push("yejin","love")
map.push("yejin","dom")
map.push("love","l love you")
map.push("eejin","zzzzz")
map.push("eejin","1")
map.push("eejin","2")
map.push("rlawhdgus","love")
map.push("hello","yejin")
map.push("wkwmdskspdy","anjrkdy")
map.push("whdgusk","aldksgo")
map.push("dkdrlahWldzzzzz","zzzz")
print map.map
print map.get("love")
