# RicercaArticolo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**vendite_campo1** | **str** |  | [optional] 
**vendite_campo2** | **str** |  | [optional] 
**vendite_campo3** | **str** |  | [optional] 
**vendite_campo4** | **str** |  | [optional] 
**acquisti_campo1** | **str** |  | [optional] 
**acquisti_campo2** | **str** |  | [optional] 
**acquisti_campo3** | **str** |  | [optional] 
**acquisti_campo4** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.ricerca_articolo import RicercaArticolo

# TODO update the JSON string below
json = "{}"
# create an instance of RicercaArticolo from a JSON string
ricerca_articolo_instance = RicercaArticolo.from_json(json)
# print the JSON string representation of the object
print(RicercaArticolo.to_json())

# convert the object into a dict
ricerca_articolo_dict = ricerca_articolo_instance.to_dict()
# create an instance of RicercaArticolo from a dict
ricerca_articolo_from_dict = RicercaArticolo.from_dict(ricerca_articolo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


