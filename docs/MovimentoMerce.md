# MovimentoMerce

Movimento di magazzino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**modalita_pagamento_id** | **int** | Identificativo univoco di Amica.MovimentoMerce.ModalitaPagamento. | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**causale_magazzino_id** | **int** | Identificativo univoco di Amica.MovimentoMerce.CausaleMagazzino. | [optional] 
**causale_magazzino** | [**CausaleMagazzino**](CausaleMagazzino.md) |  | [optional] 
**anagrafica_id** | **int** | Identificativo univoco di Amica.MovimentoMerce.Anagrafica. | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**documento_id** | **int** | Identificativo univoco di Amica.Documento. | [optional] 
**iva_esclusa** | **bool** | Indica se i prezzi inseriti sono da considerarsi al netto dell&#39;IVA. Se &#x60;false&#x60;, l&#39;IVA verrà scorporata in fase di elaborazione (app ufficiali). | [optional] 
**data** | **datetime** | Data del movimento. | [optional] 
**descrizione** | **str** | Descrizione. | [optional] 
**documento_numero** | **str** | Numero del documento di riferimento. | [optional] 
**documento_data** | **datetime** | Data del documento di riferimento. | [optional] 
**note** | **str** | Note. | [optional] 
**righe** | [**List[MovimentoMerceRiga]**](MovimentoMerceRiga.md) | Righe del movimento. | [optional] 

## Example

```python
from amica_sdk.models.movimento_merce import MovimentoMerce

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


