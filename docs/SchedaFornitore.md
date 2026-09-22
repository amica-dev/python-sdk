# SchedaFornitore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**pagamento_id** | **int** |  | [optional] 
**pagamento** | [**Pagamento**](Pagamento.md) |  | [optional] 
**listino_id** | **int** |  | [optional] 
**listino** | [**Listino**](Listino.md) |  | [optional] 
**capo_area_id** | **int** |  | [optional] 
**capo_area** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**categoria_anagrafica_id** | **int** |  | [optional] 
**categoria_anagrafica** | [**CategoriaAnagrafica**](CategoriaAnagrafica.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**fatturato_anno_corrente** | **float** |  | [optional] 
**numero_fatture_anno_corrente** | **int** |  | [optional] 
**insoluti_anno_corrente** | **float** |  | [optional] 
**numero_insoluti_anno_corrente** | **int** |  | [optional] 
**fatturato_anno_precedente** | **float** |  | [optional] 
**numero_fatture_anno_precedente** | **int** |  | [optional] 
**insoluti_anno_precedente** | **float** |  | [optional] 
**numero_insoluti_anno_precedente** | **int** |  | [optional] 
**data_ultima_fattura** | **datetime** |  | [optional] 
**data_ultimo_pagamento** | **datetime** |  | [optional] 
**data_ultimo_insoluto** | **datetime** |  | [optional] 
**conto_raw** | **str** |  | [optional] 
**conto** | **str** |  | [optional] [readonly] 
**iscrizione_ruolo** | **str** |  | [optional] 
**enasarco** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.scheda_fornitore import SchedaFornitore

# TODO update the JSON string below
json = "{}"
# create an instance of SchedaFornitore from a JSON string
scheda_fornitore_instance = SchedaFornitore.from_json(json)
# print the JSON string representation of the object
print(SchedaFornitore.to_json())

# convert the object into a dict
scheda_fornitore_dict = scheda_fornitore_instance.to_dict()
# create an instance of SchedaFornitore from a dict
scheda_fornitore_from_dict = SchedaFornitore.from_dict(scheda_fornitore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


