class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            print(f"Duplicate key '{key}' not allowed.")
            return node

        self.update_height(node)
        bf = self.balance_factor(node)

        if bf > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        if bf < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        if bf > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if bf < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        self.update_height(root)
        bf = self.balance_factor(root)

        if bf > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        if bf > 1 and self.balance_factor(root.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(root)
        if bf < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        if bf < -1 and self.balance_factor(root.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return root

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if node.key < key:
            return self.search(node.right, key)
        return self.search(node.left, key)

    def count_records(self, node):
        if not node:
            return 0
        return 1 + self.count_records(node.left) + self.count_records(node.right)

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)
        return result


if __name__ == "__main__":
    tree = AVLTree()
    root = None

    while True:
        print("\n==============================")
        print("       AVL TREE MANAGER       ")
        print("==============================")
        print("1. Insert a record")
        print("2. Delete a record")
        print("3. Search for a record")
        print("4. Traverse all records (Inorder)")
        print("5. Count total records")
        print("6. Exit")
       
        choice = input("\nEnter your choice (1-6): ").strip()
       
        if choice == '1':
            val = int(input("Enter key to insert: "))
            root = tree.insert(root, val)
            print(f"Record '{val}' processed.")
               
        elif choice == '2':
            val = int(input("Enter key to delete: "))
            if tree.search(root, val):
                root = tree.delete(root, val)
                print(f"Record '{val}' deleted successfully.")
            else:
                print(f"Record '{val}' not found in the tree.")
               
        elif choice == '3':
            val = int(input("Enter key to search: "))
            found = tree.search(root, val)
            if found:
                print(f"Record '{val}' found.")
            else:
                print(f"Record '{val}' not found.")
               
        elif choice == '4':
            records = tree.inorder(root)
            print(f"Inorder Traversal: {records}")
           
        elif choice == '5':
            total = tree.count_records(root)
            print(f"Total records in tree: {total}")
           
        elif choice == '6':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 6.")
