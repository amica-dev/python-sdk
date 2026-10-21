# DocumentoComputeDataBeneServizio

Metadati della riga di documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ritenuta_fiscale** | **bool** | Indica se la ritenuta fiscale è applicabile o meno. | [optional] 
**importo** | **float** | Importo. | [optional] 
**importo_ivato** | **float** | Importo IVA inclusa della riga, come restituito da &#x60;beneservizio/compute&#x60;. Serve con IVA inclusa (&#x60;IvaEsclusa&#x60; a &#x60;false&#x60;): l&#39;imposta del riepilogo è la differenza fra ivato e imponibile. Se non indicato si ricava da importo e aliquota. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco del codice IVA. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_data_bene_servizio import DocumentoComputeDataBeneServizio

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeDataBeneServizio from a JSON string
documento_compute_data_bene_servizio_instance = DocumentoComputeDataBeneServizio.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeDataBeneServizio.to_json())

# convert the object into a dict
documento_compute_data_bene_servizio_dict = documento_compute_data_bene_servizio_instance.to_dict()
# create an instance of DocumentoComputeDataBeneServizio from a dict
documento_compute_data_bene_servizio_from_dict = DocumentoComputeDataBeneServizio.from_dict(documento_compute_data_bene_servizio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


