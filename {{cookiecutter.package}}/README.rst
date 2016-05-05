{{cookiecutter.package}}
========================

Install
-------

.. code:: sh
   python setup.py install


Testing
-------

.. code:: sh
   python setup.py test


Deployment
----------

.. code:: sh
   pip install -r requirements-dev.txt
   fab pack deploy
