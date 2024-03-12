def transformJSON(lists_tup):
    list_list = []
    for result in lists_tup:
        list_dict = {
            'id': result[0],
            'preco': result[1],
            'tamanho': result[2],
            'peca': result[3],
            'descricao': result[4]                  
        }    
        list_list.append(list_dict)
        
    return list_list