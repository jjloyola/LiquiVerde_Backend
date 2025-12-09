import logging
from typing import Optional
from domains.optimization.optimizatin_product_with_store import OptimizationProductWithStore
from domains.optimization.optimization_product_list_with_store import OptimizationProductListWithStore
from domains.optimization.shopping_list_optimization_data import ShoppingListOptimizationData
from fastapi import APIRouter, HTTPException, Depends
from pydantic import ValidationError
from domains.shopping_list_service_interface import IShoppingListService
from dependencies.shopping_list_dependencies import get_shopping_list_service
from resources.dtos.input.add_item_request_dto import AddItemRequestDto
from resources.dtos.input.optimization.shopping_list_optimization_input_dto import ShoppingListOptimizationInputDto
from resources.dtos.input.update_item_request_dto import UpdateItemRequestDto
from resources.dtos.output.optimization.evaluated_shopping_list_dto import EvaluatedShoppingListDto
from resources.dtos.output.optimization.shopping_list_optimization_out_dto import ShoppingListOptimizationOutputDto
from resources.dtos.output.product_dto import ProductWithStoreDto

shopping_list_router = APIRouter(prefix="/api/lists", tags=["shopping_lists"])

# APIS NO FUNCIONALES, NO TESTEADAS O NO COMPLETADAS


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



@shopping_list_router.post("/optimize")
def optimize_shopping_list(input_request: ShoppingListOptimizationInputDto, shopping_list_service: IShoppingListService = Depends(get_shopping_list_service)):
    """Optimize a shopping list"""

    try:
       
        result: ShoppingListOptimizationOutputDto = None
        
        original_shopping_list: OptimizationProductListWithStore = OptimizationProductListWithStore(
            products_with_store=[OptimizationProductWithStore(product_id=item.product_id, 
                                                              store_id=item.store_id, 
                                                              quantity=item.quantity, 
                                                              price=item.price, 
                                                              sustainability_score=item.sustainability_score, 
                                                              ) for item in input_request.list_to_optimize],
            price_importance_percentage=input_request.price_importance_percentage,
            sustainability_importance_percentage=input_request.sustainability_importance_percentage,
            max_budget=input_request.max_budget
        )
        
        
        optimization_data: ShoppingListOptimizationData = ShoppingListOptimizationData(
            original_shopping_list=original_shopping_list,
            best_solution_shopping_list=None,
            price_importance_percentage=input_request.price_importance_percentage,
            sustainability_importance_percentage=input_request.sustainability_importance_percentage,
            max_budget=input_request.max_budget
        )
        
        
        optimization_result = shopping_list_service.optimize_shopping_list(optimization_data)
        return None
      
        '''  
        result = ShoppingListOptimizationOutputDto(
            original_shopping_list=original_shopping_list,
            optimized_shopping_list=optimization_result.best_solution_shopping_list,
            price_importance_percentage=input_request.price_importance_percentage,
            sustainability_importance_percentage=input_request.sustainability_importance_percentage,
            max_budget=input_request.max_budget
        )
        '''
        
    
    except ValidationError as e:
        error_details = []
        for error in e.errors():
            field = " -> ".join(str(loc) for loc in error["loc"])
            error_details.append(f"{field}: {error['msg']}")
        error_message = "Validation error: " + "; ".join(error_details)
        logging.error(error_message)
        raise HTTPException(status_code=422, detail=error_message)
    except Exception as e:
        logging.error("Error optimizing shopping list: " + str(e))
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))
    return result.model_dump(mode = "json")

    '''
    
    try:
        optimized_shopping_list = shopping_list_service.optimize_shopping_list(request)
        return optimized_shopping_list.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error. Error: " + str(e))
    '''