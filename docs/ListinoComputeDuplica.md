# ListinoComputeDuplica

Parametri della procedura `Duplica`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listino_id** | **int** | Identificativo univoco del &#x60;Listino&#x60; da cui copiare le righe, clienti o fornitori. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_duplica import ListinoComputeDuplica

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeDuplica from a JSON string
listino_compute_duplica_instance = ListinoComputeDuplica.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeDuplica.to_json())

# convert the object into a dict
listino_compute_duplica_dict = listino_compute_duplica_instance.to_dict()
# create an instance of ListinoComputeDuplica from a dict
listino_compute_duplica_from_dict = ListinoComputeDuplica.from_dict(listino_compute_duplica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


