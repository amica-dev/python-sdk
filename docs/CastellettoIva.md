# CastellettoIva

Importo IVA a debito associato a una Amica.CastellettoIva.RegistrazioneContabile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**registrazione_contabile_id** | **int** | Identificativo univoco di Amica.CastellettoIva.RegistrazioneContabile (registrazione contabile). | [optional] 
**registrazione_contabile** | [**RegistrazioneContabile**](RegistrazioneContabile.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di Amica.CastellettoIva.CausaleIva. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**registro_iva_id** | **int** | Identificativo univoco di &#x60;RegistroIva&#x60;. | [optional] 
**imponibile** | **float** | Imponibile. | [optional] 
**imposta** | **float** | Imposta. | [optional] 
**detraibile** | **float** | Quota detraibile. | [optional] 
**indetraibile** | **float** | Quota non detraibile. | [optional] 
**totale** | **float** | Importo totale (imponibile + imposta). | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.castelletto_iva import CastellettoIva

# TODO update the JSON string below
json = "{}"
# create an instance of CastellettoIva from a JSON string
castelletto_iva_instance = CastellettoIva.from_json(json)
# print the JSON string representation of the object
print(CastellettoIva.to_json())

# convert the object into a dict
castelletto_iva_dict = castelletto_iva_instance.to_dict()
# create an instance of CastellettoIva from a dict
castelletto_iva_from_dict = CastellettoIva.from_dict(castelletto_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


