from pydantic import BaseModel
from classes.site_info import site_info

class fit_request(BaseModel):

   data : list[dict[str| int | float ,str| int | float]]
   target : str