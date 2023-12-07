lst = ["1", "2", "3", "4", "5", "6"]

new_lst = [lst.pop() for i in range(len(lst))]
print(new_lst)