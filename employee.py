class person:
    def __init__(self,id,Name):
        self.id = id
        self.Name = Name

    def printwhole(self):
        print(self.id,"|",self.Name)

class employee(person):
    def __init__(self, id, Name,salary,post):
        self.salary = salary
        self.post = post
        super().__init__(id, Name)

    def printwhole2(self):
        print(self.id,"|",self.Name,"|",self.salary,"|",self.post)

Daksh = employee("662012","Daksh Singh","60,000","Manager")
Daksh.printwhole2()       
        