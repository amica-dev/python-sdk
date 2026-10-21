# DocumentoComputeData

Utilizzato dal metodo `Compute` di `DocumentoService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iva_esclusa** | **bool** | Indica se i prezzi del documento sono IVA esclusa. Con IVA inclusa l&#39;imposta di ogni riepilogo si ricava dall&#39;importo ivato delle righe (&#x60;ImportoIvato&#x60;), come nel client Windows. Se non indicato vale &#x60;true&#x60;. | [optional] 
**righe** | [**List[DocumentoComputeDataBeneServizio]**](DocumentoComputeDataBeneServizio.md) | Metadati delle righe del documento. | [optional] 
**spese_documento** | [**List[DocumentoComputeDataSpesa]**](DocumentoComputeDataSpesa.md) | Metadati dell&#39;elenco delle spese. | [optional] 
**sconto_percentuale** | **float** | Sconto, in percentuale, da calcolare sull&#39;intero importo del documento. Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto_pagamento_percentuale** | **float** | Sconto riconosciuto in base alla modalità di pagamento utilizzata (es.: +5% in caso di rimessa diretta). Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto_incondizionato_importo** | **float** | Sconto, in valuta, da applicare all&#39;intero importo del documento. | [optional] 
**cassa_previdenziale_percentuale** | **float** | Contributo cassa previdenziale (percentuale) da applicare al documento. Il valore è una frazione: &#x60;0.04&#x60; corrisponde al 4%. | [optional] 
**cassa_previdenziale_causale_iva_id** | **int** | Identificativo univoco della causale IVA della cassa previdenziale. | [optional] 
**ritenuta_include_cassa_previdenziale** | **bool** | Indica se la ritenuta debba essere applicata all&#39;importo della cassa previdenziale riportato nel documento. | [optional] 
**quota_ritenuta_su_imponibile** | **float** | Quota dell&#39;imponibile su cui applicare la ritenuta. Il valore è una frazione: &#x60;1.00&#x60; corrisponde al 100%. | [optional] 
**ritenuta_percentuale** | **float** | Quota di ritenuta da applicare al documento. Il valore è una frazione: &#x60;0.20&#x60; corrisponde al 20%. | [optional] 
**enasarco_importo** | **float** | Importo Enasarco. | [optional] 
**abbuono_importo** | **float** | Importo dell&#39;abbuono. | [optional] 
**bonus_fiscale_percentuale** | **float** | Importo del bonus fiscale. Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_data import DocumentoComputeData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeData from a JSON string
documento_compute_data_instance = DocumentoComputeData.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeData.to_json())

# convert the object into a dict
documento_compute_data_dict = documento_compute_data_instance.to_dict()
# create an instance of DocumentoComputeData from a dict
documento_compute_data_from_dict = DocumentoComputeData.from_dict(documento_compute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


