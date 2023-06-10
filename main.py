import json

p_data  = dict()
purchase_item = dict()


try:  
  with open('./data/products.txt') as file:
    data = file.read()
    to_dic = json.loads(data) # convert str to dict
    p_data = to_dic # assign converted dic to global product_data
except FileNotFoundError:
  print('File not found')
except IOError as e:
  print('IO Error', str(e))  
  
  
code = 3
keys = list(p_data.keys()) # get the list of keys
  
 
def list_gen(p_code ,dic_item): # this function is going to generate list for all the dic items(keys)
    
    for key, index in enumerate(keys): # iterate over each key in the dictionary
      if int(p_code) == int(key):  # check whether code is equals to a key
        purchase_item[index] = key # add product name and it's price
        return {key : index}
    return None  



counter = 0
limit = 3
while counter < 3:
    u_chose  = input("Enter product code to buy or 'q Q' to quite: ")
    if u_chose == 'q' or u_chose == 'Q':
        print('Program terminated')
        break;
    
    if not u_chose.isnumeric():
        print(f"Invalid product code '{u_chose}'. Product code are only numerics")
        
    else:
        if list_gen(u_chose , p_data):
        
        
            find_match = [key for key, value in p_data.items() if key in purchase_item.keys()]
            print('find_match', find_match)  
            print('Name \tPrice \tCode')
            for key, value in p_data.items():
                if key == find_match[0]:
                    print(key, p_data[key], code, sep='\t')
        else:
            print(f"No product found with code: {u_chose}")
    