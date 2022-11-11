from typing import Union

from pydantic import BaseModel


class TokenData(BaseModel):
    user_id: Union[str, None] = None
    session_id: Union[str, None] = None
    