# ListinoComputeSconti

Parametri della procedura `Sconti`: i quattro sconti da assegnare a ogni riga, come frazione (`0.10` corrisponde al 10%).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sconto1** | **float** | Primo sconto. | [optional] 
**sconto2** | **float** | Secondo sconto. | [optional] 
**sconto3** | **float** | Terzo sconto. | [optional] 
**sconto4** | **float** | Quarto sconto. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_sconti import ListinoComputeSconti

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeSconti from a JSON string
listino_compute_sconti_instance = ListinoComputeSconti.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeSconti.to_json())

# convert the object into a dict
listino_compute_sconti_dict = listino_compute_sconti_instance.to_dict()
# create an instance of ListinoComputeSconti from a dict
listino_compute_sconti_from_dict = ListinoComputeSconti.from_dict(listino_compute_sconti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


