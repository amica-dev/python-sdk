# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.3.7
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from amica_python_sdk.models.ddt_import_data import DdtImportData
from amica_python_sdk.models.distinct_property_group import DistinctPropertyGroup
from amica_python_sdk.models.documento import Documento
from amica_python_sdk.models.documento_compute_data import DocumentoComputeData
from amica_python_sdk.models.documento_compute_result import DocumentoComputeResult
from amica_python_sdk.models.documento_import_data import DocumentoImportData
from amica_python_sdk.models.documento_totali import DocumentoTotali
from amica_python_sdk.models.ordini_import_data import OrdiniImportData
from amica_python_sdk.models.periodic_invoicing_data import PeriodicInvoicingData
from amica_python_sdk.models.reso_import_data import ResoImportData

from amica_python_sdk.api_client import ApiClient, RequestSerialized
from amica_python_sdk.api_response import ApiResponse
from amica_python_sdk.rest import RESTResponseType


class DocumentoApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def documento_compute(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_compute_data: Annotated[Optional[DocumentoComputeData], Field(description="Dati di input per l'operazione di calcolo.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> DocumentoComputeResult:
        """Calcola i totali di un documento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_compute_data: Dati di input per l'operazione di calcolo.
        :type documento_compute_data: DocumentoComputeData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_compute_serialize(
            company_id=company_id,
            idempotency_key=idempotency_key,
            documento_compute_data=documento_compute_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DocumentoComputeResult",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_compute_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_compute_data: Annotated[Optional[DocumentoComputeData], Field(description="Dati di input per l'operazione di calcolo.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[DocumentoComputeResult]:
        """Calcola i totali di un documento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_compute_data: Dati di input per l'operazione di calcolo.
        :type documento_compute_data: DocumentoComputeData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_compute_serialize(
            company_id=company_id,
            idempotency_key=idempotency_key,
            documento_compute_data=documento_compute_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DocumentoComputeResult",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_compute_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_compute_data: Annotated[Optional[DocumentoComputeData], Field(description="Dati di input per l'operazione di calcolo.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Calcola i totali di un documento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_compute_data: Dati di input per l'operazione di calcolo.
        :type documento_compute_data: DocumentoComputeData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_compute_serialize(
            company_id=company_id,
            idempotency_key=idempotency_key,
            documento_compute_data=documento_compute_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DocumentoComputeResult",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_compute_serialize(
        self,
        company_id,
        idempotency_key,
        documento_compute_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento_compute_data is not None:
            _body_params = documento_compute_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/compute',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_delete(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Elimina un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_delete_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_delete_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Elimina un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_delete_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_delete_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Elimina un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_delete_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_delete_serialize(
        self,
        company_id,
        id,
        validation_override,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v3/{companyId}/Documento/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_distinct(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        selector: Annotated[StrictStr, Field(description="Il campo usato per distinguere gli elementi.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[DistinctPropertyGroup]:
        """Restituisce una lista di elementi distinti.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param selector: Il campo usato per distinguere gli elementi. (required)
        :type selector: str
        :param skip: Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_distinct_serialize(
            company_id=company_id,
            selector=selector,
            skip=skip,
            take=take,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DistinctPropertyGroup]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_distinct_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        selector: Annotated[StrictStr, Field(description="Il campo usato per distinguere gli elementi.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[DistinctPropertyGroup]]:
        """Restituisce una lista di elementi distinti.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param selector: Il campo usato per distinguere gli elementi. (required)
        :type selector: str
        :param skip: Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_distinct_serialize(
            company_id=company_id,
            selector=selector,
            skip=skip,
            take=take,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DistinctPropertyGroup]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_distinct_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        selector: Annotated[StrictStr, Field(description="Il campo usato per distinguere gli elementi.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce una lista di elementi distinti.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param selector: Il campo usato per distinguere gli elementi. (required)
        :type selector: str
        :param skip: Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_distinct_serialize(
            company_id=company_id,
            selector=selector,
            skip=skip,
            take=take,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DistinctPropertyGroup]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_distinct_serialize(
        self,
        company_id,
        selector,
        skip,
        take,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if selector is not None:
            
            _query_params.append(('Selector', selector))
            
        if skip is not None:
            
            _query_params.append(('Skip', skip))
            
        if take is not None:
            
            _query_params.append(('Take', take))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v3/{companyId}/Documento/distinct',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_emit(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento da emettere.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Emette un documento.

        A seconda del tipo di documento, l'emissione comporta una serie di operazioni amministrative e contabili:               1) Aggiornamento dell'`Anagrafica` coinvolta (fatturato, numero fatture, ecc.);              2) Creazione della registrazione contabile di emissione;              3) Creazione delle scadenze attive o passive, in base al tipo di pagamento;              4) Eventuale autoproduzione dei beni fatturati tramite distinta base, se l'opzione è attiva;              5) Creazione del movimento di magazzino;              6) Aggiornamento delle giacenze dei beni coinvolti, nei rispettivi magazzini;              7) Aggiornamento di eventuali ordini collegati.               Un documento già emesso non può essere riemesso. Alcuni tipi di documento non supportano l'emissione (ordini e preventivi, ad esempio).

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param documento_id: ID univoco del documento da emettere. (required)
        :type documento_id: int
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_emit_serialize(
            company_id=company_id,
            documento_id=documento_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_emit_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento da emettere.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Emette un documento.

        A seconda del tipo di documento, l'emissione comporta una serie di operazioni amministrative e contabili:               1) Aggiornamento dell'`Anagrafica` coinvolta (fatturato, numero fatture, ecc.);              2) Creazione della registrazione contabile di emissione;              3) Creazione delle scadenze attive o passive, in base al tipo di pagamento;              4) Eventuale autoproduzione dei beni fatturati tramite distinta base, se l'opzione è attiva;              5) Creazione del movimento di magazzino;              6) Aggiornamento delle giacenze dei beni coinvolti, nei rispettivi magazzini;              7) Aggiornamento di eventuali ordini collegati.               Un documento già emesso non può essere riemesso. Alcuni tipi di documento non supportano l'emissione (ordini e preventivi, ad esempio).

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param documento_id: ID univoco del documento da emettere. (required)
        :type documento_id: int
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_emit_serialize(
            company_id=company_id,
            documento_id=documento_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_emit_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento da emettere.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Emette un documento.

        A seconda del tipo di documento, l'emissione comporta una serie di operazioni amministrative e contabili:               1) Aggiornamento dell'`Anagrafica` coinvolta (fatturato, numero fatture, ecc.);              2) Creazione della registrazione contabile di emissione;              3) Creazione delle scadenze attive o passive, in base al tipo di pagamento;              4) Eventuale autoproduzione dei beni fatturati tramite distinta base, se l'opzione è attiva;              5) Creazione del movimento di magazzino;              6) Aggiornamento delle giacenze dei beni coinvolti, nei rispettivi magazzini;              7) Aggiornamento di eventuali ordini collegati.               Un documento già emesso non può essere riemesso. Alcuni tipi di documento non supportano l'emissione (ordini e preventivi, ad esempio).

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param documento_id: ID univoco del documento da emettere. (required)
        :type documento_id: int
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_emit_serialize(
            company_id=company_id,
            documento_id=documento_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_emit_serialize(
        self,
        company_id,
        documento_id,
        idempotency_key,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if documento_id is not None:
            _path_params['documentoId'] = documento_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{documentoId}/emit',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_get(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Restituisce un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_get_serialize(
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_get_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Restituisce un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_get_serialize(
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_get_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce un elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_get_serialize(
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_get_serialize(
        self,
        company_id,
        id,
        expand,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'Expand': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('Expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v3/{companyId}/Documento/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_acconti(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID degli acconti da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da uno o più acconti in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID degli acconti da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_acconti_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_acconti_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID degli acconti da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da uno o più acconti in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID degli acconti da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_acconti_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_acconti_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID degli acconti da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da uno o più acconti in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID degli acconti da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_acconti_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_acconti_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        documento_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento_import_data is not None:
            _body_params = documento_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/acconto',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_ddt(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ddt_import_data: Annotated[Optional[DdtImportData], Field(description="Opzioni di importazione, inclusi gli ID dei DDT da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da uno o più DDT in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ddt_import_data: Opzioni di importazione, inclusi gli ID dei DDT da importare.
        :type ddt_import_data: DdtImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ddt_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ddt_import_data=ddt_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_ddt_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ddt_import_data: Annotated[Optional[DdtImportData], Field(description="Opzioni di importazione, inclusi gli ID dei DDT da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da uno o più DDT in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ddt_import_data: Opzioni di importazione, inclusi gli ID dei DDT da importare.
        :type ddt_import_data: DdtImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ddt_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ddt_import_data=ddt_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_ddt_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ddt_import_data: Annotated[Optional[DdtImportData], Field(description="Opzioni di importazione, inclusi gli ID dei DDT da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da uno o più DDT in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ddt_import_data: Opzioni di importazione, inclusi gli ID dei DDT da importare.
        :type ddt_import_data: DdtImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ddt_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ddt_import_data=ddt_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_ddt_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        ddt_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if ddt_import_data is not None:
            _body_params = ddt_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/ddt',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_ordini(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ordini_import_data: Annotated[Optional[OrdiniImportData], Field(description="Opzioni di importazione, inclusi gli ID degli ordini da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da uno o più ordini in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ordini_import_data: Opzioni di importazione, inclusi gli ID degli ordini da importare.
        :type ordini_import_data: OrdiniImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ordini_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ordini_import_data=ordini_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_ordini_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ordini_import_data: Annotated[Optional[OrdiniImportData], Field(description="Opzioni di importazione, inclusi gli ID degli ordini da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da uno o più ordini in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ordini_import_data: Opzioni di importazione, inclusi gli ID degli ordini da importare.
        :type ordini_import_data: OrdiniImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ordini_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ordini_import_data=ordini_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_ordini_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        ordini_import_data: Annotated[Optional[OrdiniImportData], Field(description="Opzioni di importazione, inclusi gli ID degli ordini da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da uno o più ordini in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param ordini_import_data: Opzioni di importazione, inclusi gli ID degli ordini da importare.
        :type ordini_import_data: OrdiniImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_ordini_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            ordini_import_data=ordini_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_ordini_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        ordini_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if ordini_import_data is not None:
            _body_params = ordini_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/ordine',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_preventivi(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei preventivi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da uno o più preventivi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID dei preventivi da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_preventivi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_preventivi_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei preventivi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da uno o più preventivi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID dei preventivi da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_preventivi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_preventivi_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei preventivi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da uno o più preventivi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID dei preventivi da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_preventivi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_preventivi_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        documento_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento_import_data is not None:
            _body_params = documento_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/preventivo',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_pro_forma(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID delle proforma da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da una o più fatture proforma in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID delle proforma da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_pro_forma_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_pro_forma_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID delle proforma da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da una o più fatture proforma in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID delle proforma da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_pro_forma_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_pro_forma_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento_import_data: Annotated[Optional[DocumentoImportData], Field(description="Opzioni di importazione, inclusi gli ID delle proforma da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da una o più fatture proforma in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento_import_data: Opzioni di importazione, inclusi gli ID delle proforma da importare.
        :type documento_import_data: DocumentoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_pro_forma_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento_import_data=documento_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_pro_forma_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        documento_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento_import_data is not None:
            _body_params = documento_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/proforma',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_import_resi(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        reso_import_data: Annotated[Optional[ResoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei resi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Importa righe da uno o più resi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param reso_import_data: Opzioni di importazione, inclusi gli ID dei resi da importare.
        :type reso_import_data: ResoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_resi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            reso_import_data=reso_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_import_resi_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        reso_import_data: Annotated[Optional[ResoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei resi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Importa righe da uno o più resi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param reso_import_data: Opzioni di importazione, inclusi gli ID dei resi da importare.
        :type reso_import_data: ResoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_resi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            reso_import_data=reso_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_import_resi_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID del documento di destinazione.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        reso_import_data: Annotated[Optional[ResoImportData], Field(description="Opzioni di importazione, inclusi gli ID dei resi da importare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa righe da uno o più resi in un documento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID del documento di destinazione. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param reso_import_data: Opzioni di importazione, inclusi gli ID dei resi da importare.
        :type reso_import_data: ResoImportData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_import_resi_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            reso_import_data=reso_import_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_import_resi_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        reso_import_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if reso_import_data is not None:
            _body_params = reso_import_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{id}/import/reso',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_list(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Documento]:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_list_serialize(
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_list_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Documento]]:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_list_serialize(
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_list_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_list_serialize(
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_list_serialize(
        self,
        company_id,
        skip,
        take,
        skip_total_count,
        filter,
        order,
        expand,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'Expand': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if skip is not None:
            
            _query_params.append(('Skip', skip))
            
        if take is not None:
            
            _query_params.append(('Take', take))
            
        if skip_total_count is not None:
            
            _query_params.append(('SkipTotalCount', skip_total_count))
            
        if filter is not None:
            
            _query_params.append(('Filter', filter))
            
        if order is not None:
            
            _query_params.append(('Order', order))
            
        if expand is not None:
            
            _query_params.append(('Expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v3/{companyId}/Documento',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_new_instance(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Restituisce una nuova istanza di un documento del tipo specificato.

        Richiede il parametro query `TipoDocumento` (int) che indica il tipo di documento da creare.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_serialize(
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_new_instance_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Restituisce una nuova istanza di un documento del tipo specificato.

        Richiede il parametro query `TipoDocumento` (int) che indica il tipo di documento da creare.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_serialize(
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_new_instance_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce una nuova istanza di un documento del tipo specificato.

        Richiede il parametro query `TipoDocumento` (int) che indica il tipo di documento da creare.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_serialize(
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_new_instance_serialize(
        self,
        company_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v3/{companyId}/Documento/new',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_new_instance_from_template(
        self,
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).


        :param documento_id: ID univoco del documento. (required)
        :type documento_id: int
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_from_template_serialize(
            documento_id=documento_id,
            company_id=company_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_new_instance_from_template_with_http_info(
        self,
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).


        :param documento_id: ID univoco del documento. (required)
        :type documento_id: int
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_from_template_serialize(
            documento_id=documento_id,
            company_id=company_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_new_instance_from_template_without_preload_content(
        self,
        documento_id: Annotated[StrictInt, Field(description="ID univoco del documento.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).


        :param documento_id: ID univoco del documento. (required)
        :type documento_id: int
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_new_instance_from_template_serialize(
            documento_id=documento_id,
            company_id=company_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_new_instance_from_template_serialize(
        self,
        documento_id,
        company_id,
        idempotency_key,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if documento_id is not None:
            _path_params['documentoId'] = documento_id
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/{documentoId}/newinstancefromtemplate',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_periodic_invoicing(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[Optional[StrictInt], Field(description="Non utilizzato.")] = None,
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        periodic_invoicing_data: Annotated[Optional[PeriodicInvoicingData], Field(description="Criteri e opzioni di fatturazione periodica.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Documento]:
        """Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: Non utilizzato.
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param periodic_invoicing_data: Criteri e opzioni di fatturazione periodica.
        :type periodic_invoicing_data: PeriodicInvoicingData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_periodic_invoicing_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            periodic_invoicing_data=periodic_invoicing_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_periodic_invoicing_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[Optional[StrictInt], Field(description="Non utilizzato.")] = None,
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        periodic_invoicing_data: Annotated[Optional[PeriodicInvoicingData], Field(description="Criteri e opzioni di fatturazione periodica.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Documento]]:
        """Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: Non utilizzato.
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param periodic_invoicing_data: Criteri e opzioni di fatturazione periodica.
        :type periodic_invoicing_data: PeriodicInvoicingData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_periodic_invoicing_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            periodic_invoicing_data=periodic_invoicing_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_periodic_invoicing_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[Optional[StrictInt], Field(description="Non utilizzato.")] = None,
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        periodic_invoicing_data: Annotated[Optional[PeriodicInvoicingData], Field(description="Criteri e opzioni di fatturazione periodica.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: Non utilizzato.
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param periodic_invoicing_data: Criteri e opzioni di fatturazione periodica.
        :type periodic_invoicing_data: PeriodicInvoicingData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_periodic_invoicing_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            periodic_invoicing_data=periodic_invoicing_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Documento]",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
            '409': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_periodic_invoicing_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        periodic_invoicing_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if id is not None:
            
            _query_params.append(('id', id))
            
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if periodic_invoicing_data is not None:
            _body_params = periodic_invoicing_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento/periodicinvoicing',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_post(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Salva un nuovo elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_post_serialize(
            company_id=company_id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "Documento",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_post_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Salva un nuovo elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_post_serialize(
            company_id=company_id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "Documento",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_post_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Salva un nuovo elemento.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_post_serialize(
            company_id=company_id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "Documento",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '422': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_post_serialize(
        self,
        company_id,
        validation_override,
        idempotency_key,
        documento,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento is not None:
            _body_params = documento


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v3/{companyId}/Documento',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_put(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Documento:
        """Aggiorna un elemento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_put_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '409': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_put_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Documento]:
        """Aggiorna un elemento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_put_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '409': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_put_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.")] = None,
        documento: Annotated[Optional[Documento], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Aggiorna un elemento esistente.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param idempotency_key: Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`.
        :type idempotency_key: str
        :param documento: Istanza dell'elemento da salvare.
        :type documento: Documento
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_put_serialize(
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            idempotency_key=idempotency_key,
            documento=documento,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Documento",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
            '409': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_put_serialize(
        self,
        company_id,
        id,
        validation_override,
        idempotency_key,
        documento,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if documento is not None:
            _body_params = documento


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v3/{companyId}/Documento/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def documento_totali(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.")] = None,
        raggruppa: Annotated[Optional[StrictStr], Field(description="Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[DocumentoTotali]:
        """Restituisce i totali dei documenti che soddisfano il filtro, eventualmente raggruppati per mese, anno o anagrafica. I totali sono calcolati dal server: per conoscere il fatturato di un periodo non serve scaricare i documenti.

         Le note di credito, clienti e fornitori, entrano nei totali con segno negativo.  Senza raggruppamento la risposta contiene un solo gruppo, anche se nessun documento soddisfa il filtro.             Raggruppando per mese o per anno i gruppi sono in ordine cronologico e `Periodo` ne indica il primo giorno;             raggruppando per anagrafica sono in ordine di totale documento decrescente, con `AnagraficaId` e             `RagioneSociale`.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param filter: Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.
        :type filter: str
        :param raggruppa: Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.
        :type raggruppa: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_totali_serialize(
            company_id=company_id,
            filter=filter,
            raggruppa=raggruppa,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DocumentoTotali]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def documento_totali_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.")] = None,
        raggruppa: Annotated[Optional[StrictStr], Field(description="Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[DocumentoTotali]]:
        """Restituisce i totali dei documenti che soddisfano il filtro, eventualmente raggruppati per mese, anno o anagrafica. I totali sono calcolati dal server: per conoscere il fatturato di un periodo non serve scaricare i documenti.

         Le note di credito, clienti e fornitori, entrano nei totali con segno negativo.  Senza raggruppamento la risposta contiene un solo gruppo, anche se nessun documento soddisfa il filtro.             Raggruppando per mese o per anno i gruppi sono in ordine cronologico e `Periodo` ne indica il primo giorno;             raggruppando per anagrafica sono in ordine di totale documento decrescente, con `AnagraficaId` e             `RagioneSociale`.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param filter: Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.
        :type filter: str
        :param raggruppa: Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.
        :type raggruppa: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_totali_serialize(
            company_id=company_id,
            filter=filter,
            raggruppa=raggruppa,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DocumentoTotali]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def documento_totali_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.")] = None,
        raggruppa: Annotated[Optional[StrictStr], Field(description="Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce i totali dei documenti che soddisfano il filtro, eventualmente raggruppati per mese, anno o anagrafica. I totali sono calcolati dal server: per conoscere il fatturato di un periodo non serve scaricare i documenti.

         Le note di credito, clienti e fornitori, entrano nei totali con segno negativo.  Senza raggruppamento la risposta contiene un solo gruppo, anche se nessun documento soddisfa il filtro.             Raggruppando per mese o per anno i gruppi sono in ordine cronologico e `Periodo` ne indica il primo giorno;             raggruppando per anagrafica sono in ordine di totale documento decrescente, con `AnagraficaId` e             `RagioneSociale`.

        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param filter: Condizioni di ricerca che selezionano i documenti da sommare, con la stessa sintassi del parametro `Filter` dell'elenco dei documenti. Senza filtro si sommano tutti i documenti dell'azienda, compresi ordini e preventivi: per il fatturato, filtrare per classe e tipo di documento.
        :type filter: str
        :param raggruppa: Come raggruppare i totali: `Nessuno` (un solo gruppo, predefinito), `Mese`, `Anno` o `Anagrafica`.
        :type raggruppa: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._documento_totali_serialize(
            company_id=company_id,
            filter=filter,
            raggruppa=raggruppa,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[DocumentoTotali]",
            '400': "ProblemDetails",
            '429': None,
            '401': None,
            '403': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _documento_totali_serialize(
        self,
        company_id,
        filter,
        raggruppa,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if filter is not None:
            
            _query_params.append(('Filter', filter))
            
        if raggruppa is not None:
            
            _query_params.append(('Raggruppa', raggruppa))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/problem+json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2ClientCredentials', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v3/{companyId}/Documento/totali',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


