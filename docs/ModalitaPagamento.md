# ModalitaPagamento

Modalità di pagamento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome, o descrizione. | 
**codice_pagamento_fe** | **str** | Codice corrispondente per la fattura elettronica (es. \&quot;MP01\&quot;). | [optional] 
**ricevuta_bancaria** | **bool** | Indica se è una ricevuta bancaria o meno. | [optional] 

## Example

```python
from amica_sdk.models.modalita_pagamento import ModalitaPagamento

# TODO update the JSON string below
json = "{}"
# create an instance of ModalitaPagamento from a JSON string
modalita_pagamento_instance = ModalitaPagamento.from_json(json)
# print the JSON string representation of the object
print(ModalitaPagamento.to_json())

# convert the object into a dict
modalita_pagamento_dict = modalita_pagamento_instance.to_dict()
# create an instance of ModalitaPagamento from a dict
modalita_pagamento_from_dict = ModalitaPagamento.from_dict(modalita_pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


