from pydantic import BaseModel, Field


class iaclean_request(BaseModel):
   
    data : list[dict[str ,str| int | float]]
    prompt: str
    