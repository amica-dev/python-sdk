# AreaGeografica

Area geografica (zona).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome dell&#39;area. Può essere una regione, una provincia, un comune o qualsiasi altro riferimento rilevante per il caso d&#39;uso. | 

## Example

```python
from amica_python_sdk.models.area_geografica import AreaGeografica

# TODO update the JSON string below
json = "{}"
# create an instance of AreaGeografica from a JSON string
area_geografica_instance = AreaGeografica.from_json(json)
# print the JSON string representation of the object
print(AreaGeografica.to_json())

# convert the object into a dict
area_geografica_dict = area_geografica_instance.to_dict()
# create an instance of AreaGeografica from a dict
area_geografica_from_dict = AreaGeografica.from_dict(area_geografica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


