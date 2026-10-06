# InventarioRiga

Riga di un inventario: quantità e valore di un articolo, per variante (identificativo, colore, data).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**inventario_id** | **int** | Identificativo univoco di &#x60;Inventario&#x60;. | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**quantit** | **float** | Quantità inventariata. | [optional] 
**valore** | **float** | Valore totale della riga: quantità per costo unitario. | [optional] 
**identificativo** | **str** | Numero di serie o altro identificativo del prodotto. | [optional] 
**identificativo_esteso** | **str** | Identificativo esteso. | [optional] 
**data** | **datetime** | Data di scadenza, produzione, fine garanzia o altro. | [optional] 
**colore** | **str** | Colore. | [optional] 

## Example

```python
from amica_python_sdk.models.inventario_riga import InventarioRiga

# TODO update the JSON string below
json = "{}"
# create an instance of InventarioRiga from a JSON string
inventario_riga_instance = InventarioRiga.from_json(json)
# print the JSON string representation of the object
print(InventarioRiga.to_json())

# convert the object into a dict
inventario_riga_dict = inventario_riga_instance.to_dict()
# create an instance of InventarioRiga from a dict
inventario_riga_from_dict = InventarioRiga.from_dict(inventario_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


