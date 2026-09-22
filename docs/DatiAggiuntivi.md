# DatiAggiuntivi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**identificativo_esteso** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 
**colore** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.dati_aggiuntivi import DatiAggiuntivi

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAggiuntivi from a JSON string
dati_aggiuntivi_instance = DatiAggiuntivi.from_json(json)
# print the JSON string representation of the object
print(DatiAggiuntivi.to_json())

# convert the object into a dict
dati_aggiuntivi_dict = dati_aggiuntivi_instance.to_dict()
# create an instance of DatiAggiuntivi from a dict
dati_aggiuntivi_from_dict = DatiAggiuntivi.from_dict(dati_aggiuntivi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


