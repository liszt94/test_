
import paramsIn 


size = len(paramsIn.palabra)


def ejercicio1():
    arr = []
    count = 0
    num_repetidas = 0
    index = 0
    for p in paramsIn.parrafo:
        #print("p::",p, "index",index)
        if (p == paramsIn.palabra[index]):
            #print("pp:: ",palabra[index],"::",p)
            count = count + 1
            index = index + 1
            #print("count",count)
            if(count == size):
                num_repetidas = num_repetidas + 1
                #print("count", count)
                index = 0
        else:
            count = 0
            index = 0
        
       
    print("num_repetidas::",num_repetidas)


def ejercicio2():
    n = len(paramsIn.entry)
    entry = paramsIn.entry
    salida = []
    for i in range(n-1):       
        for j in range(n-1-i): 
            if (entry[j]["weight"]  < entry[j+1]['weight']) or (entry[j]["length"] <  entry[j+1]['length'] ) or (entry[j]["priority"]  < entry[j+1]['priority']):
                entry[j]['weight'], entry[j+1]['weight'] = entry[j+1]['weight'], entry[j]['weight']
                entry[j]['length'], entry[j+1]['length'] = entry[j+1]['length'], entry[j]['length']
                entry[j]['height'], entry[j+1]['height'] = entry[j+1]['height'], entry[j]['height']
                entry[j]['width'], entry[j+1]['width'] = entry[j+1]['width'], entry[j]['width']
                entry[j]['id'], entry[j+1]['id'] = entry[j+1]['id'], entry[j]['id']
                entry[j]['cost'], entry[j+1]['cost'] = entry[j+1]['cost'], entry[j]['cost']
                entry[j]['priority'], entry[j+1]['priority'] = entry[j+1]['priority'], entry[j]['priority']
                
                #print("id \n ",entry[j]['id'], entry[j+1]['id'])   
                

    

    for i in entry:
        print("\n", i)
    
#ejercicio1()
#ejercicio2()



    