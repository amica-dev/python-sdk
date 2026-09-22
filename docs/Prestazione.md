# Prestazione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**categoria_merceologica_id** | **int** |  | [optional] 
**categoria_merceologica** | [**CategoriaMerceologica**](CategoriaMerceologica.md) |  | [optional] 
**gruppo_merceologico_id** | **int** |  | [optional] 
**gruppo_merceologico** | [**GruppoMerceologico**](GruppoMerceologico.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**nome** | **str** |  | 
**codice** | **str** |  | 
**bar_code** | **str** |  | [optional] 
**stato** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.prestazione import Prestazione

# TODO update the JSON string below
json = "{}"
# create an instance of Prestazione from a JSON string
prestazione_instance = Prestazione.from_json(json)
# print the JSON string representation of the object
print(Prestazione.to_json())

# convert the object into a dict
prestazione_dict = prestazione_instance.to_dict()
# create an instance of Prestazione from a dict
prestazione_from_dict = Prestazione.from_dict(prestazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


