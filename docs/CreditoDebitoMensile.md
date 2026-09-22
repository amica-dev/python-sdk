# CreditoDebitoMensile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodo** | **datetime** |  | [optional] 
**credito** | **float** |  | [optional] 
**debito** | **float** |  | [optional] 
**saldo** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.credito_debito_mensile import CreditoDebitoMensile

# TODO update the JSON string below
json = "{}"
# create an instance of CreditoDebitoMensile from a JSON string
credito_debito_mensile_instance = CreditoDebitoMensile.from_json(json)
# print the JSON string representation of the object
print(CreditoDebitoMensile.to_json())

# convert the object into a dict
credito_debito_mensile_dict = credito_debito_mensile_instance.to_dict()
# create an instance of CreditoDebitoMensile from a dict
credito_debito_mensile_from_dict = CreditoDebitoMensile.from_dict(credito_debito_mensile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


