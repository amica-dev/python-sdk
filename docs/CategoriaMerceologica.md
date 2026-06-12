# CategoriaMerceologica

Categoria merceologica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome o descrizione. | 

## Example

```python
from amica_python_sdk.models.categoria_merceologica import CategoriaMerceologica

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriaMerceologica from a JSON string
categoria_merceologica_instance = CategoriaMerceologica.from_json(json)
# print the JSON string representation of the object
print(CategoriaMerceologica.to_json())

# convert the object into a dict
categoria_merceologica_dict = categoria_merceologica_instance.to_dict()
# create an instance of CategoriaMerceologica from a dict
categoria_merceologica_from_dict = CategoriaMerceologica.from_dict(categoria_merceologica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


