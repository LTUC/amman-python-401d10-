from linked_list import LinkedList

class HashTable():
    def __init__(self,size=3):
        self.size = size
        self.map = [None]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
    
    def set(self, key, value):
        hashed_key = self.custom_hash(key)

        if not self.map[hashed_key]: # if the Bucket is empty
            self.map[hashed_key] = [key,value]

        else: # collision happeded
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
                
            else: # if the bucket contains one pair only
                chain = LinkedList()
                exsiting_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)








        