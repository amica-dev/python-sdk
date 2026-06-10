# OrdiniImportData

Dati di importazione dell'ordine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[int]** | Identificativo del documento da importare. | [optional] 
**solo_righe** | **bool** | Importa solo le righe del documento. | [optional] 
**includi_riferimento** | **bool** | Aggiunge un riferimento al documento. | [optional] 

## Example

```python
from amica_sdk.models.ordini_import_data import OrdiniImportData

# TODO update the JSON string below
json = "{}"
# create an instance of OrdiniImportData from a JSON string
ordini_import_data_instance = OrdiniImportData.from_json(json)
# print the JSON string representation of the object
print(OrdiniImportData.to_json())

# convert the object into a dict
ordini_import_data_dict = ordini_import_data_instance.to_dict()
# create an instance of OrdiniImportData from a dict
ordini_import_data_from_dict = OrdiniImportData.from_dict(ordini_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


