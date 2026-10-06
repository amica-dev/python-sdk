# DocumentoCollegato

Dati di riferimento del documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **str** | Numero del documento. | [optional] 
**data** | **datetime** | Data del documento. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_collegato import DocumentoCollegato

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoCollegato from a JSON string
documento_collegato_instance = DocumentoCollegato.from_json(json)
# print the JSON string representation of the object
print(DocumentoCollegato.to_json())

# convert the object into a dict
documento_collegato_dict = documento_collegato_instance.to_dict()
# create an instance of DocumentoCollegato from a dict
documento_collegato_from_dict = DocumentoCollegato.from_dict(documento_collegato_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


