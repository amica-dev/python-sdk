# ArticoloMediaFile

Rappresentazione di un file multimediale associato al prodotto o articolo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**data** | **str** | Rappresentazione in Base64 del contenuto di un file multimediale. | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. | [optional] 
**field_name** | **str** | Nome (tipo) dell&#39;informazione. Solitamente &#39;immagine&#39;. | [optional] 

## Example

```python
from amica_python_sdk.models.articolo_media_file import ArticoloMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of ArticoloMediaFile from a JSON string
articolo_media_file_instance = ArticoloMediaFile.from_json(json)
# print the JSON string representation of the object
print(ArticoloMediaFile.to_json())

# convert the object into a dict
articolo_media_file_dict = articolo_media_file_instance.to_dict()
# create an instance of ArticoloMediaFile from a dict
articolo_media_file_from_dict = ArticoloMediaFile.from_dict(articolo_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


