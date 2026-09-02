# PeriodicInvoicingData

Dati di fatturazione periodica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**da** | **datetime** | Data di inizio del periodo. | [optional] 
**a** | **datetime** | Data di fine del periodo. | [optional] 
**tipo_importazione** | **str** | Tipo di importazione. | [optional] 
**causale_documento_id** | **int** | Identificativo univoco della &#x60;CausaleDocumento&#x60; del documento generato. | [optional] 
**data_documento** | **datetime** | Data del documento generato. | [optional] 
**tipo_documento** | **str** | Tipo del documento generato. | [optional] 

## Example

```python
from amica_python_sdk.models.periodic_invoicing_data import PeriodicInvoicingData

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicInvoicingData from a JSON string
periodic_invoicing_data_instance = PeriodicInvoicingData.from_json(json)
# print the JSON string representation of the object
print(PeriodicInvoicingData.to_json())

# convert the object into a dict
periodic_invoicing_data_dict = periodic_invoicing_data_instance.to_dict()
# create an instance of PeriodicInvoicingData from a dict
periodic_invoicing_data_from_dict = PeriodicInvoicingData.from_dict(periodic_invoicing_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


