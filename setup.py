from setuptools import setup, find_packages

setup(name="yaitst",
      version="0.0.1",
      description="Yai pre-built ternary search trees",
      long_description="""
Yai pre-built ternary search trees
""",
      author="Vee Satayamas",
      author_email="vsatayamas@gmail.com",
      packages=['yaitst'],
      package_dir={'yaitst': 'yaitst'},
      package_data={'yaitst': ['data/*.pickle']},
      test_suite="nose.collector")
