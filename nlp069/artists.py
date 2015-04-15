from flask import Flask, g, request, render_template
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def show_list():
    artists = []
    artist = alias = tag = ""

    if request.method == 'POST':
        artist = request.form.get('artist', None)
        alias = request.form.get('alias', None)
        tag = request.form.get('tag', None)
        artists = search(artist=artist, alias=alias, tag=tag)

    return render_template('list.html', artist=artist,
                           alias=alias, tag=tag, artists=artists)

def search(artist=None, alias=None, tag=None):
    q = {}
    if artist: q["name"] = artist
    if alias: q["aliases.name"] = alias
    if tag: q["tags.value"] = tag

    # TODO: order by, limit and pagination
    result = get_db().find(q).sort("rating.value", DESCENDING).limit(100)

    artists = []
    for r in result:
        #app.logger.debug(r)

        a = {}
        a["name"] = r.get("name", "NA")
        a["aliases"] = [ al.get("name", "") for al in r.get("aliases", []) ]
        a["tags"] = [ t.get("value", "") for t in r.get("tags", []) ]
        a["area"] = r.get("area", "NA")
        if r.get("rating"):
            rating = r.get("rating")
            a["rating"] = { "count": str(rating.get("count", "NA")), "value": str(rating.get("value", "NA")) }
        else:
            a["rating"] = {"count":"NA", "value":"NA"}
        artists.append(a)

    return artists

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        #db.close()
        pass

def connect_to_database():
    client = MongoClient()
    db = client.nlp
    coll = db.artists
    return coll

if __name__ == '__main__':
    app.run()
