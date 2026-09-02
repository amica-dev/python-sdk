# DocumentoMediaFile

File multimediale del documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**data** | **str** | Rappresentazione in Base64 del contenuto di un file multimediale. | [optional] 
**documento_id** | **int** | Identificativo univoco di &#x60;Documento&#x60;. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_media_file import DocumentoMediaFile

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoMediaFile from a JSON string
documento_media_file_instance = DocumentoMediaFile.from_json(json)
# print the JSON string representation of the object
print(DocumentoMediaFile.to_json())

# convert the object into a dict
documento_media_file_dict = documento_media_file_instance.to_dict()
# create an instance of DocumentoMediaFile from a dict
documento_media_file_from_dict = DocumentoMediaFile.from_dict(documento_media_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


