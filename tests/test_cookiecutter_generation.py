import os
import re
import sys
import sh

import pytest
from binaryornot.check import is_binary

PATTERN = "{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    return {
        "project_name": "My Test Project",
        "project_slug": "test_project",
        "application_name": "Test Application"
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions,
    used by other tests cases
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            msg = "cookiecutter variable not replaced in {}"
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


def test_tox(capsys, cookies):
    """generated project should pass the tox tests"""
    result = cookies.bake()

    try:
        # The output from tox is of interest when running the test suite.
        with capsys.disabled():
            sh.tox(_cwd=str(result.project), _err_to_out=True, _out=sys.stdout)
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
