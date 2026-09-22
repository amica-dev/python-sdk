# DocumentoMediaFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**data** | **str** |  | [optional] 
**documento_id** | **int** |  | [optional] 

## Example

```python
from amica_python_sdk.models.documento_media_file import DocumentoMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoMediaFile from a JSON string
documento_media_file_instance = DocumentoMediaFile.from_json(json)
# print the JSON string representation of the object
print(DocumentoMediaFile.to_json())

# convert the object into a dict
documento_media_file_dict = documento_media_file_instance.to_dict()
# create an instance of DocumentoMediaFile from a dict
documento_media_file_from_dict = DocumentoMediaFile.from_dict(documento_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


