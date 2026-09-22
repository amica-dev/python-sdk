# FatturaElettronicaXmlGetArchiveByDateRangeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 
**classe_documento** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_date_range_options import FatturaElettronicaXmlGetArchiveByDateRangeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaXmlGetArchiveByDateRangeOptions from a JSON string
fattura_elettronica_xml_get_archive_by_date_range_options_instance = FatturaElettronicaXmlGetArchiveByDateRangeOptions.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaXmlGetArchiveByDateRangeOptions.to_json())

# convert the object into a dict
fattura_elettronica_xml_get_archive_by_date_range_options_dict = fattura_elettronica_xml_get_archive_by_date_range_options_instance.to_dict()
# create an instance of FatturaElettronicaXmlGetArchiveByDateRangeOptions from a dict
fattura_elettronica_xml_get_archive_by_date_range_options_from_dict = FatturaElettronicaXmlGetArchiveByDateRangeOptions.from_dict(fattura_elettronica_xml_get_archive_by_date_range_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


