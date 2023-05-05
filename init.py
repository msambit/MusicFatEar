#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
from flask_bcrypt import Bcrypt
import pymysql.cursors
from datetime import date, datetime

#for uploading photo:
from app import app

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


###Initialize the app from Flask
app = Flask(__name__)
bcrypt = Bcrypt(app)
##app.secret_key = "secret key"

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       port = 3306,
                       user='root',
                       password='root',
                       db='sys',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

 
def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
    return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
    return render_template('register.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    
    #cursor used to send queries
    cursor = conn.cursor()
    
    #executes query
    query = 'SELECT * FROM user WHERE username = %s'
    
    cursor.execute(query, (username))
    
    #stores the results in a variable
    data = cursor.fetchone()
    
    #use fetchall() if you are expecting more than 1 data row
    
    cursor.close()
    error = None
    
    if(data):
        
        if(bcrypt.check_password_hash(data['pwd'].encode('utf-8'), password)):
            #creates a session for the the user
            #session is a built in
            session['username'] = username
            return redirect(url_for('home'))
        else:
            #returns an error message to the html page
            error = 'Invalid username or password'
            return render_template('login.html', error=error)        
    else:
        #returns an error message to the html page
        error = 'Invalid username or password'
        return render_template('login.html', error=error)

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    fname = request.form['fname']
    lname = request.form['lname']
    nickname = request.form['nickname']
    lastlogin = date.today().strftime('%Y-%m-%d')

    #Hashing password
    pwd = bcrypt.generate_password_hash(password).decode('utf-8')
    
    #cursor used to send queries
    cursor = conn.cursor()
    
    #executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        if(nickname is None):
            ins = 'INSERT INTO user (username, pwd, fname, lname, lastlogin) VALUES(%s, %s, %s, %s, %s)'
            cursor.execute(ins, (username, pwd, fname, lname, lastlogin))
        else:
            ins = 'INSERT INTO user (username, pwd, fname, lname, lastlogin, nickname) VALUES(%s, %s, %s, %s, %s, %s)'
            cursor.execute(ins, (username, pwd, fname, lname, lastlogin,nickname))
        conn.commit()
        cursor.close()
        return render_template('index.html')
    
#Search / Browse Music 
@app.route('/indexSearch', methods=['GET', 'POST'])
def indexSearch():
    
    #grabs information from the forms
    category = request.form.get('token')
    searchToken = request.form['searchToken']
    avgRating = request.form['rating']
    artistFname = request.form['artistFname']
    artistLname = request.form['artistLname']
    
    #cursor used to send queries
    cursor = conn.cursor()
    
    if(category == "Songs"):
       
        searchToken = "%" + searchToken + "%"
        rating = False
        query = 'SELECT * FROM song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE title LIKE %s'
        var = (searchToken,)
        if(len(avgRating) > 0):
            rating = True
            query1 = 'SELECT * FROM songrating NATURAL JOIN song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE title LIKE %s'
            var = var + (avgRating,)
            query = query1 + " AND avgStars >= %s"
        if(len(artistFname) > 0 or len(artistLname) > 0):
            if(len(artistFname) > 0):
                artistFname = "%" + artistFname + "%"
                var = var + (artistFname,)
                query = query + " AND fname LIKE %s"
            if(len(artistLname) > 0):
                artistLname = "%" + artistLname + "%"
                var = var + (artistLname,)
                query = query + " AND lname LIKE %s"
        
        cursor.execute(query, var)
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('index.html', songs=data, rating=rating)       
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('index.html', error=error)
        
    elif(category == "Artist"):
        
        searchToken = "%" + searchToken + "%"
        query = 'SELECT * FROM song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE (fname LIKE %s || lname LIKE %s)'
        cursor.execute(query, (searchToken, searchToken))
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('index.html', artists=data)        
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('index.html', error=error)
    else:
        
        rating = False
        searchToken = "%" + searchToken + "%"
        query = 'SELECT * FROM songinalbum NATURAL JOIN song NATURAL JOIN songgenre WHERE genre LIKE %s'
        var = (searchToken,)
        if(len(avgRating) > 0):
            rating = True
            query1 = 'SELECT * FROM albumRating NATURAL JOIN songinalbum NATURAL JOIN song NATURAL JOIN songgenre WHERE genre LIKE %s'
            var = var + (str(avgRating),)
            query = query1 + " AND avgStars >= %s"
        
        cursor.execute(query, var)
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('index.html', albums=data, rating=rating)        
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('index.html', error=error)

#Search / Browse Music 
@app.route('/indexSearchHome', methods=['GET', 'POST'])
def indexSearchHome():
    user = session['username']
    #grabs information from the forms
    category = request.form.get('token')
    searchToken = request.form['searchToken']
    avgRating = request.form['rating']
    artistFname = request.form['artistFname']
    artistLname = request.form['artistLname']
    
    #cursor used to send queries
    cursor = conn.cursor()
    
    if(category == "Songs"):
       
        searchToken = "%" + searchToken + "%"
        rating = False
        query = 'SELECT * FROM song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE title LIKE %s'
        var = (searchToken,)
        if(len(avgRating) > 0):
            rating = True
            query1 = 'SELECT * FROM songrating NATURAL JOIN song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE title LIKE %s'
            var = var + (avgRating,)
            query = query1 + " AND avgStars >= %s"
        if(len(artistFname) > 0 or len(artistLname) > 0):
            if(len(artistFname) > 0):
                artistFname = "%" + artistFname + "%"
                var = var + (artistFname,)
                query = query + " AND fname LIKE %s"
            if(len(artistLname) > 0):
                artistLname = "%" + artistLname + "%"
                var = var + (artistLname,)
                query = query + " AND lname LIKE %s"
        
        cursor.execute(query, var)
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('home.html', songs=data, rating=rating, username=user)       
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('home.html', error=error, username=user)
        
    elif(category == "Artist"):
        
        searchToken = "%" + searchToken + "%"
        query = 'SELECT * FROM song NATURAL JOIN artistperformssong NATURAL JOIN artist WHERE (fname LIKE %s || lname LIKE %s)'
        cursor.execute(query, (searchToken, searchToken))
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('home.html', artists=data, username=user)        
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('home.html', error=error, username=user)
    else:
        
        rating = False
        searchToken = "%" + searchToken + "%"
        query = 'SELECT * FROM songinalbum NATURAL JOIN song NATURAL JOIN songgenre WHERE genre LIKE %s'
        var = (searchToken,)
        if(len(avgRating) > 0):
            rating = True
            query1 = 'SELECT * FROM albumRating NATURAL JOIN songinalbum NATURAL JOIN song NATURAL JOIN songgenre WHERE genre LIKE %s'
            var = var + (str(avgRating),)
            query = query1 + " AND avgStars >= %s"
        
        cursor.execute(query, var)
        
        #stores the results in a variable
        data = cursor.fetchall()
        cursor.close()
        error = None
        if(data):
            return render_template('home.html', albums=data, rating=rating, username=user)        
        else:
            #returns an error message to the html page
            error = 'Nothing found with the given search parameters'
            return render_template('home.html', error=error, username=user)


@app.route('/home')
def home():
    user = session['username']
    return render_template('home.html', username=user)

#Define route for register
@app.route('/recentActivity')
def recentActivity():
    user = session['username']
    cursor = conn.cursor();
    
    #executes query
    query = 'SELECT * FROM user WHERE username = %s'
    
    cursor.execute(query, (user))
    
    #stores the results in a variable
    data = cursor.fetchone()
    lastDate = data['lastlogin']
    
    querySongReviews = 'SELECT * FROM user NATURAL JOIN reviewsong NATURAL JOIN song WHERE reviewDate > %s AND (username IN ( SELECT DISTINCT user1 FROM friend WHERE user2 = %s AND acceptStatus = "Accepted") \
                        OR username IN ( SELECT DISTINCT user2 FROM friend WHERE user1 = %s AND acceptStatus = "Accepted") \
                        OR username IN ( SELECT DISTINCT follows FROM follows WHERE follower = %s))'
    cursor.execute(querySongReviews, (lastDate,user,user,user))
    dataSong = cursor.fetchall()
    errorSong  = None
    if(not dataSong):
        errorSong = "No recent reviews of songs after your last login"
    
    queryAlbumReviews = 'SELECT * FROM user NATURAL JOIN reviewalbum WHERE reviewDate > %s AND (username IN ( SELECT DISTINCT user1 FROM friend WHERE user2 = %s AND acceptStatus = "Accepted") \
                        OR username IN ( SELECT DISTINCT user2 FROM friend WHERE user1 = %s AND acceptStatus = "Accepted") \
                        OR username IN ( SELECT DISTINCT follows FROM follows WHERE follower = %s))'
    cursor.execute(queryAlbumReviews, (lastDate,user,user,user))
    dataAlbum = cursor.fetchall()
    errorAlbum  = None
    if(not dataAlbum):
        errorAlbum = "No recent reviews of albums after your last login"
    
    queryFanSongs = 'SELECT * FROM userfanofartist NATURAL JOIN artistperformssong NATURAL JOIN song  NATURAL JOIN artist WHERE releaseDate > %s AND username = %s'
    cursor.execute(queryFanSongs, (lastDate,user))
    dataFanSongs = cursor.fetchall()
    errorFanSongs  = None
    if(not dataFanSongs):
        errorFanSongs = "No new songs of Artists you are fan of after your last login"
    cursor.close()
    
    if(errorSong is None and errorAlbum is None and errorFanSongs is None):
        return render_template('recentActivity.html', username=user, dataSong=dataSong, dataAlbum=dataAlbum, dataFanSongs=dataFanSongs)
    elif(errorSong is None and errorAlbum is None):
        return render_template('recentActivity.html', username=user, dataSong=dataSong, dataAlbum=dataAlbum, errorFanSongs=errorFanSongs)
    elif(errorSong is None and errorFanSongs is None):
        return render_template('recentActivity.html', username=user, dataSong=dataSong, errorAlbum=errorAlbum, dataFanSongs=dataFanSongs)
    elif(errorAlbum is None and errorFanSongs is None):
        return render_template('recentActivity.html', username=user, errorSong=errorSong, dataAlbum=dataAlbum, dataFanSongs=dataFanSongs)
    elif(errorSong is None):
        return render_template('recentActivity.html', username=user, dataSong=dataSong, errorAlbum=errorAlbum, errorFanSongs=errorFanSongs)
    elif(errorAlbum is None):
        return render_template('recentActivity.html', username=user, errorSong=errorSong, dataAlbum=dataAlbum, errorFanSongs=errorFanSongs)
    elif(errorFanSongs is None):
        return render_template('recentActivity.html', username=user, errorSong=errorSong, errorAlbum=errorAlbum, dataFanSongs=dataFanSongs)
    else:
        return render_template('recentActivity.html', username=user, errorSong=errorSong, errorAlbum=errorAlbum, errorFanSongs=errorFanSongs)

#Define route for register
@app.route('/myActivity')
def myActivity():
    user = session['username']
    
    cursor = conn.cursor();
    
    querySongReviews = 'SELECT * FROM user NATURAL JOIN reviewsong NATURAL JOIN song WHERE username = %s LIMIT 10'
    cursor.execute(querySongReviews, (user))
    dataSong = cursor.fetchall()
    errorSong  = None
    if(not dataSong):
        errorSong = "No song reviews"
    
    queryAlbumReviews = 'SELECT * FROM user NATURAL JOIN reviewalbum WHERE username = %s LIMIT 10'
    cursor.execute(queryAlbumReviews, (user))
    dataAlbum = cursor.fetchall()
    errorAlbum  = None
    if(not dataAlbum):
        errorAlbum = "No album reviews"
        
    cursor.close()
    
    if(errorSong is None and errorAlbum is None):
        return render_template('myActivity.html', username=user, dataSong=dataSong, dataAlbum=dataAlbum)
    elif(errorSong is None):
        return render_template('myActivity.html', username=user, dataSong=dataSong, errorAlbum=errorAlbum)
    elif(errorAlbum is None):
        return render_template('myActivity.html', username=user, errorSong=errorSong, dataAlbum=dataAlbum)
    else:
        return render_template('myActivity.html', username=user, errorSong=errorSong, errorAlbum=errorAlbum)

#Define route for register
@app.route('/social')
def social():
    user = session['username']
    
    cursor = conn.cursor();
    
    queryFriends = 'SELECT DISTINCT fname, lname FROM user WHERE username IN ( SELECT DISTINCT user1 FROM friend \
                        WHERE user2 = %s AND acceptStatus = "Accepted") OR username IN ( SELECT DISTINCT user2 FROM friend \
				        WHERE user1 = %s AND acceptStatus = "Accepted")'
    cursor.execute(queryFriends, (user,user))
    dataFriends = cursor.fetchall()
    errorFriends  = None
    if(not dataFriends):
        errorFriends = "No friends"
    
    queryFollowers = 'SELECT DISTINCT fname, lname FROM user WHERE username IN ( SELECT DISTINCT follower FROM follows WHERE follows = %s)'
    cursor.execute(queryFollowers, (user))
    dataFollowers = cursor.fetchall()
    errorFollowers  = None
    if(not dataFollowers):
        errorFollowers = "No followers"
    
    queryFollowing = 'SELECT DISTINCT fname, lname FROM user WHERE username IN ( SELECT DISTINCT follows FROM follows WHERE follower = %s)'
    cursor.execute(queryFollowing, (user))
    dataFollowing = cursor.fetchall()
    errorFollowing  = None
    if(not dataFollowing):
        errorFollowing = "No following"
    cursor.close()
    
    if(errorFriends is None and errorFollowers is None and errorFollowing is None):
        return render_template('social.html', username=user, dataFriends=dataFriends, dataFollowers=dataFollowers, dataFollowing=dataFollowing)
    elif(errorFriends is None and errorFollowers is None):
        return render_template('social.html', username=user, dataFriends=dataFriends, dataFollowers=dataFollowers, errorFollowing=errorFollowing)
    elif(errorFriends is None and errorFollowing is None):
        return render_template('social.html', username=user, dataFriends=dataFriends, errorFollowers=errorFollowers, dataFollowing=dataFollowing)
    elif(errorFollowers is None and errorFollowing is None):
        return render_template('social.html', username=user, errorFriends=errorFriends, dataFollowers=dataFollowers, dataFollowing=dataFollowing)
    elif(errorFriends is None):
        return render_template('social.html', username=user, dataFriends=dataFriends, errorFollowers=errorFollowers, errorFollowing=errorFollowing)
    elif(errorFollowers is None):
        return render_template('social.html', username=user, errorFriends=errorFriends, dataFollowers=dataFollowers, errorFollowing=errorFollowing)
    elif(errorFollowing is None):
        return render_template('social.html', username=user, errorFriends=errorFriends, errorFollowers=errorFollowers, dataFollowing=dataFollowing)
    else:
        return render_template('social.html', username=user, errorFriends=errorFriends, errorFollowers=errorFollowers, errorFollowing=errorFollowing)

#Define route for register
@app.route('/requests')
def requests():
    user = session['username']
    
    cursor = conn.cursor();
    
    query = 'SELECT DISTINCT * FROM user WHERE username IN ( SELECT DISTINCT user1 FROM friend \
                        WHERE user2 = %s AND acceptStatus = "Pending");'
    cursor.execute(query, (user))
    data = cursor.fetchall()
    cursor.close()
    error  = None
    if(data):
        return render_template('requests.html', username=user, data=data)
    else:
        error="No Pending Requests"
        return render_template('requests.html', username=user, error=error)

#Define route for register
@app.route('/resolveRequest', methods=['GET', 'POST'])
def resolveRequest():
    user = session['username']
    userId = request.form.get('token')
    decision = request.form.get('decision')
    datenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor();
    
    query = 'UPDATE friend SET acceptStatus = %s, updatedAt = %s WHERE user1 = %s AND user2 = %s'
    cursor.execute(query, (decision,datenow,userId,user))
    conn.commit()
    cursor.close()
    return redirect('/requests')

#Define route for register
@app.route('/sendRequest')
def sendRequest():
    user = session['username']
    
    cursor = conn.cursor();
    
    query = 'SELECT DISTINCT * FROM user WHERE username NOT IN ( SELECT DISTINCT user1 FROM friend WHERE user2 = %s AND acceptStatus IN ("Accepted","Pending","Not accepted")) \
            AND username NOT IN ( SELECT DISTINCT user2 FROM friend WHERE user1 = %s AND acceptStatus IN ("Accepted","Pending","Not accepted"))'
    cursor.execute(query, (user,user))
    data = cursor.fetchall()
    cursor.close()
    error  = None
    if(data):
        return render_template('sendRequest.html', username=user, data=data)
    else:
        error="No Users Remaining"
        return render_template('sendRequest.html', username=user, error=error)

#Define route for register
@app.route('/resolveSendRequest', methods=['GET', 'POST'])
def resolveSendRequest():
    user = session['username']
    userId = request.form.get('token')
    datenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor();
    
    query = 'INSERT INTO friend (user1, user2, acceptStatus, requestSentBy, createdAt, updatedAt) VALUES \
            (%s, %s, "Pending", %s, %s, %s)'
    cursor.execute(query, (user,userId,user,datenow,datenow))
    conn.commit()
    cursor.close()
    return redirect('/sendRequest')

#Define route for register
@app.route('/rateReviewMusic')
def rateReviewMusic():
    user = session['username']
    
    cursor = conn.cursor();
    
    query = 'SELECT * FROM song'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    error  = None
    if(data):
        return render_template('rateReviewMusic.html', username=user, data=data)
    else:
        error="No Songs"
        return render_template('rateReviewMusic.html', username=user, error=error)


@app.route('/rateSong', methods=['GET', 'POST'])
def rateSong():
    user = session['username']
    songId = request.form.get('token')
    rating = request.form['rating']
    dateToday = date.today().strftime('%Y-%m-%d')
    
    cursor = conn.cursor();
    queryX = 'SELECT * FROM rateSong WHERE username = %s AND songID = %s'
    cursor.execute(queryX, (user,songId))
    dataX = cursor.fetchone()
    
    if(dataX):
        query = 'UPDATE rateSong SET stars = %s, ratingDate = %s WHERE username = %s AND songID = %s'
        cursor.execute(query, (rating,dateToday,user,songId))
        conn.commit()
    else:
        query = 'INSERT INTO rateSong (username, songID, stars, ratingDate) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (user,songId,rating,dateToday))
        conn.commit()
    cursor.close()
    return redirect('/rateReviewMusic')

@app.route('/reviewSong', methods=['GET', 'POST'])
def reviewSong():
    user = session['username']
    songId = request.form.get('token')
    review = request.form['review']
    dateToday = date.today().strftime('%Y-%m-%d')
    
    cursor = conn.cursor();
    queryX = 'SELECT * FROM reviewSong WHERE username = %s AND songID = %s'
    cursor.execute(queryX, (user,songId))
    dataX = cursor.fetchone()
    
    if(dataX):
        query = 'UPDATE reviewSong SET reviewText = %s, reviewDate = %s WHERE username = %s AND songID = %s'
        cursor.execute(query, (review,dateToday,user,songId))
        conn.commit()
    else:
        query = 'INSERT INTO reviewSong (username, songID, reviewText, reviewDate) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (user,songId,review,dateToday))
        conn.commit()
    cursor.close()
    return redirect('/rateReviewMusic')

#Define route for register
@app.route('/rateReviewAlbum')
def rateReviewAlbum():
    user = session['username']
    
    cursor = conn.cursor();
    
    query = 'SELECT * FROM album'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    error  = None
    if(data):
        return render_template('rateReviewAlbum.html', username=user, data=data)
    else:
        error="No Albums"
        return render_template('rateReviewAlbum.html', username=user, error=error)


@app.route('/rateAlbum', methods=['GET', 'POST'])
def rateAlbum():
    user = session['username']
    albumID = request.form.get('token')
    rating = request.form['rating']
    
    cursor = conn.cursor();
    queryX = 'SELECT * FROM rateAlbum WHERE username = %s AND albumID = %s'
    cursor.execute(queryX, (user,albumID))
    dataX = cursor.fetchone()
    
    if(dataX):
        query = 'UPDATE rateAlbum SET stars = %s WHERE username = %s AND albumID = %s'
        cursor.execute(query, (rating,user,albumID))
        conn.commit()
    else:
        query = 'INSERT INTO rateAlbum (username, albumID, stars) VALUES (%s, %s, %s)'
        cursor.execute(query, (user,albumID,rating))
        conn.commit()
    cursor.close()
    return redirect('/rateReviewAlbum')

@app.route('/reviewAlbum', methods=['GET', 'POST'])
def reviewAlbum():
    user = session['username']
    albumID = request.form.get('token')
    review = request.form['review']
    dateToday = date.today().strftime('%Y-%m-%d')
    
    cursor = conn.cursor();
    queryX = 'SELECT * FROM reviewAlbum WHERE username = %s AND albumID = %s'
    cursor.execute(queryX, (user,albumID))
    dataX = cursor.fetchone()
    
    if(dataX):
        query = 'UPDATE reviewAlbum SET reviewText = %s, reviewDate = %s WHERE username = %s AND albumID = %s'
        cursor.execute(query, (review,dateToday,user,albumID))
        conn.commit()
    else:
        query = 'INSERT INTO reviewAlbum (username, albumID, reviewText, reviewDate) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (user,albumID,review,dateToday))
        conn.commit()
    cursor.close()
    return redirect('/rateReviewAlbum')
    
@app.route('/logout')
def logout():
    username = session['username']
    lastlogin = date.today().strftime('%Y-%m-%d')
    
    #cursor used to send queries
    cursor = conn.cursor()
    
    #executes query
    query = 'UPDATE user SET lastlogin = %s WHERE username = %s'
    
    cursor.execute(query, (lastlogin,username))
    conn.commit()
    cursor.close()
    
    session.pop('username')
    return render_template('index.html')
        
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
