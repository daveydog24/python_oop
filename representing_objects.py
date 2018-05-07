# instantiate class User
class User(object):
  # this method to run every time a new object is instantiated
  def __init__(self, name, email):
    # instance attributes from
    self.name = name
    self.email = email
    self.logged = True
  def __repr__(self):
    return "<User object {}, email {}>".format(self.name,self.email)

if __name__ == "__main__":
  user = User("Anna", "anna@anna.com")
  print user



Hacker Level OOP:
• Change all of your previous OOP assignments so that only the classes are available 
if the module is imported. Refer back to the optional modular store assignment if you need a refresher.

• Add a __repr__ method to each class. Format your string however you wish.

• Create a new document called manage.py and import all the previous OOP assignments.

• Create new instances of each of the imported classes. Print each instance.