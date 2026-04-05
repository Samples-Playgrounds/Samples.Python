

*   https://docs.pydantic.dev/latest/concepts/serialization/#serializers

"Pickling" is basically translating Python objects to a form that can easily be saved to disk or transmitted over a network, by using a module called pickle in the standard library.



https://www.reddit.com/r/Python/comments/4t6tah/what_is_pickling/

https://www.reddit.com/r/learnpython/comments/4nhjap/purpose_of_pickle/

https://docs.python.org/3/library/pickle.html


Protocol Buffer 

    https://protobuf.dev/getting-started/pythontutorial/
    
    - e.g. used in Caffe; 
    
    https://caffe.berkeleyvision.org/
    
    maintains type information, but you have to put quite much effort in
    it compared to pickle
MessagePack: 

    https://msgpack.org/
    
    
    See python package 
    
        https://pypi.org/project/msgpack-python/
    
            - supports streaming (source)
BSON
    https://bsonspec.org/
    
     see python package docs

    https://pymongo.readthedocs.io/en/stable/api/bson/index.html
    
    https://stackoverflow.com/questions/27527982/read-bson-file-in-python

    https://github.com/py-bson/bson

Depending on what exactly you want to store, there are other alternatives:

Apache Feather

    https://arrow.apache.org/docs/python/feather.html

    https://arrow.apache.org/dotnet/current/

    https://arrow.apache.org/docs/python/ipc.html#ipc

Apache Avro

    https://avro.apache.org/docs/1.11.1/getting-started-python/

    https://www.reddit.com/r/Python/comments/17x30n2/harmonizing_avro_and_python_a_dance_of_data/

    https://medium.com/vortechsa/harmonizing-avro-and-python-a-dance-of-data-classes-d1cc7bf6bb33

    https://medium.com/vortechsa/harmonizing-avro-and-python-a-dance-of-data-classes-d1cc7bf6bb33

    https://github.com/fastavro/fastavro/

    https://fastavro.readthedocs.io/en/latest/

    py-avro-schema 
    
        https://github.com/jpmorganchase/py-avro-schema
        
        has support for generic Python classes

    dataclasses-avroschema 
        
        https://github.com/marcosschroh/dataclasses-avroschema
        
        has support for dataclasses, pydantic models, and faust records
    pydantic-avro 
    
        https://github.com/godatadriven/pydantic-avro
        
        requires your Python class to inherit from pydantic.BaseModel

Apache Parquet

