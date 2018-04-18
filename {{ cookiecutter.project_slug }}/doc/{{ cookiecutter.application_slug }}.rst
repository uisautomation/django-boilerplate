{{ cookiecutter.application_name }}
===============================================================================

Installation
````````````

Add the ``{{ cookiecutter.application_module }}`` application to your
``INSTALLED_APPS`` configuration as usual.

Views and serializers
`````````````````````

.. automodule:: {{ cookiecutter.application_module }}.views
    :members:

Default URL routing
```````````````````

.. automodule:: {{ cookiecutter.application_module }}.urls
    :members:

Application configuration
`````````````````````````

.. automodule:: {{ cookiecutter.application_module }}.apps
    :members:
