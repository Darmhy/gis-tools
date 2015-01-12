gis-tools
===================

Some Python code to take a path (a sequence of latitude/longitude points),
 and compute the distance between points along the path.

Install
=======

First install GEOS. On OS X, invoke
```
brew install geos
```
Then, invoke
```
pip install -r requirements.txt
```

Usage
=======
To run the test cases, invoke
```
python -m unittest lewfish.test_geopath
```
See lewfish/test_geopath.py for usage examples.