# classes and objects in python
# you can think of a class as a basic blueprints in which you can create multipule  instences /objects from.

# it's another data structure kinda similar to arrays or linked lists, but you can create real world object via code. 

# to create a class /  
import email


class ex_girlfriends:
    def __init__(self, her_name, years_dated, Why_broke_up) -> None:
        self.her_name       = her_name
        self.years_dated = years_dated
        self.Why_broke_up   = Why_broke_up
# def is how you create a function in python
# __init__ helps localize each object / instence meaning.. the "self" keyword is used by each instence and refers to itself, (yes kinda confusing)
# but the self keyword help seperate multipul instences / objects from one another 
 
       

# this is how you create instences / objects that can use the class bule print.  
girl1 = ex_girlfriends("Stacey", "12", "He was too much man for me to hanlde")
girl2 = ex_girlfriends("Kelly", 33, "he was too perfect" )
girl3 = ex_girlfriends("Monica", 2, "I found someone better")

print(f"Hello my name is " + girl1.her_name + " And I dated Michael for " + girl1.years_dated + " years, but " + girl1.Why_broke_up )
print(girl3.her_name, girl3.Why_broke_up, "Im his second girlfriend " + girl2.her_name)

# or a smarter way to write code for storing each instence, using lists(array)
ex_girls = [
    ex_girlfriends("miley", 44, ""),
    ex_girlfriends("amanda", 30, "flew away"),
    ex_girlfriends("kesha", 50, " I swear we dated, im not lying go ask...")
]
# to call an instence with list 
print(ex_girls[0].her_name)
print(ex_girls[2].her_name  + ex_girls[2].Why_broke_up  )

#__________________________________________________________________________________________________________________________________________________#

# object methods are basically using a function within a (object and instance are the same thing).

class customers:
    def __init__(self, name, Email, phone_num) -> None:
        self.name      =  name
        self.Email     = Email
        self.phone_num = phone_num

    def membership_type(self, bronze, silver, gold):
        print("money was recieved to upgrade")
        print(" API invoked / database updated")
        self.bronze = bronze
        self.silver = silver
        self.gold   = gold    

    def print_all_customers(customers):   # notice that this function dose not have self, becuse in this case we are not refering to 
        for customers in customers:       # individual object/ instences but all of them, thus 
            print(customers)

customers = [
    customers("Penny Proud", "my.first.penny@aol.com", 555-555-55555),
    customers("Elton John", "nana@gmail.com", 123234234234) ]

customers.print_all_customers(customers)

# Encapsulation , Inheritance, Polymorphism  are the foundation of Object oriented programming