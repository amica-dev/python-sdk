# FatturaElettronicaExportResult

Esito della chiamata al metodo M:Amica.FatturaElettronicaXmlService.XmlExport(Amica.FatturaElettronicaExportOptions,Amica.RequestSettings) di `FatturaElettronicaXmlService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Nome del file. | [optional] 
**valido** | **bool** | Indica se la fattura elettronica (XML) generata ha superato il test di validazione secondo le specifiche del Sistema di Interscambio (SdI). Se &#x60;false&#x60;, vedi Amica.FatturaElettronicaExportResult.Errori per l&#39;elenco degli errori di validazione. | [optional] [readonly] 
**errori** | **List[str]** | Errori di validazione, se presenti. | [optional] 
**xml** | **str** | Contenuto del file. | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaExportResult from a JSON string
fattura_elettronica_export_result_instance = FatturaElettronicaExportResult.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaExportResult.to_json())

# convert the object into a dict
fattura_elettronica_export_result_dict = fattura_elettronica_export_result_instance.to_dict()
# create an instance of FatturaElettronicaExportResult from a dict
fattura_elettronica_export_result_from_dict = FatturaElettronicaExportResult.from_dict(fattura_elettronica_export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


