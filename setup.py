from setuptools import setup, find_packages
import os

version = '0.0.5'

setup(name='collective.leadingmedia',
      version=version,
      description="Adds functionality to retrieve and prioritize media inside of dexterity containers.",
      long_description=open("README.txt").read() + "\n" +
                       open("docs/HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='leading media',
      author='Andre Goncalves',
      author_email='andre@intk.com',
      url='https://github.com/intk/collective.leadingmedia',
      download_url='https://github.com/intk/collective.leadingmedia/tarball/0.0.3',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
