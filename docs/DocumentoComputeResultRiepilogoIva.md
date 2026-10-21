# DocumentoComputeResultRiepilogoIva

Riepilogo IVA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imponibile_lordo** | **float** | Imponibile al lordo di eventuali sconti di fattura. | [optional] 
**imponibile** | **float** | Imponibile. | [optional] 
**imposta** | **float** | Importo dell&#39;imposta. | [optional] 
**aliquota** | **float** | Aliquota IVA (percentuale). Il valore è una frazione: &#x60;0.22&#x60; corrisponde al 22%. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di &#x60;CausaleIva&#x60;. | [optional] 
**causale_iva_codice** | **str** | Codice IVA. | [optional] 
**causale_iva_nome** | **str** | Descrizione, o nome, del codice IVA. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_result_riepilogo_iva import DocumentoComputeResultRiepilogoIva

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeResultRiepilogoIva from a JSON string
documento_compute_result_riepilogo_iva_instance = DocumentoComputeResultRiepilogoIva.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeResultRiepilogoIva.to_json())

# convert the object into a dict
documento_compute_result_riepilogo_iva_dict = documento_compute_result_riepilogo_iva_instance.to_dict()
# create an instance of DocumentoComputeResultRiepilogoIva from a dict
documento_compute_result_riepilogo_iva_from_dict = DocumentoComputeResultRiepilogoIva.from_dict(documento_compute_result_riepilogo_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


