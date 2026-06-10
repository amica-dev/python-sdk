# DocumentoComputeData

Utilizzato dal metodo M:Amica.DocumentoService.Compute(Amica.DocumentoComputeData,Amica.RequestSettings,System.Boolean) di `DocumentoService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**righe** | [**List[DocumentoComputeDataBeneServizio]**](DocumentoComputeDataBeneServizio.md) | Metadati delle righe del documento. | [optional] 
**spese_documento** | [**List[DocumentoComputeDataSpesa]**](DocumentoComputeDataSpesa.md) | Metadati dell&#39;elenco delle spese. | [optional] 
**sconto_percentuale** | **float** | Sconto, in percentuale, da calcolare sull&#39;intero importo del documento. | [optional] 
**sconto_pagamento_percentuale** | **float** | Sconto riconosciuto in base alla modalità di pagamento utilizzata (es.: +5% in caso di rimessa diretta). | [optional] 
**sconto_incondizionato_importo** | **float** | Sconto, in valuta, da applicare all&#39;intero importo del documento. | [optional] 
**cassa_previdenziale_percentuale** | **float** | Contributo cassa previdenziale (percentuale) da applicare al documento. | [optional] 
**cassa_previdenziale_causale_iva_id** | **int** | Identificativo univoco della causale IVA della cassa previdenziale. | [optional] 
**ritenuta_include_cassa_previdenziale** | **bool** | Indica se la ritenuta debba essere applicata all&#39;importo della cassa previdenziale riportato nel documento. | [optional] 
**quota_ritenuta_su_imponibile** | **float** | Quota dell&#39;imponibile su cui applicare la ritenuta. | [optional] 
**ritenuta_percentuale** | **float** | Quota di ritenuta da applicare al documento. | [optional] 
**enasarco_importo** | **float** | Importo Enasarco. | [optional] 
**abbuono_importo** | **float** | Importo dell&#39;abbuono. | [optional] 
**bonus_fiscale_percentuale** | **float** | Importo del bonus fiscale. | [optional] 

## Example

```python
from amica_sdk.models.documento_compute_data import DocumentoComputeData

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


