# AnagraficaNominativo1

Persona di contatto principale all'interno di un'anagrafica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** | Nome del contatto. | [optional] 
**incarico** | **str** | Ruolo del contatto all&#39;interno dell&#39;anagrafica. | [optional] 
**telefono1** | **str** | Numero di telefono principale del contatto. | [optional] 
**telefono2** | **str** | Numero di telefono secondario del contatto. | [optional] 
**fax** | **str** | Numero di fax del contatto. | [optional] 
**e_mail** | **str** | Indirizzo email del contatto. | [optional] 
**note** | **str** | Note. | [optional] 

## Example

```python
from amica_python_sdk.models.anagrafica_nominativo1 import AnagraficaNominativo1

# TODO update the JSON string below
json = "{}"
# create an instance of AnagraficaNominativo1 from a JSON string
anagrafica_nominativo1_instance = AnagraficaNominativo1.from_json(json)
# print the JSON string representation of the object
print(AnagraficaNominativo1.to_json())

# convert the object into a dict
anagrafica_nominativo1_dict = anagrafica_nominativo1_instance.to_dict()
# create an instance of AnagraficaNominativo1 from a dict
anagrafica_nominativo1_from_dict = AnagraficaNominativo1.from_dict(anagrafica_nominativo1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


