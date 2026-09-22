# BeneServizioComputeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prezzo** | **float** |  | [optional] 
**prezzo_ivato** | **float** |  | [optional] 
**prezzo_scontato** | **float** |  | [optional] 
**importo** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.bene_servizio_compute_result import BeneServizioComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of BeneServizioComputeResult from a JSON string
bene_servizio_compute_result_instance = BeneServizioComputeResult.from_json(json)
# print the JSON string representation of the object
print(BeneServizioComputeResult.to_json())

# convert the object into a dict
bene_servizio_compute_result_dict = bene_servizio_compute_result_instance.to_dict()
# create an instance of BeneServizioComputeResult from a dict
bene_servizio_compute_result_from_dict = BeneServizioComputeResult.from_dict(bene_servizio_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


