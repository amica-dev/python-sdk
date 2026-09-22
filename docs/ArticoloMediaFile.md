# ArticoloMediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**data** | **str** |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**field_name** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.articolo_media_file import ArticoloMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of ArticoloMediaFile from a JSON string
articolo_media_file_instance = ArticoloMediaFile.from_json(json)
# print the JSON string representation of the object
print(ArticoloMediaFile.to_json())

# convert the object into a dict
articolo_media_file_dict = articolo_media_file_instance.to_dict()
# create an instance of ArticoloMediaFile from a dict
articolo_media_file_from_dict = ArticoloMediaFile.from_dict(articolo_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


