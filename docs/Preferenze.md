# Preferenze

Preferenze aziendali.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**ragione_sociale1** | **str** | Ragione sociale. | [optional] 
**ragione_sociale2** | **str** | Eventuale seconda riga della ragione sociale. Utile soprattutto in fase di stampa, quando si desidera spezzare una ragione sociale molto lunga su due righe distinte. | [optional] 
**partita_iva** | **str** | Partita IVA. | [optional] 
**registro_imprese** | **str** | Numero di iscrizione al Registro Imprese. | [optional] 
**codice_fiscale** | **str** | Codice fiscale. | [optional] 
**codice_sia** | **str** | Codice SIA. | [optional] 
**codice_rea** | **str** | Codice REA. | [optional] 
**persona_giuridica** | **bool** | Indica se l&#39;organizzazione è una persona giuridica oppure no. &#x60;true&#x60; indica una persona giuridica, &#x60;false&#x60; indica una persona fisica. | [optional] 
**data_nascita** | **datetime** | Data di nascita (persona fisica). | [optional] 
**localita_nascita** | **str** | Luogo di nascita (persona fisica). | [optional] 
**provincia_nascita** | **str** | Provincia di nascita (persona fisica). | [optional] 
**sesso** | **str** | Sesso (persona fisica). | [optional] 
**attivita** | **str** | Tipo di attività svolta dall&#39;azienda o dalla persona fisica. | [optional] 
**iva_esclusa** | **bool** | Indica se, in modo predefinito, i prezzi riportati sui documenti fiscali devono essere considerati al netto dell&#39;IVA. Se &#x60;false&#x60;, l&#39;IVA viene applicata ai prezzi quando possibile. | [optional] 
**decimali_prezzo_unitario** | **int** | Numero di decimali ammessi nei prezzi unitari. Minimo 1, massimo 5. | [optional] 
**causale_produzione_componenti_id** | **int** | Identificativo univoco di Amica.CausaleMagazzino Identificativo univoco della Amica.CausaleMagazzino da usare nella produzione di componenti. | [optional] 
**causale_produzione_composti_id** | **int** | Identificativo univoco della Amica.CausaleMagazzino da usare per gli articoli composti nella produzione di componenti. | [optional] 
**causale_magazzino_vendita_id** | **int** | Identificativo univoco della Amica.CausaleMagazzino da usare nei documenti di vendita. | [optional] 
**causale_magazzino_acquisto_id** | **int** | Identificativo univoco della Amica.CausaleMagazzino da usare nei documenti di acquisto. | [optional] 
**ricerca_articolo** | [**RicercaArticolo**](RicercaArticolo.md) |  | [optional] 
**data_speciale1** | **str** | Eventuali scadenze che cadono in questa data verranno posticipate del numero di giorni indicato da Amica.Preferenze.GiorniExtraDataSpeciale1. | [optional] 
**data_speciale2** | **str** | Eventuali scadenze che cadono in questa data verranno posticipate del numero di giorni indicato da Amica.Preferenze.GiorniExtraDataSpeciale2. | [optional] 
**giorni_extra_data_speciale1** | **int** | Numero di giorni da aggiungere a Amica.Preferenze.DataSpeciale1. | [optional] 
**giorni_extra_data_speciale2** | **int** | Numero di giorni da aggiungere a Amica.Preferenze.DataSpeciale1. | [optional] 
**pagato_manuale** | **bool** | Indica se il pagamento delle scadenze viene gestito manualmente. Se &#x60;false&#x60;, lo stato del pagamento viene determinato in base alle registrazioni contabili (il modulo &lt;a href&#x3D;\&quot;https://gestionaleamica.com/Software/ContabilitaOrdinaria\&quot;&gt;Contabilità&lt;/a&gt; deve essere attivo). | [optional] 
**causale_magazzino_merci_id** | **int** | Identificativo della Amica.CausaleMagazzino predefinita nei movimenti merci. | [optional] 
**magazzino_merci_id** | **int** | Identificativo del Amica.Magazzino predefinito nei movimenti merci. | [optional] 
**listino_merci_id** | **int** | Identificativo del Amica.Listino predefinito nei movimenti merci. | [optional] 
**modalita_pagamento_merci_id** | **int** | Identificativo della Amica.ModalitaPagamento predefinita nei movimenti merci. | [optional] 
**documenti_causale_iva_id** | **int** | Identificativo della Amica.CausaleIva predefinita nei documenti fiscali. | [optional] 
**documenti_magazzino_id** | **int** | Identificativo del Amica.Magazzino predefinito nei documenti fiscali. | [optional] 
**documenti_listino_id** | **int** | Amica.Preferenze.DocumentiListinoId predefinito nei documenti fiscali. | [optional] 
**e_mail** | **str** | Email aziendale. | [optional] 
**sito_web** | **str** | Sito web aziendale. | [optional] 
**anno_contabile** | **int** | Anno contabile corrente (es. &#39;2023&#39;). | [optional] 
**unit_di_misura** | **str** | Unità di misura predefinita. | [optional] 
**causale_pagamento_modello_cu** | **str** | Causale del modello CU (es. &#39;A&#39;). | [optional] 
**impostazioni_sdi** | [**ImpostazioniSdi**](ImpostazioniSdi.md) |  | [optional] 
**tipo_bilancio** | **str** | Tipo di bilancio predefinito: analitico o sintetico. | [optional] 
**periodo_iva** | **str** | Periodicità IVA: mensile o trimestrale. | [optional] 
**liquidazione_iva** | **str** | Tipo di liquidazione IVA: per competenza o per cassa. | [optional] 
**modifica_registrazione_contabile_alla_emissione** | **bool** | Indica se si desidera modificare la registrazione contabile creata all&#39;emissione di un documento. Si applica ad Amica20 WebApp e ad Amica 20 per Windows. | [optional] 
**ottimizza_emissione_ordini** | **bool** | Indica se l&#39;ottimizzazione per l&#39;emissione di documenti di grandi dimensioni è attiva oppure no. Si applica ad Amica20 per Windows. | [optional] 
**aggiungi_anno_in_corso_al_numero_documento** | **bool** | Indica se si desidera aggiungere l&#39;anno in corso al numero del documento (es. 1/2022). Si applica ad Amica 20 WebApp e ad Amica 20 per Windows. | [optional] 
**consenti_cambio_manuale_stato_ddt** | **bool** | Indica se si desidera abilitare l&#39;opzione di modifica dello stato dei DDT. Si applica ad Amica 20 WebApp e ad Amica 20 per Windows. | [optional] 
**email_body** | **str** | Testo del messaggio email inviato all&#39;emissione di un documento. Il documento stesso viene allegato al messaggio. Si applica ad Amica 20 per Windows. | [optional] 
**email_auto_send** | **bool** | Indica se inviare un&#39;email all&#39;emissione di un documento. | [optional] 
**auto_produzione** | **bool** | Indica se la produzione automatica dei composti è attiva. | [optional] 
**codice_destinatario** | **str** | &#39;Codice destinatario&#39; per il sistema fiscale italiano. Utilizzato per il recapito delle fatture elettroniche italiane. | [optional] 
**pec** | **str** | Indirizzo PEC italiano. | [optional] 
**modello_vendite_nota_debito_id** | **int** | Amica.ModelloContabile predefinito per le note di debito emesse. | [optional] 
**modello_vendite_nota_credito_id** | **int** | Amica.ModelloContabile predefinito per le note di credito emesse. | [optional] 
**modello_vendite_ricevuta_fiscale_id** | **int** | Amica.ModelloContabile predefinito per le ricevute fiscali emesse. | [optional] 
**modello_vendite_fattura_professionista_id** | **int** | Amica.ModelloContabile predefinito per le fatture professionisti emesse. | [optional] 
**modello_vendite_fattura_differita_id** | **int** | Amica.ModelloContabile predefinito per le fatture differite emesse. | [optional] 
**modello_vendite_fattura_acconto_id** | **int** | Amica.ModelloContabile predefinito per le fatture di acconto emesse. | [optional] 
**modello_acquisti_fattura_accompagnatoria_id** | **int** | Amica.ModelloContabile predefinito per le fatture accompagnatorie fornitori emesse. | [optional] 
**modello_vendite_fattura_accompagnaoria_id** | **int** | Amica.ModelloContabile predefinito per le fatture accompagnatorie emesse. | [optional] 
**modello_acquisti_nota_debito_id** | **int** | Amica.ModelloContabile predefinito per le note di debito fornitori emesse. | [optional] 
**modello_acquisti_nota_credito_id** | **int** | Amica.ModelloContabile predefinito per le note di credito emesse. | [optional] 
**modello_acquisti_fattura_professionisti_id** | **int** | Amica.ModelloContabile predefinito per le fatture professionisti fornitori emesse. | [optional] 
**modello_acquisti_fattura_differita_id** | **int** | Amica.ModelloContabile predefinito per le fatture differite fornitori emesse. | [optional] 
**modello_acquisti_fattura_acconto_id** | **int** | Amica.ModelloContabile predefinito per le fatture di acconto fornitori emesse. | [optional] 
**sede_legale** | [**SedeLegale**](SedeLegale.md) |  | [optional] 
**sede_operativa** | [**SedeOperativa**](SedeOperativa.md) |  | [optional] 
**sede_altra** | [**SedeAltra**](SedeAltra.md) |  | [optional] 

## Example

```python
from amica_sdk.models.preferenze import Preferenze

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


