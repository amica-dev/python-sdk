# DatiTrasporto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colli** | **int** |  | [optional] 
**peso** | **float** |  | [optional] 
**peso_unit_misura** | **str** |  | [optional] 
**data_trasporto** | **datetime** |  | [optional] 
**porto** | **str** |  | [optional] 
**mezzo_di_trasporto** | **str** |  | [optional] 
**aspetto_beni** | **str** |  | [optional] 
**autista_nome** | **str** |  | [optional] 
**autista_targa** | **str** |  | [optional] 
**autista_patente** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.dati_trasporto import DatiTrasporto

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasporto from a JSON string
dati_trasporto_instance = DatiTrasporto.from_json(json)
# print the JSON string representation of the object
print(DatiTrasporto.to_json())

# convert the object into a dict
dati_trasporto_dict = dati_trasporto_instance.to_dict()
# create an instance of DatiTrasporto from a dict
dati_trasporto_from_dict = DatiTrasporto.from_dict(dati_trasporto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


