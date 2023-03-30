from pydantic import BaseModel

class TokenSchema(BaseModel):
    acces_token : str
    refresh_token : str
