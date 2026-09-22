# RisorsaFinanziaria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**indirizzo** | **str** |  | [optional] 
**localit** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**telefono1** | **str** |  | [optional] 
**telefono2** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**contatto1_nome** | **str** |  | [optional] 
**contatto1_incarico** | **str** |  | [optional] 
**contatto1_telefono1** | **str** |  | [optional] 
**contatto1_telefono2** | **str** |  | [optional] 
**contatto1_e_mail** | **str** |  | [optional] 
**contatto2_nome** | **str** |  | [optional] 
**contatto2_incarico** | **str** |  | [optional] 
**contatto2_telefono1** | **str** |  | [optional] 
**contatto2_telefono2** | **str** |  | [optional] 
**contatto2_e_mail** | **str** |  | [optional] 
**codice_abi** | **str** |  | [optional] 
**codice_cab** | **str** |  | [optional] 
**conto_corrente** | **str** |  | [optional] 
**codice_cin** | **str** |  | [optional] 
**codice_cin_eur** | **str** |  | [optional] 
**codice_cin_paese** | **str** |  | [optional] 
**codice_swift** | **str** |  | [optional] 
**codice_iban** | **str** |  | [optional] 
**web** | **str** |  | [optional] 
**tipologia** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.risorsa_finanziaria import RisorsaFinanziaria

# TODO update the JSON string below
json = "{}"
# create an instance of RisorsaFinanziaria from a JSON string
risorsa_finanziaria_instance = RisorsaFinanziaria.from_json(json)
# print the JSON string representation of the object
print(RisorsaFinanziaria.to_json())

# convert the object into a dict
risorsa_finanziaria_dict = risorsa_finanziaria_instance.to_dict()
# create an instance of RisorsaFinanziaria from a dict
risorsa_finanziaria_from_dict = RisorsaFinanziaria.from_dict(risorsa_finanziaria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


