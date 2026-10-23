# ListinoComputeData

Utilizzato dal metodo `Compute` di `ListinoService`. Contiene il listino aperto, anche non ancora salvato, con le sue righe attuali, la procedura da eseguire e i suoi parametri. Va valorizzato solo il gruppo di parametri della procedura scelta.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listino** | [**Listino**](Listino.md) |  | [optional] 
**procedura** | **str** | La procedura da eseguire sulle righe del listino. | [optional] 
**aggiungi** | [**ListinoComputeAggiungi**](ListinoComputeAggiungi.md) |  | [optional] 
**duplica** | [**ListinoComputeDuplica**](ListinoComputeDuplica.md) |  | [optional] 
**modifica_prezzi** | [**ListinoComputeModificaPrezzi**](ListinoComputeModificaPrezzi.md) |  | [optional] 
**sconti** | [**ListinoComputeSconti**](ListinoComputeSconti.md) |  | [optional] 
**provvigioni** | [**ListinoComputeProvvigioni**](ListinoComputeProvvigioni.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_data import ListinoComputeData

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeData from a JSON string
listino_compute_data_instance = ListinoComputeData.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeData.to_json())

# convert the object into a dict
listino_compute_data_dict = listino_compute_data_instance.to_dict()
# create an instance of ListinoComputeData from a dict
listino_compute_data_from_dict = ListinoComputeData.from_dict(listino_compute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


