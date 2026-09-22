# CastellettoIva


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**registrazione_contabile_id** | **int** |  | [optional] 
**registrazione_contabile** | [**RegistrazioneContabile**](RegistrazioneContabile.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**registro_iva_id** | **int** |  | [optional] 
**imponibile** | **float** |  | [optional] 
**imposta** | **float** |  | [optional] 
**detraibile** | **float** |  | [optional] 
**indetraibile** | **float** |  | [optional] 
**totale** | **float** |  | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.castelletto_iva import CastellettoIva

# TODO update the JSON string below
json = "{}"
# create an instance of CastellettoIva from a JSON string
castelletto_iva_instance = CastellettoIva.from_json(json)
# print the JSON string representation of the object
print(CastellettoIva.to_json())

# convert the object into a dict
castelletto_iva_dict = castelletto_iva_instance.to_dict()
# create an instance of CastellettoIva from a dict
castelletto_iva_from_dict = CastellettoIva.from_dict(castelletto_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


