####RestLogging

Setup RestApiHandler for sequence logger.
```
logger = logging.getLogger("sequence")
try:
    from restapi_logging_handler import RestApiHandler

    restapihandler = RestApiHandler("http://172.17.0.1:9004/")
    logger.addHandler(restapihandler)

except Exception as e:
    pass

```

Usage, use class in Sequences.py

```
sq = Sequences("Operator_Components Mgmnt")
sq.task("Do stuff")
sq.send_to("Service", "Pass data to service")
...
```

run the app.py

```
python app.py
```

run the program you want to generate sequence for.

Results resemble:
```
Operator_Components Mgmnt->Operator_Components Mgmnt: Generate CR for sink
Operator_Components Mgmnt->Operator_Components Mgmnt: Generate CR for source
Operator_Components Mgmnt->Operator_Components Mgmnt: Generate CSR's
Operator_Components Mgmnt->Account Manager: Send CR/CSR to sign and store
Operator_Components Mgmnt->Service_Components Mgmnt (Sink): Post CR-Sink, CSR-Sink
Operator_Components Mgmnt->Service_Components Mgmnt (Source): Post CR-Source, CSR-Source
Service_Components Mgmnt->Service_Components Mgmnt: Install CR/CSR
Service_Components Mgmnt->Service_Components Mgmnt: CR Received
Service_Components Mgmnt->Service_Components Mgmnt: Verify CR format and mandatory fields
```
