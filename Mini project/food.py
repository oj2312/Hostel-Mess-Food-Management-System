class Food:
    def __init__(self,name,ing_list,all_ing_dict):
        self.name=name
        self.ing_list=ing_list
        self.all_ing_dict=all_ing_dict

    def get_cost(self):
        self.cost=0
        for i in self.ing_list:
            self.cost = self.cost + self.all_ing_dict[i]
        return self.cost

    def get_ing(self):
        return self.ing_list
'''TESTING

all_ing={"panner":5,"salt":10}
p_ing=["panner","salt"]
ct=0
Ff=Food("PANNER",p_ing,all_ing)
ct=Ff.get_cost()
print(ct)
            
WORKING'''        
        
