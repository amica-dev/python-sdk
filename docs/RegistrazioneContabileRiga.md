# RegistrazioneContabileRiga

Riga di registrazione contabile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**registrazione_contabile_id** | **int** | Identificativo univoco di Amica.RegistrazioneContabile. | [optional] 
**scadenza_id** | **int** | Identificativo univoco di Amica.Scadenza. | [optional] 
**causale_contabile_id** | **int** | Identificativo univoco di &#x60;CausaleContabile&#x60;. | [optional] 
**emissione_id** | **int** | Identificativo del Amica.Documento di riferimento. | [optional] 
**tipo_conto** | **str** | Tipo di conto (piano dei conti). | [optional] 
**sezione_conto** | **str** | Sezione del piano dei conti. | [optional] 
**partita_anno** | **int** | Anno della partita aperta. | [optional] 
**partita_numero** | **int** | Numero della partita aperta. | [optional] 
**conto** | **str** | Numero di conto (ad es. \&quot;100.20\&quot;). | [optional] 
**conto_raw** | **str** | Numero di conto, in formato grezzo (ad es. \&quot;  100   20\&quot;). | [optional] 
**descrizione_conto** | **str** | Descrizione. | [optional] 
**dare** | **float** | Importo in dare. | [optional] 
**avere** | **float** | Importo in avere. | [optional] 
**note** | **str** | Note. | [optional] 

## Example

```python
from amica_sdk.models.registrazione_contabile_riga import RegistrazioneContabileRiga

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrazioneContabileRiga from a JSON string
registrazione_contabile_riga_instance = RegistrazioneContabileRiga.from_json(json)
# print the JSON string representation of the object
print(RegistrazioneContabileRiga.to_json())

# convert the object into a dict
registrazione_contabile_riga_dict = registrazione_contabile_riga_instance.to_dict()
# create an instance of RegistrazioneContabileRiga from a dict
registrazione_contabile_riga_from_dict = RegistrazioneContabileRiga.from_dict(registrazione_contabile_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


