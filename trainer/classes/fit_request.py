from pydantic import BaseModel


class fit_request(BaseModel):
   name : str
   data : list[dict[str| int | float ,str| int | float | bool]]
   target : str