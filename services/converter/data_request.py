from typing import Literal, Optional, Union
from fastapi import UploadFile
from pydantic import BaseModel, Field


class data_request(BaseModel):
    data_type: Literal["csv_path", "json", "csv","db_path"]
    data : Union[list[dict[str| int | float ,str| int | float | bool]] ,UploadFile ,str]
    