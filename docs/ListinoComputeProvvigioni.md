# ListinoComputeProvvigioni

Parametri della procedura `Provvigioni`: le provvigioni da assegnare a ogni riga, come frazione (`0.05` corrisponde al 5%).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agente** | **float** | Provvigione dell&#39;agente. | [optional] 
**capo_area** | **float** | Provvigione del capo area. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_provvigioni import ListinoComputeProvvigioni

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeProvvigioni from a JSON string
listino_compute_provvigioni_instance = ListinoComputeProvvigioni.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeProvvigioni.to_json())

# convert the object into a dict
listino_compute_provvigioni_dict = listino_compute_provvigioni_instance.to_dict()
# create an instance of ListinoComputeProvvigioni from a dict
listino_compute_provvigioni_from_dict = ListinoComputeProvvigioni.from_dict(listino_compute_provvigioni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


