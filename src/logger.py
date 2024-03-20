import logging

import os

from datetime import datetime

Log_file = f"{datetime.now().strftime('_%m_%d_%y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",Log_file)


os.makedirs(logs_path,exist_ok=True)


LOG_File_path = os.path.join(logs_path,Log_file)


logging.basicConfig(
    filename=LOG_File_path,
    format="[ %(asctime)s ]   %(lineno)d  %(name)s - %(levelname)s -%(message)s ",
    level = logging.INFO,


)

