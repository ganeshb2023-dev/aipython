class PredicateLogicSystem:
 def __init__(self):
 self.facts={}
 self.rules=[]
 def add_fact(self,predicate,value):
 self.facts.setdefault(predicate,[])
 if value not in self.facts[predicate]:
 self.facts[predicate].append(value)
 def add_rule(self,premise,conculsion):
 self.rules.append((premise,conculsion))
 def infer(self):
 change=True
 while change:
 change=False
 for premise,conculsion in self.rules:
 if premise in self.facts:
 for val in self.facts[premise]:
 self.facts.setdefault(conculsion,[])
 if val not in self.facts[conculsion]:
 self.facts[conculsion].append(val)
 changed=True
 def query(self,predicate,value):
 return value in self.facts.get(predicate,value)
 def show_facts(self):
 print("\nCurrent facts:")
 for p,v in self.facts.items():
 print(f"{p} : {v}")
kb=PredicateLogicSystem()
while True:
 print("\n predicate Logic System")
 print("1.Add fact")
 print("2.Add rule(IF->THEN)")
 print("3.Show facts")
 print("4.Inference")
 print("5.query")
 choice =input("Enter your choices:")
 if choice=='1':
 pred=input("Enter predicate:")
 val=input("Enter value:")
 kb.add_fact(pred,val)
 print("Fact Added")
 elif choice=='2':
 premise=input("IF(predicate):")
 conculsion=input("THEN(value):")
 kb.add_rule(premise,conculsion)
 print("Rule added!",premise,"->",conculsion)
 elif choice=='3':
 kb.show_facts()
 elif choice=='4':
 kb.infer()
 print("Inference completed")
 elif choice=='5':
 pred=input("Enter predicate:")
 val=input("Enter value:")
 if kb.query(pred,val):
 print("TRUE")
 else:
 print("FALSE")
 else:
 print("Invalid choice!")
