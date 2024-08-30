from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from .checkout import create_checkout
import importlib
import logging
import asyncio
from app.models import *

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def run_single_test(test_func):
    try:
        if 'checkout' in test_func.__code__.co_varnames:
            test_func(create_checkout())
        else:
            test_func()
        return TestResult(test_name=test_func.__name__, result="Passed")
    except Exception as e:
        logger.error(f"Test {test_func.__name__} failed: {str(e)}")
        return TestResult(test_name=test_func.__name__, result="Failed", details=str(e))

async def run_all_tests():
    logger.info("Starting test run")
    test_results = []
    
    try:
        # Dynamically importing test functions
        test_module = importlib.import_module('.test_checkout', package='app')
        test_functions = [getattr(test_module, name) for name in dir(test_module) 
                          if name.startswith('test_') and callable(getattr(test_module, name))]

        print(test_functions)
        tasks = [run_single_test(test_func) for test_func in test_functions]
        test_results = await asyncio.gather(*tasks)

    except Exception as e:
        logger.error(f"Error running tests: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error running tests: {str(e)}")

    logger.info("Test run completed")
    return test_results


@app.post("/checkout", response_model=int)
async def checkout(request: CheckoutRequest):
    checkout = create_checkout()
    try:
        for item in request.items:
            if not item in ["A","B","C","D"]:
                raise HTTPException(status_code=400, detail="Wrong Checkout item Please Provide the correct item e.g [A,B,C,D]")
            checkout.scan(item)
        print(checkout.items)
        return checkout.calculate_total()
    except Exception as e:
        logger.error(f"Error during checkout: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error during checkout: {str(e)}")



@app.get("/run_tests", response_model=List[TestResult])
async def api_run_tests():
    return await run_all_tests()


@app.get("/pricing_rules", response_model=Dict[str, Dict[str, int]])
async def get_pricing_rules():
    checkout = create_checkout()
    rules = {}
    for item, (price, offers) in checkout.pricing_rules.items():
        rules[item] = {"unit_price": price}
        print(rules[item])
        for i, offer in enumerate(offers, start=1):
            rules[item][f"offer_{i}_quantity"] = offer.quantity
            rules[item][f"offer_{i}_price"] = offer.price
    print(rules)
    return rules

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)