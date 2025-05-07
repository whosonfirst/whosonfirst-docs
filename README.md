# whosonfirst-docs

Documentation for Who's On First. Theory, even.

## Important

There is no _actual documentation_ in this repository. It is a simple container with a simple name (and URL) with pointers to all the other things. Perhaps one day all those other things will be stored here but today is not that day.

## What is Who's On First

https://whosonfirst.org/what/
## Documentation

_This section was generated [by robots](bin/mk-docs.py) on 2025-05-07, derived from the [docs.json](docs.json) file_

### whosonfirst-placetypes

Where things are (and what they mean) in Who's On First documents

* https://github.com/whosonfirst/whosonfirst-placetypes

### whosonfirst-hierarchies

Relationships in Who's On First documents (see also: "All families are psychotic")

* https://github.com/whosonfirst/whosonfirst-hierarchies

### whosonfirst-sources

Where things come from in Who's On First documents

* https://github.com/whosonfirst/whosonfirst-sources

### whosonfirst-properties

What things mean in Who's On First documents

* https://github.com/whosonfirst/whosonfirst-properties

### whosonfirst-names

What things are called in Who's On First documents

* https://github.com/whosonfirst/whosonfirst-names

### whosonfirst-geometries

Types of geometries in Who's On First, and their meaning.

* https://github.com/whosonfirst/whosonfirst-geometries

### whosonfirst-dates

This is where we will think about time for Who's On First documents. Which is hard. Because it can not be denied...

* https://github.com/whosonfirst/whosonfirst-dates

### whosonfirst-categories

Buckets and vessels of meaning for Who's On First documents.

* https://github.com/whosonfirst/whosonfirst-categories


## First Principles

The gazetteer starts from a series of first principles:

### Who's On First has an opinion

It is important that Who's On First have an opinion not about any one place but rather
about _the nature of place_ itself. It is important for us to know and
understand the boundaries of our project in order to know what the project is
for and, critically, what the project is not.

### Leave as many decisions as possible to the "edges"

The world is a complicated place and we would like the gazetteer to be a project
that can support, or act as a scaffolding for, the sometimes contradictory
opinions that people have about it. We aim to leave as much meaning or
inference, as we can, about a place to individual users and applications. How
this will manifest itself in concrete terms remains to be seen but this is a
goal we have set for ourselves.

### Portability

The canonical source for a place is a text file, specifically GeoJSON with a
unique 64-bit numeric ID. This is because all computers speak "text files" and
"numbers". Text files can be inspected or updated in any old text editor. Text
files can be printed. Numbers are fast and cheap for databases to index.

We use text files because our primary concern for the data is: Ease of use,
robustness and portability _over time_. On measure, the benefits of plain old
text files outweigh both the costs and in many cases the benefits of other
formats.

Google's [Protocol Buffers](https://developers.google.com/protocol-buffers/) for
example are awesome but require that you install a whole lot of Google on your
computer in order to use them. ESRI's
[Shapefiles](https://en.wikipedia.org/wiki/Shapefile) are equally awesome and
their ubiquity and longevity is a testament to their utility but they too
require bespoke applications for even the most trivial of updates.

That does not mean that plain text or static files are necessarily the optimal
choice for delivery or distribution. We will account for that on a case-by-case
basis. If we need to pre-process all the data into a smaller and nimbler format
for a specific use-case then we will, but you will always be able to access the
data as simple text files.

### GeoJSON

We use [GeoJSON](http://www.geojson.org) as the primary exchange format for the
gazetteer for two interconnected and complementary reasons:

* It is structured data with the least amount of markup _today_. If someone
creates another markup language with even less scaffolding we might use that
instead but for now GeoJSON is a good happy medium.

* There are lots of tools for working with GeoJSON and, importantly, for
converting it into all the other formats that different people use.

## License

Please consult the [LICENSE.md](LICENSE.md) document for the licensing details for using Who's On First. The "tl;dr" is basically Creative Commons Attribution but please read the long version, yeah?

## Contributing

Please consult the [CONTRIBUTING.md](CONTRIBUTING.md) document for details on contributing to Who's On First.

## Blog

https://whosonfirst.org/blog/

## See also

* https://whosonfirst.org
