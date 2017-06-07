# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# pylint: disable=too-few-public-methods
# pylint: disable=method-hidden

"""JohnSON
   A simple Object-to-JSON serializer

   Using Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

   TODO (jonathadv): Documentation needs work.
"""

import json

class JSONable(object):
    """ JSONable """

    def to_json(self, sort_keys=False, pretty=False):
        """ Convert to JSON """

        if pretty:
            indent = 4
        else:
            indent = None

        return json.dumps(self.__dict__, sort_keys=sort_keys, indent=indent, cls=_ComplexEncoder)


class _ComplexEncoder(json.JSONEncoder):
    """ Complex Encoder """
    def default(self, obj):
        """ Default """

        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)
