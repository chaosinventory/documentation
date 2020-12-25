Database
========

Basic concept
-------------

- You have items which are from type product.
- Items can be in other items or locations.
- An item shouldn't have set both, but if, the item wins over the location.
- Locations can only be in locations.
- Against the location or item where the item usually sits is the current-item or current-location.
- This is the actual real-world state.
- You can override the usual location or item with an overlay.
- Overlays are temporary changes in the usual state.
- Overlays can be (de-) activated any time.
- Some view shows you the difference between usual and current state of the items.
- There is a global data management using key-value pairs.
- Keys are defined in advance.
- Items can get filtered and compared by keys and values.
- There is a global tag system.
- Each tag can be a sub-tag of some other.

Tables
------

ENTITY
~~~~~~
- Organisation or person
- Can own locations or items

LOCATION
~~~~~~~~
- Usually a not moving thing
- Helps organize your stuff

PRODUCT
~~~~~~~
- eg Dell XPS13, LAN Cable 3m

ITEM
~~~~
- Is an instance of a product
- Has a location or item as a marker to location your stuff

TAG
~~~
- Tag system to group and easily filter your stuff

OVERLAY
~~~~~~~
- Some temporary changes or planning of stuff for events

ERD
---

.. mermaid:: erd.mmd
