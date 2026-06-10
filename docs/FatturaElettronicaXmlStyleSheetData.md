# FatturaElettronicaXmlStyleSheetData

Opzioni per la chiamata al metodo M:Amica.FatturaElettronicaXmlService.ApplyStyleSheet(Amica.FatturaElettronicaXmlStyleSheetData,Amica.RequestSettings) di `FatturaElettronicaXmlService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco di Amica.FatturaElettronicaXml. In alternativa, valorizzare Amica.FatturaElettronicaXmlStyleSheetData.FileName. | [optional] 
**file_name** | **str** | Nome del file XML. Se presente, ha la precedenza su Amica.FatturaElettronicaXmlStyleSheetData.Id. | [optional] 
**style_sheet** | **str** | Foglio di stile da applicare. | [optional] 

## Example

```python
from amica_sdk.models.fattura_elettronica_xml_style_sheet_data import FatturaElettronicaXmlStyleSheetData

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaXmlStyleSheetData from a JSON string
fattura_elettronica_xml_style_sheet_data_instance = FatturaElettronicaXmlStyleSheetData.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaXmlStyleSheetData.to_json())

# convert the object into a dict
fattura_elettronica_xml_style_sheet_data_dict = fattura_elettronica_xml_style_sheet_data_instance.to_dict()
# create an instance of FatturaElettronicaXmlStyleSheetData from a dict
fattura_elettronica_xml_style_sheet_data_from_dict = FatturaElettronicaXmlStyleSheetData.from_dict(fattura_elettronica_xml_style_sheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


