dict={}
while(True):
    ch=input("ENter choice")
    match ch:
        case 'A':
            name=input("enter name")
            marks=input("ENter marks")
            dict.update({name,})
            break
        case "B":
            name=input("Enter name ot be updated")
            new_marks=input('Enter new marks')
            dict[name]=new_marks
            break
        case "C":
            name=input("enter name to search")
            if name not in dict:
                print("not available")
        case "D":
            for key, dict[key] in dict.items():
                print(key,dict[key])


