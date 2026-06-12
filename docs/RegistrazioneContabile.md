# RegistrazioneContabile

Registrazione contabile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**data** | **datetime** | Data della registrazione contabile. | [optional] 
**data_competenza** | **datetime** | Data di competenza. | [optional] 
**numero** | **int** | Numero della registrazione contabile. | [optional] 
**tipo_registrazione** | **str** | Tipo di registrazione. | [optional] 
**segno_iva** | **str** | Positività o negatività dell&#39;IVA. | [optional] 
**tipo_operazione** | **str** | Tipo di operazione contabile. | [optional] 
**registro_iva_id** | **int** | Identificativo univoco di &#x60;RegistroIva&#x60;. | [optional] 
**anagrafica_id** | **int** | Identificativo univoco di Amica.Anagrafica. | [optional] 
**pagamento_id** | **int** | Identificativo univoco di Amica.Pagamento. | [optional] 
**documento_id** | **int** | Identificativo univoco di Amica.RegistrazioneContabile.Documento. | [optional] 
**documento** | [**Documento**](Documento.md) |  | [optional] 
**data_documento** | **datetime** | Data del documento di riferimento. | [optional] 
**documento_numero_parte_testo** | **str** | La parte alfanumerica del numero documento, se presente (es. \&quot;bis\&quot;). | [optional] 
**documento_numero_parte_numerica** | **int** | La parte numerica del numero documento (es. \&quot;99\&quot;). | [optional] 
**documento_numero** | **str** | Numero documento completo, es. \&quot;99/bis\&quot;. Il documento deve essere già stato salvato sul backend. | [optional] 
**protocollo** | **int** | Numero di protocollo. | [optional] 
**descrizione** | **str** | Descrizione. | [optional] 
**note** | **str** | Note. | [optional] 
**righe** | [**List[RegistrazioneContabileRiga]**](RegistrazioneContabileRiga.md) | Righe della registrazione contabile. | [optional] 
**castelletto_iva** | [**List[CastellettoIva]**](CastellettoIva.md) | Importo IVA da versare. | [optional] 
**scadenze** | [**List[Scadenza]**](Scadenza.md) | Scadenze. | [optional] 

## Example

```python
from amica_python_sdk.models.registrazione_contabile import RegistrazioneContabile

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrazioneContabile from a JSON string
registrazione_contabile_instance = RegistrazioneContabile.from_json(json)
# print the JSON string representation of the object
print(RegistrazioneContabile.to_json())

# convert the object into a dict
registrazione_contabile_dict = registrazione_contabile_instance.to_dict()
# create an instance of RegistrazioneContabile from a dict
registrazione_contabile_from_dict = RegistrazioneContabile.from_dict(registrazione_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


