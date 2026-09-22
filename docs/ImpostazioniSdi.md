# ImpostazioniSdi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**api_key_sdi** | **str** |  | [optional] 
**ultimo_download_sdi** | **datetime** |  | [optional] 
**includi_pdf_sdi** | **bool** |  | [optional] 
**abbina_articoli_sdi** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.impostazioni_sdi import ImpostazioniSdi

# TODO update the JSON string below
json = "{}"
# create an instance of ImpostazioniSdi from a JSON string
impostazioni_sdi_instance = ImpostazioniSdi.from_json(json)
# print the JSON string representation of the object
print(ImpostazioniSdi.to_json())

# convert the object into a dict
impostazioni_sdi_dict = impostazioni_sdi_instance.to_dict()
# create an instance of ImpostazioniSdi from a dict
impostazioni_sdi_from_dict = ImpostazioniSdi.from_dict(impostazioni_sdi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


