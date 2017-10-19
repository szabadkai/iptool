from distutils.core import setup

setup(
    name='iptool',
    version='0.1',
    url='https://github.com/szabadkai/iptool',
    download_url='https://github.com/szabadkai/iptool/archive/master.zip',
    packages=['iptool'],
    author='Levente Szbadkai',
    author_email='levente@szabadkai.com',
    description='tool for getting your machines IP adresses',
    requires=[
        'netifaces', 'netaddr', 'ipaddr'
    ]
)
