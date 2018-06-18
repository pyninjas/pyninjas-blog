pyninjas-blog: Simple Blog Application for Django - WIP
=======================================================

INSTALL
-------

* Using pip: `pip install pyninjas-blog`
* Using source code: `python setup.py install`

Add `django.contrib.humanize` to `INSTALLED_APPS` if not added:

.. code-block:: python

    INSTALLED_APPS = [
      # other apps
      'django.contrib.humanize',
    ]
    
Add `pyninjas.blog` to `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = [
      # other apps
      'pyninjas.blog',
    ]

Add `pyninjas.blog.urls` to your project's urls:

.. code-block:: python

    urlpatterns = [
      # other urls
      path('blog/', include('pyninjas.blog.urls', namespace='blog')),
    ]

By default pyninjas-blog has all templates needed for the blog.
However it uses simple template for a demo. You can enhance it with your current template by rewriting them:

* templates/blog/base.html
* templates/blog/index.html
* templates/blog/article.html

FEATURES
--------

* [x] Use of HTML as article format
* [] Atom and RSS feeds
* [] Preview for blog posts before publishing
* [x] slug only tag and article urls
* [] OpenGraph meta data
* [] Multilevel comments (replies)
* [] Loding contents using ajax


License
-------
Copyright (c) 2018 Emin Mastizada and contributors.
MIT License.
