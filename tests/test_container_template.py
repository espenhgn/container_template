# encoding: utf-8

"""
Test module for ``container_template.sif`` singularity build
or ``container_template`` dockerfile build

In case ``singularity`` is unavailable, the test function(s) should fall
back to ``docker``.
"""

import os
import socket
import subprocess
import tempfile


# port used by tests
sock = socket.socket()
sock.bind(('', 0))
port = sock.getsockname()[1]

# Check that (1) singularity or apptainer executables exist,
# and (2) if not, check for docker.
# If neither are found, tests will fall back to plain python.
# This may be useful for testing on a local machine, but should
# be revised for the particular usecase.
try:
    pth = os.path.join('containers', 'container_template.sif')
    try:
        out = subprocess.run('singularity', check=False)
    except FileNotFoundError:
        try:
            out = subprocess.run('apptainer', check=False)
        except FileNotFoundError as exc:
            raise FileNotFoundError from exc
    cwd = os.getcwd()
    PREFIX = f'singularity run {pth} python'
    PREFIX_MOUNT = f'singularity run --home={cwd}:/home/ {pth} python'
    PREFIX_CUSTOM_MOUNT = f'singularity run --home={cwd}:/home/ ' + \
        '{custom_mount}' + f'{pth} python'
except FileNotFoundError:
    try:
        out = subprocess.run('docker', check=False)
        pwd = os.getcwd()
        PREFIX = (f'docker run -p {port}:{port} ' +
                  'ghcr.io/precimed/container_template python')
        PREFIX_MOUNT = (
            f'docker run -p {port}:{port} ' +
            f'--mount type=bind,source={pwd},target={pwd} ' +
            'ghcr.io/precimed/container_template python')
        PREFIX_CUSTOM_MOUNT = (
            f'docker run -p {port}:{port} ' +
            f'--mount type=bind,source={pwd},target={pwd} ' +
            '{custom_mount} ' +
            'ghcr.io/precimed/container_template python')
    except FileNotFoundError:
        # neither singularity nor docker found, fall back to plain python
        PREFIX = 'python'
        PREFIX_MOUNT = 'python'
        PREFIX_CUSTOM_MOUNT = 'python'


def test_assert():
    """dummy test that should pass"""
    assert True


def test_container_template_python():
    """test that the Python installation works"""
    call = f'{PREFIX} --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_container_template_python_script():
    '''test that Python can run a script'''
    pwd = os.getcwd() if PREFIX.rfind('docker') >= 0 else '.'
    call = f'''{PREFIX_MOUNT} {pwd}/tests/extras/hello.py'''
    out = subprocess.run(call.split(' '), capture_output=True)
    assert out.returncode == 0


def test_container_template_python_script_from_tempdir():
    '''test that the tempdir is working'''
    with tempfile.TemporaryDirectory() as d:
        os.system(f'cp {pwd}/tests/extras/hello.py {d}/')
        custom_mount = f'--mount type=bind,source={d},target=/temp/'
        call = f'{PREFIX_CUSTOM_MOUNT.format(custom_mount=custom_mount)} ' + \
            '/temp/hello.py'
        out = subprocess.run(call.split(' '), check=False)
        assert out.returncode == 0


def test_container_template_python_packages():
    '''test that the Python packages are installed'''
    packages = [
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'seaborn',
        'sklearn',
        'pytest',
        'jupyterlab',
    ]
    importstr = 'import ' + ', '.join(packages)
    call = f"{PREFIX} -c '{importstr}'"
    out = subprocess.run(call, shell=True)
    assert out.returncode == 0
