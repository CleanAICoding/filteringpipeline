# Class SubPipelineFilter

Implementation example can be found [here](/tests/unit/filters/test_pipelineFilter.py).


**To do**: unit test seems to be missing.

## Description

[Class SubPipelineFilter](/filtering_pipeline/filters/catalog_filter/subpipeline_filter.py) is a class that executes a (sub)-pipeline each time its ```process``` method is called. This can be used for fine-grained preprocessing.

**To do**: explain somewhere that a filter is not only used for filtering data but also to compute stuff. 

## Class arguments details

```SubPipelineFilter``` is a class that herits from [```AbstractFilter```](/filtering_pipeline/filters/abstract_filter.py). It has a single argument: a Dict ```conf``` that must contains the following keys:
- *conf_filter*: a configuration filter dict with keys `type` and `parms`.
- *catalog_filter*: a catalog Dict (such as for instance [CATALOG_FILTERS](/filtering_pipeline/filters/__init__.py))

**To do**: 
1. check that the second mandatory key for *conf_filter* is `parms` instead of `params`.
2. class seems to expect a third key, `GENERAL_CONF_PIPELINE`, but does not seem to do anything with the data it gets from it. Check that behavior.
3. the CATALOG_FILTERS example seems to be missing.