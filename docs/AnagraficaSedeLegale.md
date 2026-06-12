# AnagraficaSedeLegale

Indirizzo principale di un'anagrafica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indirizzo** | **str** | Indirizzo (via e numero civico). | 
**localit** | **str** | Località, solitamente il nome di una città, paese o frazione. | [optional] 
**cap** | **str** | CAP o codice di zona. | [optional] 
**provincia** | **str** | Provincia o area geografica. | [optional] 
**telefono1** | **str** | Numero di telefono principale. | [optional] 
**telefono2** | **str** | Numero di telefono secondario. | [optional] 
**fax** | **str** | Numero di fax. | [optional] 

## Example

```python
from amica_python_sdk.models.anagrafica_sede_legale import AnagraficaSedeLegale

# TODO update the JSON string below
json = "{}"
# create an instance of AnagraficaSedeLegale from a JSON string
anagrafica_sede_legale_instance = AnagraficaSedeLegale.from_json(json)
# print the JSON string representation of the object
print(AnagraficaSedeLegale.to_json())

# convert the object into a dict
anagrafica_sede_legale_dict = anagrafica_sede_legale_instance.to_dict()
# create an instance of AnagraficaSedeLegale from a dict
anagrafica_sede_legale_from_dict = AnagraficaSedeLegale.from_dict(anagrafica_sede_legale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


