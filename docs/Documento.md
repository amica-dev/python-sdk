# Documento

Un documento (fattura, documento di trasporto, ecc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**anagrafica_id** | **int** | Identificativo univoco di &#x60;Anagrafica&#x60;. | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**causale_documento_id** | **int** | Identificativo univoco di &#x60;CausaleDocumento&#x60;. | [optional] 
**causale_documento** | [**CausaleDocumento**](CausaleDocumento.md) |  | [optional] 
**agente_id** | **int** | Identificativo univoco di &#x60;Anagrafica&#x60; dell&#39;agente. | [optional] 
**agente** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**pagamento_id** | **int** | Identificativo univoco di &#x60;Pagamento&#x60;. | [optional] 
**pagamento** | [**Pagamento**](Pagamento.md) |  | [optional] 
**vettore_id** | **int** | Identificativo univoco di &#x60;Anagrafica&#x60; del vettore. | [optional] 
**vettore** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**cassa_previdenziale_causale_iva_id** | **int** | Identificativo univoco della causale IVA della cassa previdenziale. | [optional] 
**modello_id** | **int** | Obsoleto. Non utilizzare. | [optional] 
**cassa_previdenziale_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**destinazione_id** | **int** | Identificativo univoco di &#x60;Indirizzo&#x60; di destinazione. | [optional] 
**destinazione** | [**Indirizzo**](Indirizzo.md) |  | [optional] 
**valuta_id** | **int** | Identificativo univoco di &#x60;Valuta&#x60;. | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**causale_magazzino_id** | **int** | Identificativo univoco di &#x60;CausaleMagazzino&#x60;. | [optional] 
**causale_magazzino** | [**CausaleMagazzino**](CausaleMagazzino.md) |  | [optional] 
**iva1_causale_iva_id** | **int** | Identificativo univoco della prima causale IVA. | [optional] 
**iva1_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva2_causale_iva_id** | **int** | Identificativo univoco della seconda causale IVA. | [optional] 
**iva2_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva3_causale_iva_id** | **int** | Identificativo univoco della terza causale IVA. | [optional] 
**iva3_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva4_causale_iva_id** | **int** | Identificativo univoco della quarta causale IVA. | [optional] 
**iva4_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**tipo_documento** | **str** | Tipologia del documento. | [optional] 
**documento_fiscale** | **str** | Tipo di documento fiscale. | [optional] 
**destinazione_diversa** | **bool** | Indica se la destinazione della merce è diversa dall&#39;indirizzo principale. | [optional] 
**iva_esclusa** | **bool** | Indica se i prezzi inseriti sono da considerarsi al netto dell&#39;IVA. Se &#x60;false&#x60;, l&#39;IVA verrà scorporata in fase di elaborazione (app ufficiali). | [optional] 
**ritenuta_include_cassa_previdenziale** | **bool** | Indica se la ritenuta deve essere applicata anche all&#39;importo della cassa previdenziale riportato nel documento. | [optional] 
**classe_documento** | **str** | Classe del documento. | [optional] 
**contatto** | **int** | Persona di contatto preferita, &#x60;AnagraficaNominativo1&#x60; oppure &#x60;AnagraficaNominativo2&#x60;. | [optional] 
**numero_parte_testo** | **str** | La parte alfanumerica del numero del documento, se presente. Ad esempio, \&quot;bis\&quot; per il documento num. 99/bis. | [optional] 
**numero_parte_numerica** | **int** | Il numero del documento, nella sua parte numerica. Ad esempio, 99 per il num. 99/bis. | [optional] 
**data** | **datetime** | Data del documento. | [optional] 
**stato** | **str** | Lo stato corrente del documento. Ad esempio: Bozza, oppure Emesso. | [optional] 
**data_scadenza_preventivo** | **datetime** | La data di scadenza, nel caso in cui il documento sia un preventivo. | [optional] 
**data_inizio_scadenze** | **datetime** | Data della prima scadenza di pagamento. | [optional] 
**sconto_percentuale** | **float** | Sconto, in percentuale, da calcolare sull&#39;intero importo del documento. Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto_incondizionato_importo** | **float** | Sconto, in valuta, da applicare all&#39;intero importo del documento. | [optional] 
**abbuono_importo** | **float** | Importo dell&#39;abbuono. | [optional] 
**ritenuta_percentuale** | **float** | Quota della ritenuta da applicare al documento. Il valore è una frazione: &#x60;0.20&#x60; corrisponde al 20%. | [optional] 
**enasarco_percentuale** | **float** | Contributo Enasarco da applicare al documento. | [optional] 
**enasarco_importo** | **float** | Importo Enasarco. | [optional] 
**quota_ritenuta_su_imponibile** | **float** | Quota dell&#39;imponibile su cui applicare la ritenuta. Il valore è una frazione: &#x60;0.50&#x60; corrisponde al 50%. | [optional] 
**cambio** | **float** | Tasso di cambio rispetto all&#39;Euro, nel caso in cui la &#x60;Valuta&#x60; del documento non sia l&#39;Euro. | [optional] 
**cassa_previdenziale_nome** | **str** | Nome della cassa previdenziale applicata al documento. | [optional] 
**cassa_previdenziale_percentuale** | **float** | Aliquota (percentuale) della cassa previdenziale da applicare al documento. Il valore è una frazione: &#x60;0.04&#x60; corrisponde al 4%. | [optional] 
**note** | **str** | Note. | [optional] 
**sconto_pagamento_percentuale** | **float** | Sconto riconosciuto in base alla modalità di pagamento utilizzata (es: +5% in caso di rimessa diretta). Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**iva1_imponibile** | **float** | Totale imponibile attribuibile a &#x60;Iva1CausaleIva&#x60; | [optional] 
**iva2_imponibile** | **float** | Totale imponibile attribuibile a &#x60;Iva2CausaleIva&#x60; | [optional] 
**iva3_imponibile** | **float** | Totale imponibile attribuibile a &#x60;Iva3CausaleIva&#x60; | [optional] 
**iva4_imponibile** | **float** | Totale imponibile attribuibile a &#x60;Iva4CausaleIva&#x60; | [optional] 
**iva1_imponibile_lordo** | **float** | Totale imponibile attribuibile a &#x60;Iva1CausaleIva&#x60; al lordo di eventuali sconti di fattura. | [optional] 
**iva2_imponibile_lordo** | **float** | Totale imponibile attribuibile a &#x60;Iva2CausaleIva&#x60; al lordo di eventuali sconti di fattura. | [optional] 
**iva3_imponibile_lordo** | **float** | Totale imponibile attribuibile a &#x60;Iva3CausaleIva&#x60; al lordo di eventuali sconti di fattura. | [optional] 
**iva4_imponibile_lordo** | **float** | Totale imponibile attribuibile a &#x60;Iva4CausaleIva&#x60; al lordo di eventuali sconti di fattura. | [optional] 
**iva1_imposta** | **float** | Totale imposta per &#x60;Iva1CausaleIva&#x60; | [optional] 
**iva2_imposta** | **float** | Totale imposta per &#x60;Iva2CausaleIva&#x60; | [optional] 
**iva3_imposta** | **float** | Totale imposta per &#x60;Iva3CausaleIva&#x60; | [optional] 
**iva4_imposta** | **float** | Totale imposta per &#x60;Iva4CausaleIva&#x60; | [optional] 
**totale_ritenuta** | **float** | Importo della ritenuta. | [optional] 
**totale_cassa_previdenziale** | **float** | Importo della cassa previdenziale. | [optional] 
**totale_spese** | **float** | Totale delle spese esenti e non esenti. | [optional] 
**totale_spese_esenti** | **float** | Totale delle spese esenti da IVA. | [optional] 
**totale_spese_non_esenti** | **float** | Totale delle spese non esenti da IVA. | [optional] 
**totale_merce** | **float** | Importo della merce. | [optional] 
**totale_merce_scontata** | **float** | Importo della merce scontata. | [optional] 
**totale_imponibile** | **float** | Totale imponibile, considerando tutte le causali IVA coinvolte. | [optional] 
**totale_imposta** | **float** | Imposta IVA. | [optional] 
**totale_esente** | **float** | Importi esenti da IVA. | [optional] 
**totale_documento** | **float** | Importo totale del documento. | [optional] 
**netto_a_pagare** | **float** | Netto a pagare. | [optional] 
**totale_split_payment** | **float** | Importo dello split payment. | [optional] 
**bollo** | **float** | Importo del bollo. | [optional] 
**xml_file_name** | **str** | Nome del file XML. | [optional] 
**riferimento_amministrazione** | **str** | Numero di riferimento dell&#39;amministrazione. | [optional] 
**banca** | [**BancaDocumento**](BancaDocumento.md) |  | [optional] 
**dati_trasporto** | [**DatiTrasporto**](DatiTrasporto.md) |  | [optional] 
**dati_sdi** | [**DatiSdi**](DatiSdi.md) |  | [optional] 
**dati_pa** | [**DatiPA**](DatiPA.md) |  | [optional] 
**righe** | [**List[BeneServizio]**](BeneServizio.md) | Righe del documento. | [optional] 
**spese_documento** | [**List[SpesaDocumento]**](SpesaDocumento.md) | Elenco delle spese. | [optional] 
**scadenze** | [**List[Scadenza]**](Scadenza.md) | Elenco delle scadenze. | [optional] 
**numero** | **str** | Numero completo del documento. Ad esempio, &#x60;99/bis&#x60;. Generato a partire da &#x60;NumeroParteNumerica&#x60; e &#x60;NumeroParteTesto&#x60;. Nota bene: proprietà valorizzata solo nel caso di un&#39;istanza salvata sul backend. | [optional] 
**media_file** | [**DocumentoMediaFile**](DocumentoMediaFile.md) |  | [optional] 
**allegato** | **str** | Obsoleto. Non utilizzare. | [optional] 
**bonus_fiscale_causale** | **str** | Causale del bonus fiscale. | [optional] 
**bonus_fiscale_importo** | **float** | Importo del bonus fiscale. | [optional] 
**bonus_fiscale_percentuale** | **float** | Percentuale del bonus fiscale. Il valore è una frazione: &#x60;0.50&#x60; corrisponde al 50%. | [optional] 
**progressivo_invio** | [**List[ProgressivoInvio]**](ProgressivoInvio.md) | Numeri di invio (progressivi), così come restituiti dallo Sdi. | [optional] 

## Example

```python
from amica_python_sdk.models.documento import Documento

# TODO update the JSON string below
json = "{}"
# create an instance of Documento from a JSON string
documento_instance = Documento.from_json(json)
# print the JSON string representation of the object
print(Documento.to_json())

# convert the object into a dict
documento_dict = documento_instance.to_dict()
# create an instance of Documento from a dict
documento_from_dict = Documento.from_dict(documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


