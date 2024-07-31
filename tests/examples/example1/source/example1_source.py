from typing import Dict
import logging
import os
from ..abstract_filter import SourceFilter


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class SourceFolder(SourceFilter):
    """
        A basic source that generates a list.
    """

    def __init__(self, conf: Dict = {}):
        super().__init__()
        self.folder_path = conf.get('folder_path')

    def generator(self) -> object:
        logger.debug('Start generator')

        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            logger.debug(f'File: {file}, file path: {file_path}')
            yield file_path
        logger.info('Stop generator')
