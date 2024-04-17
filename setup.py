from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
          name="pyLevelSet",
          version="0.2.0",
          author="Shi-YiHao",
          author_email="syh-1999@outlook.com",
          description="A Level-set particles generator",
          long_description=long_description,
          long_description_content_type="text/markdown",
          url="https://github.com/Yihao-Shi/pyLevelSet",
          packages=find_packages(exclude='images'),
          exclude_package_data={'bandwidth_reporter':['*.png', '*.vtu', '*.vtr', '*.stl']},
          include_package_data=True,
          python_requires='>=3.8,<=3.11',
          install_requires=[
                               'numpy',
                               'scipy',
                               'trimesh',
                               'scikit-image',
                               'rtree',
                               'open3d',
                               'matplotlib',
                               'pyevtk'
                           ],
          classifiers=[
                          'Programming Language :: Python :: 3.8',
                          'Programming Language :: Python :: 3.9',
                          'Programming Language :: Python :: 3.10',
                          'License :: OSI Approved :: GNU Affero General Public License v3',
                          'Development Status :: 3 - Alpha'
                      ]
    )
