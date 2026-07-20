# DistinctPropertyGroup

Query distinct con raggruppamento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Chiave di distinzione (es.: \&quot;RagioneSociale1\&quot;). | [optional] 
**items** | [**List[DistinctPropertyGroup]**](DistinctPropertyGroup.md) | Valori distinti trovati per la chiave indicata. | [optional] 

## Example

```python
from amica_python_sdk.models.distinct_property_group import DistinctPropertyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DistinctPropertyGroup from a JSON string
distinct_property_group_instance = DistinctPropertyGroup.from_json(json)
# print the JSON string representation of the object
print(DistinctPropertyGroup.to_json())

# convert the object into a dict
distinct_property_group_dict = distinct_property_group_instance.to_dict()
# create an instance of DistinctPropertyGroup from a dict
distinct_property_group_from_dict = DistinctPropertyGroup.from_dict(distinct_property_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


