import requests

url = "https://api.freeapi.app/api/v1/public/randomproducts"
response=requests.get(url)
data=response.json()

if data["success"] and "data" in data:
    products = data['data']['data']  
    
    for product in products:
        product_id = product.get('id')
        title = product.get('title')
        brand = product.get('brand')
        price = product.get('price')
        
        print(f"ID: {product_id}, Title: {title}, Brand: {brand}, Price: {price}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")