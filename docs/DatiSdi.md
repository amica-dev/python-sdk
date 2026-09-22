# DatiSdi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo_sdi** | **str** |  | [optional] 
**stato_sdi** | **str** |  | [optional] 
**descrizione_stato_sdi** | **str** |  | [optional] 
**data_consegna_sdi** | **datetime** |  | [optional] 

## Example

```python
from amica_python_sdk.models.dati_sdi import DatiSdi

# TODO update the JSON string below
json = "{}"
# create an instance of DatiSdi from a JSON string
dati_sdi_instance = DatiSdi.from_json(json)
# print the JSON string representation of the object
print(DatiSdi.to_json())

# convert the object into a dict
dati_sdi_dict = dati_sdi_instance.to_dict()
# create an instance of DatiSdi from a dict
dati_sdi_from_dict = DatiSdi.from_dict(dati_sdi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


