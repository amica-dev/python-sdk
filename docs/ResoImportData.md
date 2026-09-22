# ResoImportData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[int]** |  | [optional] 
**solo_righe** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.reso_import_data import ResoImportData

# TODO update the JSON string below
json = "{}"
# create an instance of ResoImportData from a JSON string
reso_import_data_instance = ResoImportData.from_json(json)
# print the JSON string representation of the object
print(ResoImportData.to_json())

# convert the object into a dict
reso_import_data_dict = reso_import_data_instance.to_dict()
# create an instance of ResoImportData from a dict
reso_import_data_from_dict = ResoImportData.from_dict(reso_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


