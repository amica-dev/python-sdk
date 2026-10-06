# Pagamento

Pagamento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**modalita_pagamento_id** | **int** | Identificativo univoco di &#x60;ModalitaPagamento&#x60;. | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**spesa_id** | **int** | Identificativo univoco di &#x60;Spesa&#x60;. | [optional] 
**spesa** | [**Spesa**](Spesa.md) |  | [optional] 
**risorsa_finanziaria_id** | **int** | Identificativo univoco di &#x60;RisorsaFinanziaria&#x60;. | [optional] 
**risorsa_finanziaria** | [**RisorsaFinanziaria**](RisorsaFinanziaria.md) |  | [optional] 
**nome** | **str** | Nome, o descrizione. | 
**calcolo_prima_rata** | **str** | Se e come l&#39;IVA e le spese devono essere considerate nel calcolo della prima rata. | [optional] 
**decorrenza_prima_rata** | **str** | Da quando decorre il pagamento della prima rata. | [optional] 
**giorni_aggiuntivi** | **int** | Giorni extra da aggiungere ad ogni scadenza. | [optional] 
**sconto** | **float** | Sconto riconosciuto per l&#39;utilizzo del pagamento (percentuale). | [optional] 
**inizio_scadenze** | **int** | Periodicità della prima rata. Per le successive, impostare &#x60;Periodicità&#x60;. | [optional] 
**periodicit** | **int** | Periodicità delle rate successive alla prima. Per la prima rata, impostare &#x60;InizioScadenze&#x60;. Default impostato a 30. | [optional] 
**fine_mese** | **bool** | Indica se le scadenze devono essere riportate a fine mese. | [optional] 
**giorni_esatti** | **bool** | Indica se il pagamento è utilizzato nel caso di &#39;Art. 62 prodotti alimentari (giorni esatti)&#39;. | [optional] 
**rate** | **int** | Numero di rate. | [optional] 
**note** | **str** | Note. | [optional] 

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


