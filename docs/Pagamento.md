# Pagamento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**modalita_pagamento_id** | **int** |  | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**spesa_id** | **int** |  | [optional] 
**spesa** | [**Spesa**](Spesa.md) |  | [optional] 
**risorsa_finanziaria_id** | **int** |  | [optional] 
**risorsa_finanziaria** | [**RisorsaFinanziaria**](RisorsaFinanziaria.md) |  | [optional] 
**nome** | **str** |  | 
**calcolo_prima_rata** | **str** |  | [optional] 
**decorrenza_prima_rata** | **str** |  | [optional] 
**giorni_aggiuntivi** | **int** |  | [optional] 
**sconto** | **float** |  | [optional] 
**inizio_scadenze** | **int** |  | [optional] 
**periodicit** | **int** |  | [optional] 
**fine_mese** | **bool** |  | [optional] 
**giorni_esatti** | **bool** |  | [optional] 
**rate** | **int** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.pagamento import Pagamento

# TODO update the JSON string below
json = "{}"
# create an instance of Pagamento from a JSON string
pagamento_instance = Pagamento.from_json(json)
# print the JSON string representation of the object
print(Pagamento.to_json())

# convert the object into a dict
pagamento_dict = pagamento_instance.to_dict()
# create an instance of Pagamento from a dict
pagamento_from_dict = Pagamento.from_dict(pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


