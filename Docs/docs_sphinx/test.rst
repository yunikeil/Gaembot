
Test
=====

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   cookbook
   


Section
-------

Subsection
~~~~~~~~~~



You can use ``backticks`` for showing ``highlighted`` code.



`A cool website`_

.. _A cool website: http://sphinx-doc.org



A cool bit of code::

   Some cool Code

.. code-block:: rst

   A bit of **rst** which should be *highlighted* properly.



:ref:`reference-name`

.. _reference-name:

Cool section
------------



:option:`-i`

.. option:: -i <regex>, --ignore <regex>

   Ignore pages that match a specific pattern.



You can learn more about this at :pep:`8` or :rfc:`1984`.



These flags allow you to change the behavior of Crawler.
Check out how to use them in the Cookbook.

.. option:: -d <sec>, --delay <sec>

    Use a delay in between page fetchs so we don't overwhelm the remote server.
    Value in seconds.

Default: 1 second
    
.. option:: -i <regex>, --ignore <regex>

    Ignore pages that match a specific pattern.

Default: None

Getting started with Crawler is easy.
The main class you need to care about is :class:`~games.CirulliGame.GameCirulliView`

games.CirulliGame
-----------------

.. autoclass:: games.CirulliGame.GameCirulliView
    :members:
















