# ModelloContabile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**codice** | **str** |  | 
**nome** | **str** |  | 
**stato** | **bool** |  | [optional] 
**registro_iva_id** | **int** |  | [optional] 
**segno_iva** | **str** |  | [optional] 
**tipo_operazione_contabile** | **str** |  | [optional] 
**tipo_registrazione_contabile** | **str** |  | [optional] 
**azione_partita** | **str** |  | [optional] 
**righe** | [**List[ModelloContabileRiga]**](ModelloContabileRiga.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.modello_contabile import ModelloContabile

# TODO update the JSON string below
json = "{}"
# create an instance of ModelloContabile from a JSON string
modello_contabile_instance = ModelloContabile.from_json(json)
# print the JSON string representation of the object
print(ModelloContabile.to_json())

# convert the object into a dict
modello_contabile_dict = modello_contabile_instance.to_dict()
# create an instance of ModelloContabile from a dict
modello_contabile_from_dict = ModelloContabile.from_dict(modello_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


