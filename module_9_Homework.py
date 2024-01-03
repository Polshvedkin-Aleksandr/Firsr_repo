
def func_hello():
    res = "--How can I help you?--"
    return res
def input_error (func):
    def inner(words):
        try:
            return func(words)
        except IndexError: 
            print("-Enter user name and number-")
            return {}
        except KeyError:
            print("-Give me name-")
            return{}
    return inner
@ input_error
def func_phone(words):
    key=words[1] 
    phone={key: all[words[1]]}
    return phone
@ input_error
def func_add(words):
    add = {words[1] :words[2]}
    return add
@ input_error
def func_change(words):
    if words[1] in all.keys():
        change = {words[1]: words[2]}
        return change
    else: return {}

def main():
    while True:
        command = input("Input command: ")
        if command.strip()=='': continue
        command=command.lower()
        words=command.split()
        if words[0]=='hello':print(func_hello())
        elif words[0]=='add':
            if len(words) !=3: continue
            add_contact=func_add(words)
            all.update(add_contact)
            print ("-Сontact added-")
            continue 
        elif words[0]=='change':
            if len(words) != 3:
                continue
            change_contact = func_change(words)
            if change_contact!={}:
                all.update(change_contact)
                print("-Contact changed-")
            else: print ("-Name not found !-")
            continue
        elif words[0]=='phone':
            if len(words) != 2: continue
            contact_phone=func_phone(words)
            for key,value in contact_phone.items():
                print(f'{key} : {value}')
            continue
        elif words[0]=='show' and len(words)==2:
            if words[1]=='all':
                print("-Contacts-")
                for key,value in all.items(): print(f'{key} : {value}')
            continue
        elif (words[0]=='good' and len(words)==2):
            if words[1]=='bye': 
                print("---Good bye!---")
                break
        elif (words[0]=='close' or words[0]=='exit'):
            print("---Good bye!---")
            break
        
if __name__=='__main__':
    all = {}
    main()

