# Inventario

Inventario di magazzino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**magazzino_id** | **int** | Identificativo univoco di &#x60;Magazzino&#x60;. Obbligatorio in scrittura; può mancare negli inventari creati dal client Windows, che non si possono elaborare. | 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**data** | **datetime** | Data dell&#39;inventario: l&#39;elaborazione considera i movimenti fino a questa data inclusa. | 
**nome** | **str** | Nome o descrizione. | [optional] 
**fiscale** | **bool** | Indica se l&#39;inventario è fiscale. L&#39;elaborazione parte dall&#39;inventario fiscale precedente dello stesso magazzino. | [optional] 
**valorizzazione** | **str** | Criterio di valorizzazione delle righe. | 
**escludi_articoli_inattivi** | **bool** | Indica se l&#39;elaborazione deve escludere gli articoli non attivi. | [optional] 
**note** | **str** | Note. | [optional] 
**righe** | [**List[InventarioRiga]**](InventarioRiga.md) | Righe dell&#39;inventario. In sola lettura: le produce l&#39;elaborazione (&#x60;Process&#x60;). | [optional] 

## Example

```python
from amica_python_sdk.models.inventario import Inventario

# TODO update the JSON string below
json = "{}"
# create an instance of Inventario from a JSON string
inventario_instance = Inventario.from_json(json)
# print the JSON string representation of the object
print(Inventario.to_json())

# convert the object into a dict
inventario_dict = inventario_instance.to_dict()
# create an instance of Inventario from a dict
inventario_from_dict = Inventario.from_dict(inventario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


