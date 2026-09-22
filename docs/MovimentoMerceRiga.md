# MovimentoMerceRiga


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**movimento_merce_id** | **int** |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**listino_id** | **int** |  | [optional] 
**magazzino_id** | **int** |  | [optional] 
**prezzo_id** | **int** |  | [optional] 
**prezzo** | [**Prezzo**](Prezzo.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**taglia_id** | **int** |  | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**quantit** | **float** |  | [optional] 
**prezzo_netto** | **float** |  | [optional] 
**prezzo_ivato** | **float** |  | [optional] 
**colore** | **str** |  | [optional] 
**identificativo** | **str** |  | [optional] 
**identificativo_esteso** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 

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


