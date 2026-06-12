# Prestazione

Erogazione di una prestazione.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**categoria_merceologica_id** | **int** | Identificativo univoco di Amica.Prestazione.CategoriaMerceologica. | [optional] 
**categoria_merceologica** | [**CategoriaMerceologica**](CategoriaMerceologica.md) |  | [optional] 
**gruppo_merceologico_id** | **int** | Identificativo univoco di Amica.Prestazione.GruppoMerceologico. | [optional] 
**gruppo_merceologico** | [**GruppoMerceologico**](GruppoMerceologico.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di Amica.Prestazione.CausaleIva. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**nome** | **str** | Nome. | 
**codice** | **str** | Codice. | 
**bar_code** | **str** | Codice a barre. | [optional] 
**stato** | **bool** | Indica se è attiva o meno. | [optional] 
**note** | **str** | Note. | [optional] 

## Example

```python
from amica_python_sdk.models.prestazione import Prestazione

# TODO update the JSON string below
json = "{}"
# create an instance of Prestazione from a JSON string
prestazione_instance = Prestazione.from_json(json)
# print the JSON string representation of the object
print(Prestazione.to_json())

# convert the object into a dict
prestazione_dict = prestazione_instance.to_dict()
# create an instance of Prestazione from a dict
prestazione_from_dict = Prestazione.from_dict(prestazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


