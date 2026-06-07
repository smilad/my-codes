

# user = {
#     "name": "milad",
#     "last_name": "soleymani"
# }

# print(user)

# print ("------------------")

# user2 = {
#     "name" : "kianosh",
#     "last_name": "safari"
# }


# print(user2)

# print("----------")


# my_users = list([user,user2])


# print(my_users)


# for i in my_users:
#     print(i)


#complex type dic -> list 

# input -> exit 
# name lname isClosed
# freinds_list -> close -> non close freind


f_list = []

def create_user(**kvargs):
    print(kvargs)
    return kvargs

def get_user_list():
    return f_list

def define_user():
    name = input("whats is you name")
    lname = input("what is your last name")
    isClose= input('is your close freind y/n')
    f = create_user(name=name,last_name=lname,isCloses= isClose=='y')
    f_list.append(f)

while True:
    define_user()
    want_continue = input('do you want other freind y/n')
    if want_continue == 'n':
        break



def find_by_name(name):
    for u in f_list:
        if u['name'] == name:
            return u
    
    return None


def delete_user_by_name(name):
    removed = None
    for idx,u in enumerate(f_list):
        if u['name'] == name:
            removed = f_list.pop(idx)
    
    print(removed)



print(find_by_name("milad"))
delete_user_by_name("milad")


# CRD
print(f_list)
# def delete_user_by_name(name):
#     for  u in f_list:
#         if u['name'] == name:
#             f_list.remove(u)