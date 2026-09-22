# CausaleIva


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**codice** | **str** |  | 
**nome** | **str** |  | 
**aliquota** | **float** |  | [optional] 
**indeducibilit** | **float** |  | [optional] 
**intracomunitaria** | **bool** |  | [optional] 
**non_imponibile** | **bool** |  | [optional] 
**natura** | **str** |  | [optional] 
**split_payment** | **bool** |  | [optional] 
**fattura_elettronica** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.causale_iva import CausaleIva

# TODO update the JSON string below
json = "{}"
# create an instance of CausaleIva from a JSON string
causale_iva_instance = CausaleIva.from_json(json)
# print the JSON string representation of the object
print(CausaleIva.to_json())

# convert the object into a dict
causale_iva_dict = causale_iva_instance.to_dict()
# create an instance of CausaleIva from a dict
causale_iva_from_dict = CausaleIva.from_dict(causale_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


