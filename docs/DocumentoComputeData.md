# DocumentoComputeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**righe** | [**List[DocumentoComputeDataBeneServizio]**](DocumentoComputeDataBeneServizio.md) |  | [optional] 
**spese_documento** | [**List[DocumentoComputeDataSpesa]**](DocumentoComputeDataSpesa.md) |  | [optional] 
**sconto_percentuale** | **float** |  | [optional] 
**sconto_pagamento_percentuale** | **float** |  | [optional] 
**sconto_incondizionato_importo** | **float** |  | [optional] 
**cassa_previdenziale_percentuale** | **float** |  | [optional] 
**cassa_previdenziale_causale_iva_id** | **int** |  | [optional] 
**ritenuta_include_cassa_previdenziale** | **bool** |  | [optional] 
**quota_ritenuta_su_imponibile** | **float** |  | [optional] 
**ritenuta_percentuale** | **float** |  | [optional] 
**enasarco_importo** | **float** |  | [optional] 
**abbuono_importo** | **float** |  | [optional] 
**bonus_fiscale_percentuale** | **float** |  | [optional] 

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


