from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from domains.list_item import ListItem
from domains.shopping_list_service_interface import IShoppingListService
from dependencies.shopping_list_dependencies import get_shopping_list_service
from resources.dtos.input.add_item_request_dto import AddItemRequestDto
from resources.dtos.input.update_item_request_dto import UpdateItemRequestDto

shopping_list_router = APIRouter(prefix="/api/lists", tags=["shopping_lists"])

@shopping_list_router.post("/{list_id}/items")
def add_item_to_list(list_id: Optional[int], request: AddItemRequestDto, shopping_list_service: IShoppingListService = Depends(get_shopping_list_service)):
    """Add a product to a shopping list"""
    try:
        list_item = shopping_list_service.add_item_to_list(
            list_id=list_id,
            product_id=request.product_id,
            quantity=request.quantity,
            priority=request.priority,
            notes=request.notes
        )
        return list_item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))


#retornar list + items dentro de la lista
@shopping_list_router.get("/{list_id}")
def get_list_by_id(list_id: int, shopping_list_service: IShoppingListService = Depends(get_shopping_list_service)):
    """Get a shopping list by ID"""
    try:
        shopping_list = shopping_list_service.get_list_by_id(list_id)
        if not shopping_list:
            raise HTTPException(status_code=404, detail="Shopping list not found")
        return shopping_list.model_dump()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))


@shopping_list_router.delete("/{list_id}/items/{item_id}")
def delete_list_item(list_id: int, item_id: int, shopping_list_service: IShoppingListService = Depends(get_shopping_list_service)):
    """Delete an item from a shopping list"""
    try:
        success = shopping_list_service.delete_list_item(list_id, item_id)
        if not success:
            raise HTTPException(status_code=404, detail="List item not found")
        return {"message": "Item deleted successfully"}
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))
