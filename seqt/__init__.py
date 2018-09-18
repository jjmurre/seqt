from string import Template
from six.moves import configparser


class SQLQuery(object):

    def __init__(self, sql, is_fragment=False):
        self.sql = sql

    def __call__(self, **kwargs):
        s = Template(self.sql)
        return s.substitute(kwargs)


class SQLFragment(SQLQuery):

    def __call__(self, **kwargs):
        condition = kwargs.pop('condition', True)
        if not condition:
            return ''
        return super(SQLFragment, self).__call__(**kwargs)


class SQLFactory(object):

    def __init__(self, file_path):
        cp = configparser.RawConfigParser()
        cp.readfp(open(file_path))
        self.all = dict(cp.items('queries'))
        self.fragments = dict(cp.items('fragments'))
        self.all.update(self.fragments)

    def __getattr__(self, name):
        if name in self.fragments:
            return SQLFragment(self.all[name])
        return SQLQuery(self.all[name])
