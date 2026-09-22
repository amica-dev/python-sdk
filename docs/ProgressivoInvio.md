# ProgressivoInvio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**documento_id** | **int** |  | [optional] 
**progressivo** | **str** |  | 

## Example

```python
from amica_python_sdk.models.progressivo_invio import ProgressivoInvio

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressivoInvio from a JSON string
progressivo_invio_instance = ProgressivoInvio.from_json(json)
# print the JSON string representation of the object
print(ProgressivoInvio.to_json())

# convert the object into a dict
progressivo_invio_dict = progressivo_invio_instance.to_dict()
# create an instance of ProgressivoInvio from a dict
progressivo_invio_from_dict = ProgressivoInvio.from_dict(progressivo_invio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


