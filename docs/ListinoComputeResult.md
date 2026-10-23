# ListinoComputeResult

Restituito dal metodo `Compute` di `ListinoService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listino** | [**Listino**](Listino.md) |  | [optional] 
**avvisi** | **List[str]** | Avvisi della procedura, da mostrare all&#39;utente. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_result import ListinoComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeResult from a JSON string
listino_compute_result_instance = ListinoComputeResult.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeResult.to_json())

# convert the object into a dict
listino_compute_result_dict = listino_compute_result_instance.to_dict()
# create an instance of ListinoComputeResult from a dict
listino_compute_result_from_dict = ListinoComputeResult.from_dict(listino_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


