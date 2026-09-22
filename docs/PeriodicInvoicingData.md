# PeriodicInvoicingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**da** | **datetime** |  | [optional] 
**a** | **datetime** |  | [optional] 
**tipo_importazione** | **str** |  | [optional] 
**causale_documento_id** | **int** |  | [optional] 
**data_documento** | **datetime** |  | [optional] 
**tipo_documento** | **str** |  | [optional] 

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


