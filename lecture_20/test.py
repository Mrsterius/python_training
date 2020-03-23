import BST_try

li = [27, 24, 12, 7, 4, 4, 27, 27, 2, 29, 30, 12, 25, 16, 24, 2, 19, 26, 22, 3]

tree = BST_try.BST()
for item in li:
    tree.add(item)
tree.display()
print(tree.balanced())