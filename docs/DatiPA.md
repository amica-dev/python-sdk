# DatiPA

Dati per la pubblica amministrazione.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_commessa_convenzione_pa** | **str** | Identificativo del contratto o della convenzione assegnato dalla pubblica amministrazione. | [optional] 
**codice_cup** | **str** | Codice CUP assegnato dalla pubblica amministrazione. | [optional] 
**codice_cig** | **str** | Codice CIG assegnato dalla pubblica amministrazione. | [optional] 
**numero_ordine_pa** | **str** | Numero d&#39;ordine della pubblica amministrazione. | [optional] 
**data_ordine_pa** | **datetime** | Data dell&#39;ordine della pubblica amministrazione. | [optional] 

## Example

```python
from amica_python_sdk.models.dati_pa import DatiPA

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPA from a JSON string
dati_pa_instance = DatiPA.from_json(json)
# print the JSON string representation of the object
print(DatiPA.to_json())

# convert the object into a dict
dati_pa_dict = dati_pa_instance.to_dict()
# create an instance of DatiPA from a dict
dati_pa_from_dict = DatiPA.from_dict(dati_pa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


