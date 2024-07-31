"""
        filtering-pipeline: Example 1 - Olympic Game PARIS 2024
        The results of the Olympic Games are recorded daily.
        We want to generate a daily summary of the results for France and calculate the total number of medals obtained for France by category (Gold, Silver and Bronze).
        
"""
import unittest
import logging
import copy

from tests.asset.mock.mock_subpipeline_filter import MockSubPipelineFilter
from tests.examples.example1.source.example1_source import SourceFolder
from filtering_pipeline.utils.to_dict import yaml_to_dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Initialization: load conf filter
conf_filter = yaml_to_dict('tests/examples/example1/conf_example1.yml')
conf_filter['General']['sink'] = None

conf = {'conf_filter': conf_filter,
        'catalog_filter': {'SourceFolder': SourceFolder,
                           'MockFilter': MockFilter}}

subpipeline_filter = MockSubPipelineFilter(conf)