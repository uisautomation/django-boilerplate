# Django Boilerplate

This repository contains a
[cookiecutter](https://github.com/audreyr/cookiecutter) template for Django
projects created by the Automation Group.

## Quickstart

```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/uisautomation/django-boilerplate/
```

## Configuration

Cookie cutter will ask you for the following values:

* **project_name**: A human-readable name for the project. E.g. "UIS
    Frobnication-Requester".
* **project_slug**: A filename-safe version of the project name. Used to
    construct filenames for project metadata. By default, generated from project
    name. E.g., for the project name above, "uis_frobnication-requester".
* **project_module**: Name of the Python module containing project-wide
    settings, URL mapping, etc. By default, this is generated from project name,
    E.g., for the project name above, "uis_frobnication_requester_project".
* **application_name**: A human-readable name for the project's first Django
    application. By default, this is equal to the project name.
* **application_slug**: A filename-safe version of the application name. Used to
    construct filenames and the Django view namespace for the application.
    E.g., for the project name above, "uis_frobnication-requester".
* **application_module**: Name of the Python module containing the first
    application for the project. By default, this is generated from the project
    name.  E.g., for the project name above,
    "uis_frobnication_requester".
* **secret_key**: Secret key used in development. By default this is a long
    string made unique by prepending the **project_slug** value.
* **postgresql_version**: Version of PostgreSQL which should be used for running
    tests.

### "Slug" versus "module"

It's worth distinguishing between "slug" and "module" names here. The practical
difference is that a "slug" name may contain a hyphen and a "module" name may
not. The semantic difference is that the "module" name is used when one needs to
refer to a particular bit of code and "slug" is used for various "short name"
metadata. The difference is best demonstrated by the project slug/module name
and application slug/module name. Often the name of the first application is
better represented by the project name and the Django project has to have a
similar but different name. Having the project module name explicitly end with
``_project`` makes the distinction clear.

## Testing

The repository is tested via the ``tox`` test runner. The tests include a basic
check that the template can generate output and that running tox in the
generated output succeeds.
