from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import httpx
import asyncio

app = FastAPI(title="Order service")

USER_SERVICE = "http://localhost:8001"
PRODUCT_SERVICE = "http://localhost:8002"


# Request Order
class OrderRequest(BaseModel):
    user_id: int
    product_id: int

# POST - create Order
@app.post("/orders",status_code=201)
async def create_order(order_request: OrderRequest):
    try:
        async with httpx.AsyncClient() as client:
            # Call User service
            user_response = await client.get(f'{USER_SERVICE}/users/{order_request.user_id}')
            if user_response.status_code == 404:
                raise HTTPException(status_code=404,detail="User Not Found")
            user_response.raise_for_status()
            user = user_response.json()
            # Call Product Service
            product_response = await client.get(f"{PRODUCT_SERVICE}/products/{order_request.product_id}")
            if product_response.status_code == 404:
                raise HTTPException(status_code=404,detail="Product Not Found")
            product_response.raise_for_status()
            product = product_response.json()
            
            # Create Order response
            return {"user": user['name'],
                    "product":product['name'],
                    'amount':product['price'],
                    'status':'Order created'}
    except HTTPException:
        raise
    except httpx.RequestError:
        raise HTTPException(status_code=503,detail="A dependent service is unavailable")
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=502,detail="A dependent service returned an error")
    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8003)
    
            
            
