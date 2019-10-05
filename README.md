
### About

Prevent version normalization when packaging Python projects with [setuptools](https://setuptools.readthedocs.io/en/latest/). For more details, see https://github.com/pypa/setuptools/issues/308.


### Usage

Install `setupnovernormalize` using e.g. `pip`:

    pip install setupnovernormalize

Then simply import `setupnovernormalize` in your `setup.py`:

    import setupnovernormalize
    
    ...
    
    setup(
        name='Your Package',
        version='version-that-will-not-be-touched',
        ...
    )
