from typing import Dict, Literal, Optional, Union 

from pydantic import BaseModel, conlist

Options = Literal[
    "fill_null_with_mean",
    "fill_null_with_mode",
    "fill_null_with_zeros",
    "fill_null_with_ones",
    "convert_numeric",
    "strip_strings",
    "lowercase_strings",
    "remove_special_chars",
    "standardize_dates",
    "remove_outliers",
    "normalize_columns",
    "encode_categories",
    "remove_constant_columns",
    "remove_empty_columns",
    "remove_long_texts"
]
class clean_request(BaseModel):
   
    data : list[dict[str,str| int | float]]
    processes : dict [Options,list[str]] 



    
   



