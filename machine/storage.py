# The storage will contain all the products available
# when the app start the storage will load all the product from the products.txt
import json 

product_data = dict()
track_user_choice = [] # store what the user is buying

#* file handling
try: 
  with open('./data/products.txt') as file:
    data = file.read()
    to_dic = json.loads(data) # convert str to dict
    product_data = to_dic # assign converted dic to global product_data
except FileNotFoundError:
  print('File not found')
except IOError as e:
  print('IO Error', str(e))  
  
  
def displayProduct():
  print('*************** Welcome To VENDING MACHINE ***************')
  print('Name\tPrice(GMD)\tCode')
  
  for keys in product_data:
    print(keys, product_data[keys], sep="\t\t")
 
 
  
def lookup_codes(product_code):
  list_of_codes = [] # this will hold dynamic index of product_data as 
  keys = list(product_data.keys()) # get the list of keys
  
  for index, key in enumerate(keys):    
    list_of_codes.append(index) # fill list_of_codes with index of product ranging from 0 to len - 1 of product_Data.
    print('key@: ', key)
         
  if product_code in list_of_codes: # check whether user chose in actual a code in the product list        
    return True
  else:    
    return False
  
  
def lookup_product(product_code):  
  keys = list(product_data.keys()) # get the list of keys
  # lookup for product
  for key, val in product_data.items():  
    print(f" {val}, {product_code}")  
    if int(val) == int(product_code):
      print('val', val)
      return {key: val}
    
  return None
      
  

counter = 0 # user can buy only three product
limit = 3 # show users a count of the product they can buy
userChose = ''
while counter < 3:
  print(f"You have {limit} more products to buy")
  displayProduct()
  userChose = input("Enter product code to buy or 'q - Q' to quite: ")
  if userChose == 'q' or userChose == 'Q': # check for 'q' or 'Q'
    print('program terminated')
    break # kill the App
  

  # check for non number input apart from q or Q
  if not userChose.isnumeric():  
    # invalid input     
    print(f"Invalid product code '{userChose}'. Product code are only numerics")
  
  else:
    # look_up_codes == True
    if lookup_codes(int(userChose)): # change userChose to integer while passing it
      # get the product by it's code
      print(f"You are buying {lookup_product(userChose)}")
      
      # update only when a product is found
      counter += 1
      limit -= 1
    else: # look_up_codes == False
      print(f"No product is found with code: '{userChose}'. Try with a correct code")
    

    
    