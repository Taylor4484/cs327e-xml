import xml.etree.ElementTree as ET
tree = ET.parse('RunXML.in')
itr = tree.iter()


i, j = 0, 0

#lst generating index numbers
"""
lst = []
for child in itr:
    lst.append(child.tag)
print(lst)
"""


ET.dump(tree)

"""
for child in itr:
    j = j+1
    print("\t",child.tag)
    
    
    for children in child:
        if children in child:
            i = i+1
            print("\t\t",children.tag)
            i=0

        else: break
        
        for kid in children:
            if kid in children:
                i = i+1
                print("\t\t\t",kid.tag)
                i=0
            else: break

            for grad in kid:
                if grad in kid:
                    i = i+1
                    print("\t\t\t\t",grad.tag)
                    i=0
                else: break

                for great in grad:
                    if great in grad:
                        i = i+1
                        print("\t\t\t\t\t",great.tag)
                        i=0
                    else: break
    

class node:
    def __int__(self):
        self.nodes = []
        self.root = None
        self.name = ""
    def create_node(self, node, parent=None)
        node = Node
"""
