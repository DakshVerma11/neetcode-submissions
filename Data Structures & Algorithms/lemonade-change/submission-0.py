class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        inventory={5:0,10:0}

        for bill in bills:
            if bill==5:
                inventory[5]+=1
            if bill==10:
                if inventory[5]>0:
                    inventory[5]-=1
                    inventory[10]+=1
                else:
                    return False
            if bill==20:
                if inventory[10]>0 and inventory[5]>0:
                    inventory[10]-=1
                    inventory[5]-=1
                elif inventory[5]>2:
                    inventory[5]-=3
                else:
                    return False
        return True
                    
                