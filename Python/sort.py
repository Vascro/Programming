list = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
list = [i.split('.',1)[0] for i in list]
list.sort()
print(list)