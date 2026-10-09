from fastapi_offline import FastAPIOffline


app = FastAPIOffline()

mylist = [100, 200, 300,200]

@app.get('/')
def say_hello():
    return {'HELLO' : 'WORLD'}
#################################

@app.get('/getItem/')
def get_item():
    return {'output' : mylist}
#################################

@app.get('/lastone/')
def get_last_item():
    if len(mylist)>0:
        return {'output1' : mylist[-1] }
    else:
        return {'list is empty'}
##################################

@app.post('/additem/{new_item}')
def insert_item(new_item:int):
    mylist.append(new_item)
    return {'output2' :  mylist}
##################################

@app.delete('/removeitem/')
def remove_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {'list after remove': mylist}
    else:
        return{f'{item}not found in list'}
######################################

@app.delete('/popindex/')
def pop_item(index:int):
    if index >= 0 and index < len(mylist):
        r = mylist.pop(index)
        return {f'{r} deletnfrom list'}
    else:
        return{'index not found'}
    #####################################3

@app.put('/updateItem/')
def update_item(index:int, new_item:int):
    if index >= 0 and index < len(mylist):
        mylist[index]= new_item
        return {'update_list': mylist}
    else:
        return {f'index of {index}, not found'}
#################################################
@app.put('/updateItemm/')
def updateitem(old_item:int, new_item:int):
    if old_item in mylist:
        i = mylist.index(old_item)
        mylist[i]= new_item

        return {'update_list': mylist}
    else:
        return {f'index of {old_item}, not found'}






















