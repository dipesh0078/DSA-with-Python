class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        self.children.append(child)
        child.parent=self
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print(self,n):
        spaces=' '*self.get_level()*6
        prefix=spaces+'|----' if self.parent else ''
        print(prefix + self.data)
        for child in self.children:
            if n<child.get_level():
                break
            else:
                child.print(n)

def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface pro"))
    laptop.add_child(TreeNode("Dell"))

    cellphone=TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Nothing"))

    tv=TreeNode("Tv")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("ASUS"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root=build_product_tree()
    root.print(1)
    root.print(2)