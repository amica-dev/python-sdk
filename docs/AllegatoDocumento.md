# AllegatoDocumento

Rappresentazione binaria, con metadati, di un allegato XML (\"fattura elettronica\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** | Nome dell&#39;allegato. | [optional] 
**descrizione** | **str** | Descrizione dell&#39;allegato. | [optional] 
**formato** | **str** | Formato dell&#39;allegato. Esempi validi sono \&quot;PDF\&quot;, \&quot;XML\&quot;, \&quot;TXT\&quot;, \&quot;DOC\&quot;, ecc. | [optional] 
**data_documento** | **datetime** | Data dell&#39;allegato. | [optional] 
**numero_documento** | **str** | Numero dell&#39;allegato. | [optional] 
**allegato** | **bytearray** | Rappresentazione binaria dell&#39;allegato. Questo campo contiene l&#39;allegato stesso. | [optional] 

## Example

```python
from amica_sdk.models.allegato_documento import AllegatoDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of AllegatoDocumento from a JSON string
allegato_documento_instance = AllegatoDocumento.from_json(json)
# print the JSON string representation of the object
print(AllegatoDocumento.to_json())

# convert the object into a dict
allegato_documento_dict = allegato_documento_instance.to_dict()
# create an instance of AllegatoDocumento from a dict
allegato_documento_from_dict = AllegatoDocumento.from_dict(allegato_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


