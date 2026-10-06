# InventarioComputeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**righe** | [**List[InventarioRiga]**](InventarioRiga.md) |  | [optional] 
**avvisi** | **List[str]** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**giacenze_allineabili** | **bool** |  | [optional] 
**inventario** | [**Inventario**](Inventario.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.inventario_compute_result import InventarioComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of InventarioComputeResult from a JSON string
inventario_compute_result_instance = InventarioComputeResult.from_json(json)
# print the JSON string representation of the object
print(InventarioComputeResult.to_json())

# convert the object into a dict
inventario_compute_result_dict = inventario_compute_result_instance.to_dict()
# create an instance of InventarioComputeResult from a dict
inventario_compute_result_from_dict = InventarioComputeResult.from_dict(inventario_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


