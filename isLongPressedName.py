# Compare Strings by Frequency of the Smallest Character

from typing import List


class Solution:
  
    def run(self):  
             
        name = "alex"
        typed = "aaleex"
        #print(f'{self.isLongPressedName(name, typed)} - expected True')

        name = "alex"
        typed = "aaleexe"
        print(f'{self.isLongPressedName(name, typed)} - expected False')

        name = "alexey"
        typed = "aaleexe"
        print(f'{self.isLongPressedName(name, typed)} - expected False')
        
        name = "saeed"
        typed = "ssaaedd"
        print(f'{self.isLongPressedName(name, typed)} - expected False')
        
        name = "leelee"
        typed = "lleeelee"
        print(f'{self.isLongPressedName(name, typed)} - expected True')

        name = "laiden"
        typed = "laiden"
        print(f'{self.isLongPressedName(name, typed)} - expected True')
        

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed:
            return False

        if name == typed:
            return True
        namelist = list(name)
        typedlist = list(typed)
        while namelist:
            sn = namelist.pop(0)
            if not typedlist:
                return False
            st = typedlist.pop(0)
            if sn != st:
                return False
            nt = 0          
            while len(typedlist) > 0 and typedlist[0] == sn:
                typedlist.pop(0)
                nt += 1
            ns = 0
            while len(namelist) > 0 and namelist[0] == sn:
                namelist.pop(0)
                ns += 1
            # if in typed less amount of current letter than in name
            if ns > nt:
                return False
        if typedlist:
            return False  

        return True

if __name__ == '__main__':
    Solution().run()

