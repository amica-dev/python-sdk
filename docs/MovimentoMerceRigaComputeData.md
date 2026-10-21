# MovimentoMerceRigaComputeData

Utilizzato dal metodo di calcolo `ComputeRiga` di `MovimentoMerceService`. Contiene la riga da completare, i dati della testata del movimento che servono al calcolo e il campo della riga appena modificato. Il movimento può non essere ancora salvato.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**riga** | [**MovimentoMerceRiga**](MovimentoMerceRiga.md) |  | [optional] 
**modificato** | **str** | Il campo della riga appena modificato, che decide cosa ricalcolare. Se non indicato si ricava il prezzo non modificabile da quello modificabile, come per &#x60;CausaleIva&#x60;. | [optional] 
**iva_esclusa** | **bool** | &#x60;IvaEsclusa&#x60; della testata. Con IVA esclusa si scrive il prezzo netto e si             ricava quello ivato, con IVA inclusa il contrario. | [optional] 
**anagrafica_id** | **int** | &#x60;AnagraficaId&#x60; della testata, se già scelta. Alla scelta dell&#39;articolo ne             determina listino e causale IVA. | [optional] 
**causale_magazzino_id** | **int** | &#x60;CausaleMagazzinoId&#x60; della testata, se già scelta. Dice se il movimento è un             carico, e quindi se il listino dell&#39;anagrafica è quello del fornitore o del cliente. | [optional] 

## Example

```python
from amica_python_sdk.models.movimento_merce_riga_compute_data import MovimentoMerceRigaComputeData

# TODO update the JSON string below
json = "{}"
# create an instance of MovimentoMerceRigaComputeData from a JSON string
movimento_merce_riga_compute_data_instance = MovimentoMerceRigaComputeData.from_json(json)
# print the JSON string representation of the object
print(MovimentoMerceRigaComputeData.to_json())

# convert the object into a dict
movimento_merce_riga_compute_data_dict = movimento_merce_riga_compute_data_instance.to_dict()
# create an instance of MovimentoMerceRigaComputeData from a dict
movimento_merce_riga_compute_data_from_dict = MovimentoMerceRigaComputeData.from_dict(movimento_merce_riga_compute_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


