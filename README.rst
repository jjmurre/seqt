seqt
====

Structured Easy Query Templates

For projects that do not use an ORM, but raw sql strings, it can be convenient
to have the sql in one place, instead of sprinkling the code with sql strings.

This little library makes it possible to put the sql strings in an `*.ini` file.
The keys of the ini file entries will be converted into callable functions.

Example
=======

Given an ini file with the following contents::

    [queries]

    fetch_object:
        SELECT * from schema.table
        WHERE id = %s

    fetch_objects:
        SELECT * from schema.table
        WHERE id IN ($slots)

    fetch_objects_by_name:
        SELECT * from schema.table
        WHERE $name_filter

    [fragments]
    name_filter: name = %s


Now, the queries can be used from python::

    from seqt import SQLFactory

    queries = SQLFactory('<path-to-ini>')

    sql = queries.fetch_object()
    
    # Use some DB-API compliant connection/cursor like mysqlclient

    with connection.cursor() as cursor:
        rows = cursor.execute(sql, (1,))


Inside the generated sql strings, template variables can be embedded using `$name` syntax. E.g.::

    ids = [1, 4, 5]
    slots = ', '.join(['%s'] * len(ids))
    sql = queries.fetch_objects(slots=slots)

    with connection.cursor() as cursor:
        rows = cursor.execute(sql, ids)


Filters can be prepared for re-use by using fragments::

    name_filter = queries.name_filter()
    sql = queries.fetch_objects_by_name(name_filter=name_filter)

    with connection.cursor() as cursor:
        rows = cursor.execute(sql, ('foo',))






