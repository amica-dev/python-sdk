# CassaPrevidenziale

Tabella \"Cassa Previdenziale\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice** | **str** | Codice della voce. | [optional] 
**descrizione** | **str** | Descrizione della voce. | [optional] 

## Example

```python
from amica_python_sdk.models.cassa_previdenziale import CassaPrevidenziale

# TODO update the JSON string below
json = "{}"
# create an instance of CassaPrevidenziale from a JSON string
cassa_previdenziale_instance = CassaPrevidenziale.from_json(json)
# print the JSON string representation of the object
print(CassaPrevidenziale.to_json())

# convert the object into a dict
cassa_previdenziale_dict = cassa_previdenziale_instance.to_dict()
# create an instance of CassaPrevidenziale from a dict
cassa_previdenziale_from_dict = CassaPrevidenziale.from_dict(cassa_previdenziale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


