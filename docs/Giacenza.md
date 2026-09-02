# Giacenza

Giacenza corrente (inventario).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**magazzino_id** | **int** | Identificativo univoco di &#x60;Magazzino&#x60;. | [optional] 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**quantit_in_giacenza** | **float** | Quantità in giacenza. | [optional] 
**quantit_impegnata** | **float** | Quantità impegnata. | [optional] 
**quantit_ordinata** | **float** | Quantità ordinata. | [optional] 
**scorta_minima** | **float** | Scorta minima. | [optional] 
**gestione_sottoscorta** | **bool** | Indica se devono essere generati gli avvisi di sottoscorta. | [optional] 
**data_ultimo_carico** | **datetime** | Data dell&#39;ultimo carico. | [optional] 
**data_ultimo_scarico** | **datetime** | Data dell&#39;ultimo scarico. | [optional] 
**carico_quantit** | **float** | Quantità totale caricata. | [optional] 
**carico_valore** | **float** | Valore totale caricato. | [optional] 
**scarico_quantit** | **float** | Quantità totale scaricata. | [optional] 
**scarico_valore** | **float** | Valore totale scaricato. | [optional] 
**identificativo** | **str** | Numero di serie, o qualsiasi altro identificativo. | [optional] 
**identificativo_esteso** | **str** | Identificativo esteso. | [optional] 
**data** | **datetime** | Data di scadenza, produzione, fine garanzia o altro. | [optional] 
**colore** | **str** | Colore. | [optional] 

## Example

```python
from amica_python_sdk.models.giacenza import Giacenza

# TODO update the JSON string below
json = "{}"
# create an instance of Giacenza from a JSON string
giacenza_instance = Giacenza.from_json(json)
# print the JSON string representation of the object
print(Giacenza.to_json())

# convert the object into a dict
giacenza_dict = giacenza_instance.to_dict()
# create an instance of Giacenza from a dict
giacenza_from_dict = Giacenza.from_dict(giacenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


