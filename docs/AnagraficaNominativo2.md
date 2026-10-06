# AnagraficaNominativo2

Persona di contatto secondaria all'interno di un'anagrafica.

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
from amica_python_sdk.models.anagrafica_nominativo2 import AnagraficaNominativo2

# TODO update the JSON string below
json = "{}"
# create an instance of AnagraficaNominativo2 from a JSON string
anagrafica_nominativo2_instance = AnagraficaNominativo2.from_json(json)
# print the JSON string representation of the object
print(AnagraficaNominativo2.to_json())

# convert the object into a dict
anagrafica_nominativo2_dict = anagrafica_nominativo2_instance.to_dict()
# create an instance of AnagraficaNominativo2 from a dict
anagrafica_nominativo2_from_dict = AnagraficaNominativo2.from_dict(anagrafica_nominativo2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


