# ProgressivoInvio

Numero progressivo di invio al Sistema di Interscambio (SdI).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**documento_id** | **int** | Riferimento a Amica.Documento. | [optional] 
**progressivo** | **str** | Numero progressivo di invio al Sistema di Interscambio (SdI). | 

## Example

```python
from amica_python_sdk.models.progressivo_invio import ProgressivoInvio

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressivoInvio from a JSON string
progressivo_invio_instance = ProgressivoInvio.from_json(json)
# print the JSON string representation of the object
print(ProgressivoInvio.to_json())

# convert the object into a dict
progressivo_invio_dict = progressivo_invio_instance.to_dict()
# create an instance of ProgressivoInvio from a dict
progressivo_invio_from_dict = ProgressivoInvio.from_dict(progressivo_invio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


