from pydantic import BaseModel

class CheckoutRequest(BaseModel):
    items: str

class TestResult(BaseModel):
    test_name: str
    result: str
    details: str = ""