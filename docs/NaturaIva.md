# NaturaIva

Tabella \"Natura Iva\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice** | **str** | Codice della voce. | [optional] 
**descrizione** | **str** | Descrizione della voce. | [optional] 

## Example

```python
from amica_sdk.models.natura_iva import NaturaIva

# TODO update the JSON string below
json = "{}"
# create an instance of NaturaIva from a JSON string
natura_iva_instance = NaturaIva.from_json(json)
# print the JSON string representation of the object
print(NaturaIva.to_json())

# convert the object into a dict
natura_iva_dict = natura_iva_instance.to_dict()
# create an instance of NaturaIva from a dict
natura_iva_from_dict = NaturaIva.from_dict(natura_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


