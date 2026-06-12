# Listino

Listino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**fornitore_id** | **int** | Identificativo univoco di Amica.Anagrafica (fornitore). | [optional] 
**fornitore** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**valuta_id** | **int** | Identificativo univoco di Amica.Listino.Valuta (valuta). | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**nome** | **str** | Nome del listino. | 
**iva_inclusa** | **bool** | Indica se i prezzi base sono IVA inclusa oppure no. | [optional] 
**ricarico** | **float** | Ricarico da applicare ai prezzi base di tutte le righe del listino. | [optional] 
**data_creazione** | **datetime** | Data di creazione. | [optional] 
**valido_dal** | **datetime** | Inizio validità del listino. | [optional] 
**valido_al** | **datetime** | Fine validità del listino. | [optional] 
**tipo_listino** | **str** | Tipo di listino. | [optional] 
**calcolo_prezzi** | **str** | Modalità di calcolo dei prezzi del listino. | [optional] 
**note** | **str** | Note. | [optional] 
**righe** | [**List[Prezzo]**](Prezzo.md) | Righe del listino. | [optional] 

## Example

```python
from amica_python_sdk.models.listino import Listino

# TODO update the JSON string below
json = "{}"
# create an instance of Listino from a JSON string
listino_instance = Listino.from_json(json)
# print the JSON string representation of the object
print(Listino.to_json())

# convert the object into a dict
listino_dict = listino_instance.to_dict()
# create an instance of Listino from a dict
listino_from_dict = Listino.from_dict(listino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


