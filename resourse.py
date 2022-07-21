from datetime import datetime

import pandas
from pydantic import BaseModel, validator
from typing import Optional, List


class Resource:
    def __init__(self, df: pandas.DataFrame = ""):
        self.task_id = df.task_id
        self.TASK__status_code = df.TASK__status_code  # str
        self.rsrc_id = df.rsrc_id  # int
        self.name_rsrc = df.name_rsrc  # str
        self.task__task_name = df.task__task_name  # str
        self.start_date = df.start_date  # Optional[datetime]
        self.end_date = df.end_date  # Optional[datetime]
        self.target_qty = df.target_qty  # float
        self.total_qty = df.total_qty  # float
        self.act_qty = df.act_qty  # float
        self.remain_qty = df.remain_qty  # float

    def to_db_update_model(self):
        source_dict = super().dict(
            by_alias=True, exclude={"project_code", "last_publication", "business_unit"}
        )

        return source_dict

    def to_db_insert_model(self):
        source_dict = super().dict(by_alias=True, exclude={"last_publication"})

        return source_dict
