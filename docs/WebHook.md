# WebHook

Metadati del webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**azienda_id** | **int** | Azienda per cui il webhook deve essere attivo. Impostare a &#x60;null&#x60; se il webhook deve essere attivo per tutte le aziende. | [optional] 
**url** | **str** | L&#39;URL del webhook. È l&#39;endpoint della tua integrazione che riceverà la richiesta POST quando gli Amica.WebHook.Events indicati vengono scatenati. Sono accettati solo URL https. | [optional] 
**enabled** | **bool** | Indica se il webhook è abilitato o meno. Alla creazione viene impostato a &#x60;true&#x60;. | [optional] 
**secret** | **str** | Il segreto usato per generare le firme del webhook. Restituito alla creazione del webhook e mai aggiornabile. | [optional] 
**description** | **str** | Una descrizione opzionale dell&#39;utilizzo del webhook. | [optional] 
**events** | **List[str]** | Elenco degli eventi da abilitare per questo endpoint. Vedi Amica.Eventi.Available per l&#39;elenco dei nomi di evento validi. | [optional] 

## Example

```python
from amica_sdk.models.web_hook import WebHook

# TODO update the JSON string below
json = "{}"
# create an instance of WebHook from a JSON string
web_hook_instance = WebHook.from_json(json)
# print the JSON string representation of the object
print(WebHook.to_json())

# convert the object into a dict
web_hook_dict = web_hook_instance.to_dict()
# create an instance of WebHook from a dict
web_hook_from_dict = WebHook.from_dict(web_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


