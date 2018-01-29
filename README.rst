
protoc-gen-swagger
====================

.. image:: https://travis-ci.org/universe-proton/protoc-gen-swagger.svg?branch=master
    :target: https://travis-ci.org/universe-proton/protoc-gen-swagger


A python package for swagger's annotation protobuf files, which are located inside `grpc-gateway <https://github.com/grpc-ecosystem/grpc-gateway>`_ repository.

`Swagger <https://swagger.io/>`_ is a popular api tool. When you import swagger proto files in your protobuf message file, you may get stuck when using the generated python code.
An import error as the following:

.. code-block::

   ModuleNotFoundError: No module named 'protoc_gen_swagger'

With this package, you could forget the error.


Installation
============

We can simply use pip to install, as the following:

.. code-block:: bash

   $ pip install protoc-gen-swagger

or installing from git

.. code-block:: bash

   $ pip install git+https://github.com/universe-proton/protoc-gen-swagger


Maintain
=========

When the source repository `grpc-gateway <https://github.com/grpc-ecosystem/grpc-gateway>`_ is taged, we can use command `bash gen.sh <tag-version>` to update the package.
Maybe we could do some automated work in the future.

Now, this package version 0.1.0 is the same as grpc-gateway version v1.3.1 .


How to Contribute
=================

Open an `issue <https://github.com/universe-proton/protoc-gen-swagger/issues>`_, join a discussion or make a pull request.
