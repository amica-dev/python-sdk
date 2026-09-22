# DocumentoComputeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totale_merce** | **float** |  | [optional] 
**totale_merce_scontata** | **float** |  | [optional] 
**totale_imponibile** | **float** |  | [optional] 
**totale_spese_esenti** | **float** |  | [optional] 
**totale_spese_non_esenti** | **float** |  | [optional] 
**totale_spese** | **float** |  | [optional] 
**totale_ritenuta** | **float** |  | [optional] 
**totale_cassa_previdenziale** | **float** |  | [optional] 
**enasarco_importo** | **float** |  | [optional] 
**totale_esente** | **float** |  | [optional] 
**totale_imposta** | **float** |  | [optional] 
**totale_split_payment** | **float** |  | [optional] 
**totale_abbuoni** | **float** |  | [optional] 
**totale_documento** | **float** |  | [optional] 
**bonus_fiscale_importo** | **float** |  | [optional] 
**netto_a_pagare** | **float** |  | [optional] 
**riepiloghi_iva** | [**List[DocumentoComputeResultRiepilogoIva]**](DocumentoComputeResultRiepilogoIva.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_result import DocumentoComputeResult

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


