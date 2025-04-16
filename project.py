from Validator import validation
from typing import Dict
from datetime import datetime
from toolkit import utils
import pandas as pd

class testA():
    @validation()
    def compute(self, input: Dict[str, pd.DataFrame], time: datetime) -> Dict[str, pd.DataFrame]:
        print(input)
        res = {
            'test1': pd.DataFrame(
                {
                    'time': [time],
                    'symbol': ['test'],
                    'value': [1]
                }
            )
        }

        return res
    
    @validation()
    def compute_history(self, input: Dict[str, pd.DataFrame], start_time:datetime, end_time:datetime) -> Dict[str, pd.DataFrame]:
        res = {
            'test1': pd.DataFrame(
                {
                    'time': [start_time],
                    'symbol': 'test',
                    'value': 1,
                }
            )
        }
        
        return res