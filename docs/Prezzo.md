# Prezzo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**listino_id** | **int** |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**prestazione_id** | **int** |  | [optional] 
**prestazione** | [**Articolo**](Articolo.md) |  | [optional] 
**importo** | **float** |  | [optional] 
**sconto1** | **float** |  | [optional] 
**sconto2** | **float** |  | [optional] 
**sconto3** | **float** |  | [optional] 
**sconto4** | **float** |  | [optional] 
**ricarico** | **float** |  | [optional] 
**provvigione_agente** | **float** |  | [optional] 
**provvigione_capo_area** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.prezzo import Prezzo

# TODO update the JSON string below
json = "{}"
# create an instance of Prezzo from a JSON string
prezzo_instance = Prezzo.from_json(json)
# print the JSON string representation of the object
print(Prezzo.to_json())

# convert the object into a dict
prezzo_dict = prezzo_instance.to_dict()
# create an instance of Prezzo from a dict
prezzo_from_dict = Prezzo.from_dict(prezzo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


