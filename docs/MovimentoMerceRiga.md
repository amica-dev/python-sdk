# MovimentoMerceRiga

Riga di un movimento di magazzino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**movimento_merce_id** | **int** | Identificativo univoco di &#x60;MovimentoMerce&#x60;. | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**listino_id** | **int** | Identificativo univoco di &#x60;Listino&#x60;. | [optional] 
**magazzino_id** | **int** | Identificativo univoco di &#x60;Magazzino&#x60;. | [optional] 
**prezzo_id** | **int** | Identificativo univoco di &#x60;Prezzo&#x60;. | [optional] 
**prezzo** | [**Prezzo**](Prezzo.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di &#x60;CausaleIva&#x60;. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**taglia_id** | **int** | Identificativo univoco di &#x60;Taglia&#x60;. | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**quantit** | **float** | Quantità movimentata. | [optional] 
**prezzo_netto** | **float** | Prezzo applicato, al netto dell&#39;IVA. | [optional] 
**prezzo_ivato** | **float** | Prezzo applicato, IVA inclusa. | [optional] 
**colore** | **str** | Colore. | [optional] 
**identificativo** | **str** | Numero di serie o altro identificativo del prodotto. | [optional] 
**identificativo_esteso** | **str** | Identificativo esteso del prodotto. | [optional] 
**data** | **datetime** | Data di scadenza, produzione, fine garanzia o altro. | [optional] 

## Example

```python
from amica_python_sdk.models.movimento_merce_riga import MovimentoMerceRiga

# TODO update the JSON string below
json = "{}"
# create an instance of MovimentoMerceRiga from a JSON string
movimento_merce_riga_instance = MovimentoMerceRiga.from_json(json)
# print the JSON string representation of the object
print(MovimentoMerceRiga.to_json())

# convert the object into a dict
movimento_merce_riga_dict = movimento_merce_riga_instance.to_dict()
# create an instance of MovimentoMerceRiga from a dict
movimento_merce_riga_from_dict = MovimentoMerceRiga.from_dict(movimento_merce_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


