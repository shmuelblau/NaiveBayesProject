
from typing import Optional
from pydantic import BaseModel, Field
from classes.site_info import site_info

class fit_request(BaseModel):
    data_type: str
    json_data: Optional[list[dict[str ,str]]] = None
    csv_path: Optional[str] = None
    csv_data:Optional[str] = None
    