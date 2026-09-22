# Preferenze


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**ragione_sociale1** | **str** |  | [optional] 
**ragione_sociale2** | **str** |  | [optional] 
**partita_iva** | **str** |  | [optional] 
**registro_imprese** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**codice_sia** | **str** |  | [optional] 
**codice_rea** | **str** |  | [optional] 
**persona_giuridica** | **bool** |  | [optional] 
**data_nascita** | **datetime** |  | [optional] 
**localita_nascita** | **str** |  | [optional] 
**provincia_nascita** | **str** |  | [optional] 
**sesso** | **str** |  | [optional] 
**attivita** | **str** |  | [optional] 
**iva_esclusa** | **bool** |  | [optional] 
**decimali_prezzo_unitario** | **int** |  | [optional] 
**causale_produzione_componenti_id** | **int** |  | [optional] 
**causale_produzione_composti_id** | **int** |  | [optional] 
**causale_magazzino_vendita_id** | **int** |  | [optional] 
**causale_magazzino_acquisto_id** | **int** |  | [optional] 
**ricerca_articolo** | [**RicercaArticolo**](RicercaArticolo.md) |  | [optional] 
**data_speciale1** | **str** |  | [optional] 
**data_speciale2** | **str** |  | [optional] 
**giorni_extra_data_speciale1** | **int** |  | [optional] 
**giorni_extra_data_speciale2** | **int** |  | [optional] 
**pagato_manuale** | **bool** |  | [optional] 
**causale_magazzino_merci_id** | **int** |  | [optional] 
**magazzino_merci_id** | **int** |  | [optional] 
**listino_merci_id** | **int** |  | [optional] 
**modalita_pagamento_merci_id** | **int** |  | [optional] 
**documenti_causale_iva_id** | **int** |  | [optional] 
**documenti_magazzino_id** | **int** |  | [optional] 
**documenti_listino_id** | **int** |  | [optional] 
**e_mail** | **str** |  | [optional] 
**sito_web** | **str** |  | [optional] 
**anno_contabile** | **int** |  | [optional] 
**unit_di_misura** | **str** |  | [optional] 
**causale_pagamento_modello_cu** | **str** |  | [optional] 
**impostazioni_sdi** | [**ImpostazioniSdi**](ImpostazioniSdi.md) |  | [optional] 
**tipo_bilancio** | **str** |  | [optional] 
**periodo_iva** | **str** |  | [optional] 
**liquidazione_iva** | **str** |  | [optional] 
**modifica_registrazione_contabile_alla_emissione** | **bool** |  | [optional] 
**ottimizza_emissione_ordini** | **bool** |  | [optional] 
**aggiungi_anno_in_corso_al_numero_documento** | **bool** |  | [optional] 
**consenti_cambio_manuale_stato_ddt** | **bool** |  | [optional] 
**email_body** | **str** |  | [optional] 
**email_auto_send** | **bool** |  | [optional] 
**auto_produzione** | **bool** |  | [optional] 
**codice_destinatario** | **str** |  | [optional] 
**pec** | **str** |  | [optional] 
**modello_vendite_nota_debito_id** | **int** |  | [optional] 
**modello_vendite_nota_credito_id** | **int** |  | [optional] 
**modello_vendite_ricevuta_fiscale_id** | **int** |  | [optional] 
**modello_vendite_fattura_professionista_id** | **int** |  | [optional] 
**modello_vendite_fattura_differita_id** | **int** |  | [optional] 
**modello_vendite_fattura_acconto_id** | **int** |  | [optional] 
**modello_acquisti_fattura_accompagnatoria_id** | **int** |  | [optional] 
**modello_vendite_fattura_accompagnaoria_id** | **int** |  | [optional] 
**modello_acquisti_nota_debito_id** | **int** |  | [optional] 
**modello_acquisti_nota_credito_id** | **int** |  | [optional] 
**modello_acquisti_fattura_professionisti_id** | **int** |  | [optional] 
**modello_acquisti_fattura_differita_id** | **int** |  | [optional] 
**modello_acquisti_fattura_acconto_id** | **int** |  | [optional] 
**sede_legale** | [**SedeLegale**](SedeLegale.md) |  | [optional] 
**sede_operativa** | [**SedeOperativa**](SedeOperativa.md) |  | [optional] 
**sede_altra** | [**SedeAltra**](SedeAltra.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.preferenze import Preferenze

# TODO update the JSON string below
json = "{}"
# create an instance of Preferenze from a JSON string
preferenze_instance = Preferenze.from_json(json)
# print the JSON string representation of the object
print(Preferenze.to_json())

# convert the object into a dict
preferenze_dict = preferenze_instance.to_dict()
# create an instance of Preferenze from a dict
preferenze_from_dict = Preferenze.from_dict(preferenze_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


