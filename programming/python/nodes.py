BINARYTREE = ['','','','',
                '','E','F','A','B','C','D',
                None,None,None,None,None,None,None,None,None,None,None,None]
                         
class Encoding:          
    def __init__(self, binaryTree):
        self._encoding = binaryTree


en = Encoding(BINARYTREE)
print(en._encoding)