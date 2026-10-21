# BeneServizioComputeData

Utilizzato dal metodo di calcolo `Compute` di `BeneServizioService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iva_esclusa** | **bool** | Indica se il calcolo debba essere effettuato a partire da &#x60;Prezzo&#x60; o da &#x60;PrezzoIvato&#x60;. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di &#x60;CausaleIva&#x60;. | [optional] 
**listino_id** | **int** | Identificativo univoco di &#x60;Listino&#x60;. | [optional] 
**quantit** | **float** | Quantità. | [optional] 
**prezzo** | **float** | Prezzo IVA esclusa. | [optional] 
**prezzo_ivato** | **float** | Prezzo IVA inclusa. | [optional] 
**sconto1** | **float** | Primo sconto percentuale, applicato al prezzo del bene o servizio. Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto2** | **float** | Secondo sconto percentuale, applicato dopo l&#39;applicazione di &#x60;Sconto1&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto3** | **float** | Terzo sconto percentuale, applicato dopo l&#39;applicazione di &#x60;Sconto2&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto4** | **float** | Quarto sconto percentuale, applicato dopo l&#39;applicazione di &#x60;Sconto3&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
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


