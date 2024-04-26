class TreeNode():
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print(self,condition):
        spaces=' '*self.get_level()*3
        prefix=spaces +'|---' if self.parent else ''
        if condition=='name':
            print(prefix+self.name)
            for child in self.children:
                child.print('name')
        if condition=='designation':
            print(prefix+self.designation)
            for child in self.children:
                child.print('designation')
        if condition=='both':
            print(prefix+self.name + '('+self.designation+')')
            for child in self.children:
                child.print('both')
        
def build_product_tree():
    root=TreeNode("Dipesh",'CEO')

    CTO=TreeNode("Abiral",'CTO')
    CTO.add_child(TreeNode("Ayush","Backend Head"))
    CTO.add_child(TreeNode("Ram","Frontend  Head"))
    CTO.add_child(TreeNode("Kabin","Manager Head"))

    HR=TreeNode("Isha","HR")
    HR.add_child(TreeNode("Apurba","Recruiter Head"))
    HR.add_child(TreeNode("Apeksha","Interviewer Head"))
    HR.add_child(TreeNode("Biraj","Policy Head"))

    

    root.add_child(CTO)
    root.add_child(HR)
   

    return root


if __name__=="__main__":
    root_node=build_product_tree()
    root_node.print("name") 
    root_node.print("designation") 
    root_node.print("both")
  
        

