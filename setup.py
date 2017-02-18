from setuptools import setup

setup(
    name='secura-pi-cam',
    version='0.1',
    author=u'Raveen Savinda Rathnayake',
    author_email='raveen.s.r@gmail.com',
    url='https://github.com/RAVEENSAVINDA/rpi-security',
    license='GPLv2',
    description='A security system written in python to run on a Raspberry Pi with motion detection and mobile notifications',
    long_description=open('README.md').read(),
    scripts = [ 'bin/secura_pi_cam.py' ],
    data_files=[
        ('/lib/systemd/system', ['etc/secura_pi_cam.service']),
        ('/etc', ['etc/secura_pi_cam.conf']),
        ('/var/lib/secura_pi_cam', ['etc/state.yaml'])
    ],
    install_requires=[
        'python-telegram-bot',
        'picamera',
        'requests',
        'requests[security]',
        'netaddr',
        'netifaces',
        'pyyaml',
        'Pillow>=3.4.0'
    ],
    classifiers=[
    'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7'
    ],
)
