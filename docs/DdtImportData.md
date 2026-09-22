# DdtImportData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[int]** |  | [optional] 
**tipo_importazione** | **str** |  | [optional] 
**spese_incluse** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.ddt_import_data import DdtImportData

# TODO update the JSON string below
json = "{}"
# create an instance of DdtImportData from a JSON string
ddt_import_data_instance = DdtImportData.from_json(json)
# print the JSON string representation of the object
print(DdtImportData.to_json())

# convert the object into a dict
ddt_import_data_dict = ddt_import_data_instance.to_dict()
# create an instance of DdtImportData from a dict
ddt_import_data_from_dict = DdtImportData.from_dict(ddt_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


