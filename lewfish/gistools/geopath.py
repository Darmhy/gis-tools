from shapely.geometry import LineString, Point
import utm

from geopy.distance import vincenty

class GeoPath(object):
    """Represents a connected sequence of geospatial coordinates. 
    
    To compute distances, spherical lat/lon coordinates are first
    projected to planar coordinates using the UTM projection. Then,
    simple euclidean distance metrics can be used. However, the distances
    are only approximations due to the projection.
    In an informal experiment, the approximation is only off by 0.03% 
    over a city-sized distance. Note that this method will not work for
    paths over multiple UTM zones. This can be fixed in future versions 
    by using a different projection method.
    """

    def __init__(self, path):
        """Initialize a path.
        
        Arguments:
        path -- a list of (lat, lon) tuples
        """

        self.path = path
        self.start = self.path[0]

        #convert the path to UTM coordinates so that one unit
        #is equal to one meter
        self.utm_path = [self.to_utm(c) for c in self.path]
        self.utm_path = LineString(self.utm_path)
        self.path_length = None

    def to_utm(self, c):
        """Convert a coordinate to UTM format.

        Arguments:
        c -- a coordinate represented as a (lat, lon) tuple"""

        u = utm.from_latlon(*c)
        return (u[0],u[1])
        
    def get_len(self):
        """Return the length of the path in kilometers."""
        return self.utm_path.length / 1000.0

    def get_dist(self, c1, c2):
        """Return kilometers between two coordinates along path.

        Arguments:
        c1 -- a coordinate represented as a (lat, lon) tuple
        c2 -- a coordinate represented as a (lat, lon) tuple
        """

        p1 = self.utm_path.project(Point(*self.to_utm(c1)))
        p2 = self.utm_path.project(Point(*self.to_utm(c2)))
        return abs(p2 - p1) / 1000.0

    def get_norm_pos(self, c):
        """Return normalized position of coordinate along path, ranging
        from 0 (beginning of path) to 1 (end of path).

        Arguments:
        c -- a coordinate represented as a (lat, lon) tuple
        """

        d = self.get_dist(self.start, c)
        return d / self.get_len()

    def get_dist_to_path(self, c):
        """Return the shortest distance to the path in km."""

        c = Point(*self.to_utm(c))
        #closest = self.utm_path.interpolate(self.utm_path.project(Point(*self.to_utm(c))))
        return self.utm_path.distance(c) / 1000.0
    
def exp():
    """An experiment to compute the relative error.

    Arguments:
    c -- a coordinate represented as a (lat, lon) tuple
    """
    
    #olney transportation center
    p1 = (40.040042, -75.144772)
    #att station
    p2 = (39.907473, -75.173907)

    #the distance, taking into account curvature of the earth
    v_dist = vincenty(p1, p2).meters / 1000.0

    gp = GeoPath([p1,p2])
    gp_dist = gp.get_len()

    error = abs(v_dist - gp_dist)
    rel_error = error / v_dist
    print rel_error

    #the distance computed by GeoPath is within 0.03%
    #of the "true" distance over the length of Broad
    #Street line, which is good enough
    
if __name__ == "__main__":
    exp()
