# DocumentoTotali

Totali di un gruppo di documenti, calcolati dal server. Le note di credito sono sottratte.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodo** | **datetime** | Primo giorno del mese o dell&#39;anno del gruppo, se il raggruppamento è per periodo. | [optional] 
**anagrafica_id** | **int** | Identificativo univoco dell&#39;&#x60;Anagrafica&#x60; del gruppo, se il raggruppamento è per anagrafica. | [optional] 
**ragione_sociale** | **str** | Ragione sociale dell&#39;&#x60;Anagrafica&#x60; del gruppo, se il raggruppamento è per anagrafica. | [optional] 
**documenti** | **int** | Numero di documenti del gruppo. | [optional] 
**totale_imponibile** | **float** | Somma degli imponibili. | [optional] 
**totale_esente** | **float** | Somma degli importi esenti. | [optional] 
**totale_imposta** | **float** | Somma delle imposte. | [optional] 
**totale_documento** | **float** | Somma dei totali documento. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_totali import DocumentoTotali

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoTotali from a JSON string
documento_totali_instance = DocumentoTotali.from_json(json)
# print the JSON string representation of the object
print(DocumentoTotali.to_json())

# convert the object into a dict
documento_totali_dict = documento_totali_instance.to_dict()
# create an instance of DocumentoTotali from a dict
documento_totali_from_dict = DocumentoTotali.from_dict(documento_totali_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


