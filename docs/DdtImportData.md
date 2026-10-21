# DdtImportData

Dati di importazione del DDT.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[int]** | Identificativo del documento da importare. | [optional] 
**tipo_importazione** | **str** | Indica se importare i totali del documento o tutti i dati, e se gli articoli dello stesso tipo debbano essere accorpati. | [optional] 
**spese_incluse** | **bool** | Indica se importare nella fattura le spese dei DDT, in tutte le modalità di importazione. Le spese dello stesso tipo si sommano, anche a quelle che la fattura ha già. Se &#x60;false&#x60;, le spese dei DDT non vengono importate. | [optional] 

## Example

```python
from amica_python_sdk.models.ddt_import_data import DdtImportData

# TODO update the JSON string below
json = "{}"
# create an instance of DdtImportData from a JSON string
ddt_import_data_instance = DdtImportData.from_json(json)
# print the JSON string representation of the object
print(DdtImportData.to_json())

# convert the object into a dict
ddt_import_data_dict = ddt_import_data_instance.to_dict()
# create an instance of DdtImportData from a dict
ddt_import_data_from_dict = DdtImportData.from_dict(ddt_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


