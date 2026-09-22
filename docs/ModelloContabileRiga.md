# ModelloContabileRiga


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**modello_contabile_id** | **int** |  | [optional] 
**causale_contabile_id** | **int** |  | [optional] 
**conto_raw** | **str** |  | 
**importo** | **float** |  | [optional] 
**tipo_importo** | **str** |  | [optional] 
**segno_contabile** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.modello_contabile_riga import ModelloContabileRiga

# TODO update the JSON string below
json = "{}"
# create an instance of ModelloContabileRiga from a JSON string
modello_contabile_riga_instance = ModelloContabileRiga.from_json(json)
# print the JSON string representation of the object
print(ModelloContabileRiga.to_json())

# convert the object into a dict
modello_contabile_riga_dict = modello_contabile_riga_instance.to_dict()
# create an instance of ModelloContabileRiga from a dict
modello_contabile_riga_from_dict = ModelloContabileRiga.from_dict(modello_contabile_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


