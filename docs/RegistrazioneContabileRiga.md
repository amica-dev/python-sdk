# RegistrazioneContabileRiga


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**registrazione_contabile_id** | **int** |  | [optional] 
**scadenza_id** | **int** |  | [optional] 
**causale_contabile_id** | **int** |  | [optional] 
**emissione_id** | **int** |  | [optional] 
**tipo_conto** | **str** |  | [optional] 
**sezione_conto** | **str** |  | [optional] 
**partita_anno** | **int** |  | [optional] 
**partita_numero** | **int** |  | [optional] 
**conto** | **str** |  | [optional] 
**conto_raw** | **str** |  | [optional] 
**descrizione_conto** | **str** |  | [optional] 
**dare** | **float** |  | [optional] 
**avere** | **float** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.registrazione_contabile_riga import RegistrazioneContabileRiga

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrazioneContabileRiga from a JSON string
registrazione_contabile_riga_instance = RegistrazioneContabileRiga.from_json(json)
# print the JSON string representation of the object
print(RegistrazioneContabileRiga.to_json())

# convert the object into a dict
registrazione_contabile_riga_dict = registrazione_contabile_riga_instance.to_dict()
# create an instance of RegistrazioneContabileRiga from a dict
registrazione_contabile_riga_from_dict = RegistrazioneContabileRiga.from_dict(registrazione_contabile_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


