import array

class Node:
    List_Index = []
    def __init__(self, data):
        self.data = data
        self.child = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.next = None

class Dictionary:
    def __init__(self):
        self.root = None
        # This MarkasEnd attribute will check our entered word is ended or not!
        self.MarkasEnd = None

    def Find_index(self, key, root):
        index = ord(key) % len(root.child)
        if index > 9:
            index = index % 10
        return index

    def insert(self, key):
        for i in key:
            if self.root is None:
                self.root = Node(None)
                index = self.Find_index(i, self.root)
                for n in range(len(self.root.child)):
                    if n == index:
                        Node.List_Index.append(index)
                        if self.root.child[index] == ' ':
                            self.root.child[index] = Node(key)
            else:
                temp = self.root
                temp2 = temp.child[Node.List_Index[0]]
                while temp2.next is not None:
                    temp2 = temp2.next
                if temp2.next is None:
                    index = self.Find_index(i, temp2)
                    for n in range(len(temp2.child)):
                        if n == index:
                            Node.List_Index.append(index)
                            if temp2.child[index] == ' ':
                                temp2.child[index] = Node(key)
                                New_Node = temp2.child[index]
                                temp2.next = New_Node


    def Search_Display(self):
        for x in Node.List_Index:
            if self.root is None:
                print("Dictionary has no word stored!")
            else:
                temp = self.root
                temp1 = temp.child[x]
                while temp1 is not None:
                    print(temp1.data, "--> ", end="")
                    temp1 = temp1.next
                if temp1 is None:
                    print("\nMark-as-End function will automatically display None when the word gets end!", self.MarkasEnd)
                    break


    # def Prediction(self, key):
    #     arr = [["ant, apple, alphabet"], ["balloon", "bat", "bad"], ["cat", "camel", "coy"], ["dare", "down", "drum"], ["egg", "emit", "extract"], []]
    #     for i in range(len(arr)):
    #         index = self.Find_index(key, self.root)
    #         if index == i:
    #             print(arr[index])



print("#############################################################################")
print("This input will work according to the given algorithm! \nFor example: First word will find its exact position \nthen a node will atomatically shifted on that position with its 26 childs!")
print("#############################################################################")

D = Dictionary()
print("!! Menu to select !!", "\nPress A to search a node from the Dictionary:", "\nPress B to print the assinged position of the word from the Dictionary:")


while True:
    try:

        Inp = input("Enter your choice:")
        if Inp == "A":
            Inp1 = input("Enter the word you want to search or add:")
            print("\nHere is the word you have entered:", Inp1)
            for i in Inp1:
                D.insert(i)
                print("\nSearching and also displaying the data according to the given algorithm:")
                D.Search_Display()
                continue
        if Inp == "B":
            print("\nThese are the indexes of your searched word: \nBy using Asscii technique:", Node.List_Index)
            continue

    except:
        continue




# D.Search_Display()



# D.Prediction("a")
# Storing the data according to the given algorithm!!
# print(T.root.child[Node.List_Index[a]].data)
# print(T.root.child[Node.List_Index[a]].child[Node.List_Index[a+1]].data)
# print(T.root.child[Node.List_Index[a]].child[Node.List_Index[a+1]].child[Node.List_Index[a+2]].data)
# print(T.root.child[Node.List_Index[a]].child[Node.List_Index[a+1]].child[Node.List_Index[a+2]].child[Node.List_Index[a+3]].data)
# print(T.root.child[Node.List_Index[a]].child[Node.List_Index[a+1]].child[Node.List_Index[a+2]].child[Node.List_Index[a+3]].child[Node.List_Index[a+4]].data)
# print(T.root.child[Node.List_Index[a]].child[Node.List_Index[a+1]].child[Node.List_Index[a+2]].child[Node.List_Index[a+3]].child[Node.List_Index[a+4]].child[Node.List_Index[a+5]].data)




