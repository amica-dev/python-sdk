# DocumentoComputeResult

Restituito dal metodo M:Amica.DocumentoService.Compute(Amica.DocumentoComputeData,Amica.RequestSettings,System.Boolean) di `DocumentoService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totale_merce** | **float** | Importo della merce. | [optional] 
**totale_merce_scontata** | **float** | Importo della merce scontata. | [optional] 
**totale_imponibile** | **float** | Totale imponibile, considerando tutte le causali IVA coinvolte. | [optional] 
**totale_spese_esenti** | **float** | Totale delle spese esenti da IVA. | [optional] 
**totale_spese_non_esenti** | **float** | Totale delle spese non esenti da IVA. | [optional] 
**totale_spese** | **float** | Totale delle spese esenti e non esenti. | [optional] 
**totale_ritenuta** | **float** | Importo della ritenuta di acconto. | [optional] 
**totale_cassa_previdenziale** | **float** | Importo della cassa previdenziale. | [optional] 
**enasarco_importo** | **float** | Importo Enasarco. | [optional] 
**totale_esente** | **float** | Importi esenti da IVA. | [optional] 
**totale_imposta** | **float** | Imposta IVA. | [optional] 
**totale_split_payment** | **float** | Importo dello split payment. | [optional] 
**totale_abbuoni** | **float** | Importo degli abbuoni. | [optional] 
**totale_documento** | **float** | Importo totale del documento. | [optional] 
**bonus_fiscale_importo** | **float** | Importo del bonus fiscale. | [optional] 
**netto_a_pagare** | **float** | Netto a pagare. | [optional] 
**riepiloghi_iva** | [**List[DocumentoComputeResultRiepilogoIva]**](DocumentoComputeResultRiepilogoIva.md) | Riepiloghi IVA. | [optional] 

## Example

```python
from amica_sdk.models.documento_compute_result import DocumentoComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeResult from a JSON string
documento_compute_result_instance = DocumentoComputeResult.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeResult.to_json())

# convert the object into a dict
documento_compute_result_dict = documento_compute_result_instance.to_dict()
# create an instance of DocumentoComputeResult from a dict
documento_compute_result_from_dict = DocumentoComputeResult.from_dict(documento_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


