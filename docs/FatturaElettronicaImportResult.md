# FatturaElettronicaImportResult

Esito della chiamata al metodo M:Amica.FatturaElettronicaXmlService.XmlImport(Amica.FatturaElettronicaImportOptions,System.Byte[],System.String,Amica.RequestSettings) di `FatturaElettronicaXmlService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documento_id** | **int** | Identificativo univoco di Amica.Documento. | [optional] 
**messaggi** | **List[str]** | Messaggi relativi alla procedura di importazione. | [optional] 
**esito** | **str** | Esito dell&#39;importazione (&#x60;OK&#x60;, &#x60;OK con messaggi&#x60;, &#x60;SCARTATO (DUPLICATO)&#x60;, ecc.) | [optional] 
**is_success** | **bool** | Indica se l&#39;importazione è andata a buon fine. | [optional] [readonly] 

## Example

```python
from amica_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaImportResult from a JSON string
fattura_elettronica_import_result_instance = FatturaElettronicaImportResult.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaImportResult.to_json())

# convert the object into a dict
fattura_elettronica_import_result_dict = fattura_elettronica_import_result_instance.to_dict()
# create an instance of FatturaElettronicaImportResult from a dict
fattura_elettronica_import_result_from_dict = FatturaElettronicaImportResult.from_dict(fattura_elettronica_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


