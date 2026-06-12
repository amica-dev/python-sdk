# BeneServizioComputeData

Utilizzato dal metodo di calcolo M:Amica.BeneServizioService.Compute(Amica.BeneServizioComputeData,Amica.RequestSettings) di `BeneServizioService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iva_esclusa** | **bool** | Indica se il calcolo debba essere effettuato a partire da Amica.BeneServizioComputeData.Prezzo o da Amica.BeneServizioComputeData.PrezzoIvato. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di Amica.CausaleIva. | [optional] 
**listino_id** | **int** | Identificativo univoco di Amica.Listino. | [optional] 
**quantit** | **float** | Quantità. | [optional] 
**prezzo** | **float** | Prezzo IVA esclusa. | [optional] 
**prezzo_ivato** | **float** | Prezzo IVA inclusa. | [optional] 
**sconto1** | **float** | Primo sconto percentuale, applicato al prezzo del bene o servizio. | [optional] 
**sconto2** | **float** | Secondo sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizioComputeData.Sconto1 | [optional] 
**sconto3** | **float** | Terzo sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizioComputeData.Sconto2 | [optional] 
**sconto4** | **float** | Quarto sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizioComputeData.Sconto3 | [optional] 
**sconto_incondizionato** | **float** | Sconto incondizionato, in valuta, applicato al prezzo del bene o servizio. | [optional] 

## Example

```python
from amica_python_sdk.models.bene_servizio_compute_data import BeneServizioComputeData

# TODO update the JSON string below
json = "{}"
# create an instance of BeneServizioComputeData from a JSON string
bene_servizio_compute_data_instance = BeneServizioComputeData.from_json(json)
# print the JSON string representation of the object
print(BeneServizioComputeData.to_json())

# convert the object into a dict
bene_servizio_compute_data_dict = bene_servizio_compute_data_instance.to_dict()
# create an instance of BeneServizioComputeData from a dict
bene_servizio_compute_data_from_dict = BeneServizioComputeData.from_dict(bene_servizio_compute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


