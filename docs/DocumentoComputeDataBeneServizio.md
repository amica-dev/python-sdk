# DocumentoComputeDataBeneServizio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ritenuta_fiscale** | **bool** |  | [optional] 
**importo** | **float** |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 

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


