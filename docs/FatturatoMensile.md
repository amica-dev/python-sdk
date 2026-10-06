# FatturatoMensile

Fatturato mensile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodo** | **datetime** | Periodo di riferimento. | [optional] 
**importo** | **float** | Importo per il periodo. | [optional] 

## Example

```python
from amica_python_sdk.models.fatturato_mensile import FatturatoMensile

# TODO update the JSON string below
json = "{}"
# create an instance of FatturatoMensile from a JSON string
fatturato_mensile_instance = FatturatoMensile.from_json(json)
# print the JSON string representation of the object
print(FatturatoMensile.to_json())

# convert the object into a dict
fatturato_mensile_dict = fatturato_mensile_instance.to_dict()
# create an instance of FatturatoMensile from a dict
fatturato_mensile_from_dict = FatturatoMensile.from_dict(fatturato_mensile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


