# FatturaElettronicaXmlTemplate

Modello standard di fattura elettronica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**soggetto_emittente** | **str** |  | [optional] 
**id_trasmittente_id_paese** | **str** |  | [optional] 
**cedente_prestatore_id_paese** | **str** |  | [optional] 
**progressivo_invio** | **str** |  | [optional] 
**albo_professionale** | **str** |  | [optional] 
**provincia_albo** | **str** |  | [optional] 
**numero_iscrizione_albo** | **str** |  | [optional] 
**data_iscrizione_albo** | **datetime** |  | [optional] 
**regime_fiscale** | **str** |  | [optional] 
**sede_nazione** | **str** |  | [optional] 
**sede_numero_civico** | **str** |  | [optional] 
**stabile_organizzazione_indirizzo** | **str** |  | [optional] 
**stabile_organizzazione_numero_civico** | **str** |  | [optional] 
**stabile_organizzazione_cap** | **str** |  | [optional] 
**stabile_organizzazione_comune** | **str** |  | [optional] 
**stabile_organizzazione_provincia** | **str** |  | [optional] 
**stabile_organizzazione_nazione** | **str** |  | [optional] 
**rea_numero** | **str** |  | [optional] 
**rea_ufficio** | **str** |  | [optional] 
**rea_capitale_sociale** | **float** |  | [optional] 
**rea_socio_unico** | **str** |  | [optional] 
**rea_stato_liquidazione** | **str** |  | [optional] 
**rappresentante_id_paese** | **str** |  | [optional] 
**rappresentante_id_codice** | **str** |  | [optional] 
**rappresentante_codice_fiscale** | **str** |  | [optional] 
**rappresentante_denominazione** | **str** |  | [optional] 
**rappresentante_nome** | **str** |  | [optional] 
**rappresentante_cognome** | **str** |  | [optional] 
**rappresentante_titolo** | **str** |  | [optional] 
**rappresentante_cod_eori** | **str** |  | [optional] 
**intermediario_id_paese** | **str** |  | [optional] 
**intermediario_id_codice** | **str** |  | [optional] 
**intermediario_codice_fiscale** | **str** |  | [optional] 
**intermediario_denominazione** | **str** |  | [optional] 
**intermediario_nome** | **str** |  | [optional] 
**intermediario_cognome** | **str** |  | [optional] 
**intermediario_titolo** | **str** |  | [optional] 
**intermediario_cod_eori** | **str** |  | [optional] 

## Example

```python
from amica_sdk.models.fattura_elettronica_xml_template import FatturaElettronicaXmlTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaXmlTemplate from a JSON string
fattura_elettronica_xml_template_instance = FatturaElettronicaXmlTemplate.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaXmlTemplate.to_json())

# convert the object into a dict
fattura_elettronica_xml_template_dict = fattura_elettronica_xml_template_instance.to_dict()
# create an instance of FatturaElettronicaXmlTemplate from a dict
fattura_elettronica_xml_template_from_dict = FatturaElettronicaXmlTemplate.from_dict(fattura_elettronica_xml_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


