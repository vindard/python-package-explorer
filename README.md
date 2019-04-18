# `python3-indy` Package Explorer
A small tool I built to explore through the various methods in the `python3-indy` package from the terminal.

---

### To use

1. Run `$ python3`

1. Import the `IndyMethods` class with `$ from indy_explore import IndyMethods`

1. Assign to variable `$ i = IndyMethods()`

1. Assign methods:
    ```
    find = i.find
    print_docstrings = i.print_docstrings
    ```
 
1. Pass search strings to see results. Example:
    ```
    $ find('schema')
    
    [{'issuer_create_schema': 'anoncreds'},
     {'build_get_schema_request': 'ledger'},
     {'build_schema_request': 'ledger'},
     {'parse_get_schema_response': 'ledger'}]
  
    ```
    ```
    $ print_docstrings('create_schema')
    
    {'issuer_create_schema': 'anoncreds'}
    Call with: indy.anoncreds.issuer_create_schema

        Create credential schema entity that describes credential attributes list and allows credentials
        interoperability.

        Schema is public and intended to be shared with all anoncreds workflow actors usually by publishing SCHEMA transaction
        to Indy distributed ledger.

        It is IMPORTANT for current version POST Schema in Ledger and after that GET it from Ledger
        with correct seq_no to save compatibility with Ledger.
        After that can call indy_issuer_create_and_store_credential_def to build corresponding Credential Definition.

        :param issuer_did: DID of schema issuer
        :param name: a name the schema
        :param version: a version of the schema
        :param attrs: a list of schema attributes descriptions (the number of attributes should be less or equal than 125)
        :return:
           schema_id: identifier of created schema
            schema_json: schema as json
    ```
