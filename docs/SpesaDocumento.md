# SpesaDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**documento_id** | **int** |  | [optional] 
**spesa_id** | **int** |  | [optional] 
**spesa** | [**Spesa**](Spesa.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**importo** | **float** |  | [optional] 
**pagamento** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.spesa_documento import SpesaDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of SpesaDocumento from a JSON string
spesa_documento_instance = SpesaDocumento.from_json(json)
# print the JSON string representation of the object
print(SpesaDocumento.to_json())

# convert the object into a dict
spesa_documento_dict = spesa_documento_instance.to_dict()
# create an instance of SpesaDocumento from a dict
spesa_documento_from_dict = SpesaDocumento.from_dict(spesa_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


