"""
The example is based on https://www.flaskapi.org/ with modification
"""

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flaskext.mysql import MySQL
mysql = MySQL()
app = FlaskAPI(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'insurance_package'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config["DEBUG"] = True
mysql.init_app(app)

comments = {}


def comment_get_all():
    con = mysql.connect()
    cur = con.cursor()
    cur.execute('SELECT * FROM comment')
    rows = cur.fetchall()
    for row in rows:
        index = row[0]  # assign to key
        name = row[1]  # assign to comment name
        comments[index] = name
    con.commit()
    cur.close()
    con.close()
    return comments
    print("comments: " + str(len(comments)))


def comment_display(key):
    return {
        'all': request.host_url.rstrip('/api/resources/comments'),  # link to all comments
        'link': request.host_url.rstrip('/api/resources/comments') + url_for('comments_detail', key=key),
        'comment': comments[key]
    }


@app.route("/", methods=['GET', 'POST'])
def comments_list():
    """
    List or create comments.
    """
    if request.method == 'POST':
        con = mysql.connect()
        cur = con.cursor()
        comment = str(request.data.get('comment', ''))
        index = len(comments.keys()) + 1
        comments[index] = comment
        cur.execute('INSERT INTO comment (id, name)VALUES( %s, %s)', (index, comment))
        con.commit()
        print("add a new comment to the table")
        return comment_display(index), status.HTTP_201_CREATED
        cur.close()
        con.close()
    elif request.method == 'GET':
        comment_get_all()
        return [comment_display(index) for index in sorted(comments.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def comments_detail(key):
    """
    Retrieve, update or delete comments instances.
    """
    con = mysql.connect()
    cur = con.cursor()
    request.host_url.rstrip('/')
    if request.method == 'PUT':
        name = str(request.data.get('comment', ''))
        comments[key] = name
        cur.execute('UPDATE comment SET name=%s WHERE id=%s', (name, key))
        con.commit()
        print("update the comment table")
        return comment_display(key)

    elif request.method == 'DELETE':
        comments.pop(key, None)
        cur.execute('DELETE FROM comment WHERE id=%s', key)
        con.commit()
        print("delete the comment from the table")
        if len(comments) ==0:
            return request.host_url.rstrip('/api/resources/comments')
        else:
            return [comment_display(index) for index in sorted(comments.keys())], status.HTTP_204_NO_CONTENT

    elif request.method == 'GET':
        if key not in comments:
            raise exceptions.NotFound()
            comment_get_all()
        else:
            return comment_display(key)

    cur.close()
    con.close()


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
