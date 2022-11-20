# Preprocessing pipeline 

The preprocessing pipeline is based on design pattern Pipes and Filters (see details [here](https://docs.microsoft.com/fr-fr/azure/architecture/patterns/pipes-and-filters)). Such a design decomposes a task that performs complex processing into a series of separate elements that can be reused. This can improve performance, scalability and reusability by allowing elements of tasks that perform processing to be deployed and scaled independently.

## What is a pipeline?
A pipeline is made of a [Source](source.md), [Filters](filters.md) and a [Sink](sink.md). The source is a simple algorithm that has no input port and one output port. Filters have both input and output ports and a sink has input but no output ports. 


*For simple pipeline implementation examples, see [test folder](/tests/unit/pipe/test_pipeline.py).*

The basic object is a [```Pipeline```](/filtering_pipeline/pipe/pipeline.py) python object. The ```Pipeline``` object has 4 attributes:
- ```_filters```: a list of ordered [```AbstractFilter```](/filtering_pipeline/filters/abstract_filter.py),
- ```_source```: a [```SourceFilter```](/filtering_pipeline/filters/abstract_filter.py) element,
- ```_sink```: an ```AbstractFilter``` element corresponding to the final filter applied to the pipeline,
- ```_pipeline_status```: a boolean indicating whether the pipeline is active or not. Set to False and switch to True once the source has been added.

**To do**: explain why the ```_pipeline_status``` becomes True when the source is added and not when everything has been set up.

## How to construct a pipeline?

To create a pipeline, one must:
1. Create the Pipeline object
```python
my_pipeline = Pipeline()
```

2. Create a source and add it to the pipeline
```python
my_source = ...
my_pipeline.add_source(my_source)
```

3. Add filters (Careful! the order is important)
```python
my_filter_1 = ...
my_pipeline.add_filters(my_filter_1)

my_filter_2 = ...
my_pipeline.add_filters(my_filter_2)
```
In this example, ```my_filter_1``` will be applied before ```my_filter_2```.

4. If exits, add a sink
```python
my_sink = ...
my_pipeline.add_sink(my_sink)
```