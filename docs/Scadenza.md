# Scadenza


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**registrazione_contabile_id** | **int** |  | [optional] 
**registrazione_contabile** | [**RegistrazioneContabile**](RegistrazioneContabile.md) |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**documento_id** | **int** |  | [optional] 
**documento** | [**Documento**](Documento.md) |  | [optional] 
**modalita_pagamento_id** | **int** |  | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**pagata_manualmente** | **bool** |  | [optional] 
**pagata** | **bool** |  | [optional] [readonly] 
**data** | **datetime** |  | [optional] 
**data_pagamento** | **datetime** |  | [optional] 
**data_documento** | **datetime** |  | [optional] 
**importo** | **float** |  | [optional] 
**partita_anno** | **int** |  | [optional] 
**partita_numero** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**documento_numero_parte_numerica** | **int** |  | [optional] 
**documento_numero_parte_testo** | **str** |  | [optional] 
**documento_numero** | **str** |  | [optional] 
**tipo_scadenza** | **str** |  | [optional] 
**importo_pagato** | **float** |  | [optional] 
**importo_da_pagare** | **float** |  | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.scadenza import Scadenza

# TODO update the JSON string below
json = "{}"
# create an instance of Scadenza from a JSON string
scadenza_instance = Scadenza.from_json(json)
# print the JSON string representation of the object
print(Scadenza.to_json())

# convert the object into a dict
scadenza_dict = scadenza_instance.to_dict()
# create an instance of Scadenza from a dict
scadenza_from_dict = Scadenza.from_dict(scadenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


