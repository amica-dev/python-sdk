# MovimentoMerce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**modalita_pagamento_id** | **int** |  | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**causale_magazzino_id** | **int** |  | [optional] 
**causale_magazzino** | [**CausaleMagazzino**](CausaleMagazzino.md) |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**documento_id** | **int** |  | [optional] 
**iva_esclusa** | **bool** |  | [optional] 
**data** | **datetime** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**documento_numero** | **str** |  | [optional] 
**documento_data** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**righe** | [**List[MovimentoMerceRiga]**](MovimentoMerceRiga.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.movimento_merce import MovimentoMerce

# TODO update the JSON string below
json = "{}"
# create an instance of MovimentoMerce from a JSON string
movimento_merce_instance = MovimentoMerce.from_json(json)
# print the JSON string representation of the object
print(MovimentoMerce.to_json())

# convert the object into a dict
movimento_merce_dict = movimento_merce_instance.to_dict()
# create an instance of MovimentoMerce from a dict
movimento_merce_from_dict = MovimentoMerce.from_dict(movimento_merce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


