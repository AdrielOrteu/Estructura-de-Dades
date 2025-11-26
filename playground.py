def func1(my_dict):
    for key in my_dict:
        for n in func1(my_dict[key]):
            yield n
    yield my_dict

dict1 = {
    5:{
        2:{
            1:{},
            3:{
                4:{}
            }
        },
        8:{
            7:{
                6:{}
            },
            10:{
                9:{}
            }
        }
    }
}

for element in func1(dict1):
    print(element)