.. ENG G.Locateli documentation master file, created by
   sphinx-quickstart on Wed Sep 20 16:48:03 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Primeira Documentação
==========================================

Subtitulo
----------
Aqui é um parágrafo após o Subtitulo

Texto em *itálico*, **Negtrito** e em Marcação de código.

Ambiente Virtual
----------------

>>> .\env\Scripts\activate

Lista
------

* Item 1
* Item 2
* Item 3

Lista númerada
---------------

1. Item 1
2. Item 2
3. Item 3

Bloco Literal
--------------

A próxima linha pe um bloco literal.::
   Este é uma linha de bloco literal e ele deve estar identificado

   Aqui é outra linha de bloco literal

Aqui acabou

Exibindo Imagens
----------------

.. image:: images/back.png


Site [aeph] (https://www.aephbrasil.com.br)

.. _a link:

   https://www.aephbrasil.com.br



Tabelas
---------
======    ===========  ======   =======
Valor     Comparação   Valor    Status
======    ===========  ======   =======
10        \>             5       True
5         \>             10      False
======    ===========  ======   =======  


Bloco de Código
---------------

.. code-block:: python

   def exemplo()
      return "Isso é um bloco de código Python"


Bloco de Prompt de Comando
--------------------------

Este é um parágrafo comum.

>>> print("Monstra mensagem")
Mostra mensagem


.. toctree::
   :maxdepth: 2
   :caption: Conteúdos:

   introducao

Indíces da Tabelas
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
