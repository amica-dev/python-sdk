# BeneServizioComputeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iva_esclusa** | **bool** |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**listino_id** | **int** |  | [optional] 
**quantit** | **float** |  | [optional] 
**prezzo** | **float** |  | [optional] 
**prezzo_ivato** | **float** |  | [optional] 
**sconto1** | **float** |  | [optional] 
**sconto2** | **float** |  | [optional] 
**sconto3** | **float** |  | [optional] 
**sconto4** | **float** |  | [optional] 
**sconto_incondizionato** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.bene_servizio_compute_data import BeneServizioComputeData

# TODO update the JSON string below
json = "{}"
# create an instance of BeneServizioComputeData from a JSON string
bene_servizio_compute_data_instance = BeneServizioComputeData.from_json(json)
# print the JSON string representation of the object
print(BeneServizioComputeData.to_json())

# convert the object into a dict
bene_servizio_compute_data_dict = bene_servizio_compute_data_instance.to_dict()
# create an instance of BeneServizioComputeData from a dict
bene_servizio_compute_data_from_dict = BeneServizioComputeData.from_dict(bene_servizio_compute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


