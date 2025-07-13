from pydantic import BaseModel, Field


class prediction_request(BaseModel):

    data : list[dict[str| int | float ,str| int | float]]
    