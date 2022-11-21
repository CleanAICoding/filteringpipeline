# Source 

The source is a simple algorithm that has no input port and one output port. For instance, it can generate output based on a file.

*For simple pipeline implementation example, see [test_source](/tests/unit/filters/test_source.py).*

## Source object

Source object inherits from class [SourceFilter](/filtering_pipeline/filters/abstract_filter.py).

## SourceFilter 

Object ```SourceFilter``` is an ```AbstractFilter``` object whose abstract method ```process()``` has been implemented.

**To do**: check previous sentence: it reads like a definition but seems wrong.

## How to construct a Source object?

*Example: see [SourceList](/filtering_pipeline/filters/catalog_source/source_list.py)*

