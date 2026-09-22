# RegistrazioneContabile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**data** | **datetime** |  | [optional] 
**data_competenza** | **datetime** |  | [optional] 
**numero** | **int** |  | [optional] 
**tipo_registrazione** | **str** |  | [optional] 
**segno_iva** | **str** |  | [optional] 
**tipo_operazione** | **str** |  | [optional] 
**registro_iva_id** | **int** |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**pagamento_id** | **int** |  | [optional] 
**documento_id** | **int** |  | [optional] 
**documento** | [**Documento**](Documento.md) |  | [optional] 
**data_documento** | **datetime** |  | [optional] 
**documento_numero_parte_testo** | **str** |  | [optional] 
**documento_numero_parte_numerica** | **int** |  | [optional] 
**documento_numero** | **str** |  | [optional] 
**protocollo** | **int** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**righe** | [**List[RegistrazioneContabileRiga]**](RegistrazioneContabileRiga.md) |  | [optional] 
**castelletto_iva** | [**List[CastellettoIva]**](CastellettoIva.md) |  | [optional] 
**scadenze** | [**List[Scadenza]**](Scadenza.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.registrazione_contabile import RegistrazioneContabile

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrazioneContabile from a JSON string
registrazione_contabile_instance = RegistrazioneContabile.from_json(json)
# print the JSON string representation of the object
print(RegistrazioneContabile.to_json())

# convert the object into a dict
registrazione_contabile_dict = registrazione_contabile_instance.to_dict()
# create an instance of RegistrazioneContabile from a dict
registrazione_contabile_from_dict = RegistrazioneContabile.from_dict(registrazione_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


