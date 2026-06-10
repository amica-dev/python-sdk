# Scadenza

Scadenza di pagamento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**registrazione_contabile_id** | **int** | Identificativo univoco di Amica.Scadenza.RegistrazioneContabile. | [optional] 
**registrazione_contabile** | [**RegistrazioneContabile**](RegistrazioneContabile.md) |  | [optional] 
**anagrafica_id** | **int** | Identificativo univoco di Amica.Scadenza.Anagrafica. | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**documento_id** | **int** | Identificativo univoco di Amica.Scadenza.Documento. | [optional] 
**documento** | [**Documento**](Documento.md) |  | [optional] 
**modalita_pagamento_id** | **int** | Identificativo univoco di Amica.Scadenza.ModalitaPagamento. | [optional] 
**modalita_pagamento** | [**ModalitaPagamento**](ModalitaPagamento.md) |  | [optional] 
**pagata_manualmente** | **bool** | Indica se la scadenza è stata impostata manualmente come &#39;pagata&#39;. | [optional] 
**pagata** | **bool** | Indica se la scadenza è pagata. | [optional] [readonly] 
**data** | **datetime** | Data di scadenza. | [optional] 
**data_pagamento** | **datetime** | Data di pagamento. | [optional] 
**data_documento** | **datetime** | Data del documento fiscale. | [optional] 
**importo** | **float** | Importo della scadenza. | [optional] 
**partita_anno** | **int** | Anno della partita aperta. | [optional] 
**partita_numero** | **int** | Numero della partita aperta. | [optional] 
**note** | **str** | Note. | [optional] 
**descrizione** | **str** | Descrizione. | [optional] 
**documento_numero_parte_numerica** | **int** | Numero documento, la parte numerica (es. 99). | [optional] 
**documento_numero_parte_testo** | **str** | Numero documento, la parte alfanumerica (es. \&quot;bis\&quot;) | [optional] 
**documento_numero** | **str** | Numero documento, es. \&quot;99/bis\&quot;. Il documento deve essere già salvato sul sistema. | [optional] 
**tipo_scadenza** | **str** | Tipo di scadenza. | [optional] 
**importo_pagato** | **float** | L&#39;importo già pagato della scadenza. | [optional] 
**importo_da_pagare** | **float** | Rimanenza che risulta ancora da pagare. | [optional] [readonly] 

## Example

```python
from amica_sdk.models.scadenza import Scadenza

# TODO update the JSON string below
json = "{}"
# create an instance of Scadenza from a JSON string
scadenza_instance = Scadenza.from_json(json)
# print the JSON string representation of the object
print(Scadenza.to_json())

# convert the object into a dict
scadenza_dict = scadenza_instance.to_dict()
# create an instance of Scadenza from a dict
scadenza_from_dict = Scadenza.from_dict(scadenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


