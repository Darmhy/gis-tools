gis-tools
===================

Some Python code to take a path (a sequence of latitude/longitude points),
 and compute the distance between points along the path. At the moment,
 this code will only work well for paths that lie within small regions (cities) that are within a UTM zone. See source for more details.

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