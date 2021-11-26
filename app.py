from flask import Flask, render_template, request, session, redirect, jsonify

from banktransfer import BankTransfer
from contract import Contract
from flask_session import Session
from flaskext.mysql import MySQL

from comment import Comment
from user import User
from homeinsurance import HomeInsurance
from motorinsurance import MotorInsurance
from yearlypayment import YearlyPayment

mysql = MySQL()

app = Flask(__name__, template_folder="templates")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'insurance_package'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

the_list = []  # a list of User objects


@app.route('/insurance')
def site():
    return render_template('home.html')


@app.route('/sign-up')
def signup():
    return render_template('sign_up.html')


@app.route('/logout')
def logout():
    # session.pop('login_username', None)
    session["login_username"] = None
    return redirect("insurance")


@app.route('/login')
def login():
    return render_template('login.html')


# ----------------API for Comment Starts ---------------------

@app.route('/getcomments', methods=['GET'])
def get_comments():
    if request.method == 'GET':
        con = mysql.connect()
        cur = con.cursor()
        cur.execute('SELECT * FROM comment')
        rows = cur.fetchall()
        con.commit()
        return jsonify(rows)


@app.route('/newcomment', methods=['POST'])
def new_comment():
    data = request.get_json(force=True)
    comment = data['name']
    con = mysql.connect()
    cur = con.cursor()
    cur.execute('INSERT INTO comment (name)VALUES( %s)', comment)
    con.commit()
    cur.close()
    con.close()
    return jsonify("Comment Added Successfully")


@app.route('/viewcomment', methods=['POST'])
def view_comment():
    data = request.get_json(force=True)
    id = data['id']
    con = mysql.connect()
    cur = con.cursor()
    cur.execute('SELECT * FROM comment WHERE id=%s', id)
    rows = cur.fetchall()
    con.commit()
    return jsonify(rows)


@app.route('/updatecomment', methods=['PUT'])
def update_comment():
    data = request.get_json(force=True)
    id = data['id']
    name = data['name']
    con = mysql.connect()
    cur = con.cursor()
    cur.execute('UPDATE comment SET name=%s WHERE id=%s', (name, id))
    con.commit()
    cur.close()
    con.close()
    return jsonify("Updated Comments Successfully")


@app.route('/deletecomment', methods=['DELETE'])
def delete_comment():
    data = request.get_json(force=True)
    id = data['id']
    con = mysql.connect()
    cur = con.cursor()
    cur.execute('DELETE FROM comment WHERE id=%s', id)
    con.commit()
    cur.close()
    con.close()
    return jsonify("Delete Comments Successfully")


# ----------------API for Comment Ends ---------------------


@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        rows = []
        try:
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            email = request.form['email']
            password = request.form['password']

            print("to check existing user")
            print(email)
            print(password)

            user = User()
            user.set_email(email)
            user.set_pass_word(password)

            cur.execute('SELECT username FROM member WHERE email=%s AND password=%s', (email, password))
            rows = cur.fetchall()
            rows_num = len(rows)
            print("Get  the user details")

            if rows_num == 0:
                return render_template("login.html")
            else:
                session["login_username"] = rows[0][0]
                return render_template("home.html")


        except:
            print("Check Email or password!!!!")
            con.rollback()


@app.route('/homedashboard')
def home_dashboard():
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    if session["login_username"] is not None:
        check = session["login_username"]
        cur.execute('SELECT * FROM home WHERE username=%s', check)
        check_new = cur.fetchall()
        check_num = len(check_new)

        return render_template('home_dashboard.html', check_num=check_num)
    else:
        return redirect('homenewinsurance')


@app.route('/motordashboard')
def motor_dashboard():
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    if session["login_username"] is not None:
        check = session["login_username"]
        cur.execute('SELECT * FROM motor WHERE username=%s', check)
        check_new = cur.fetchall()
        check_num = len(check_new)
        return render_template('motor_dashboard.html', check_num=check_num)
    else:
        return redirect('motornewinsurance')


@app.route('/motornewinsurance')
def motornewinsurance():
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    cur.execute('SELECT policy_name FROM policy WHERE policy_type="Motor"')
    policies = cur.fetchall()
    # con.commit()
    cur.execute('SELECT * FROM premium')
    premiums = cur.fetchall()
    # print(premiums)
    return render_template('new_motor_insurance.html', policies=policies, premiums=premiums)


# ------------------------------------------------------------------
@app.route('/viewhomeinsurance')
def view_home_insurance():
    rows = []
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    user_name = session["login_username"]

    #----------------  GoF Mediator  pattern -----------------------
    comment = Comment()
    comment.set_comment_name("Welcome " + user_name)
    comment_message = comment.send_message(" Your Home Insurance Details Registered as follows. "
                                           "Please check your mail for further procedures")
    # print(comment_message)
    # ----------------  GoF Mediator  pattern -----------------------

    # print('SELECT * FROM home WHERE username=%s', user_name)
    cur.execute('SELECT * FROM home WHERE username=%s', user_name)
    rows = cur.fetchall()
    con.commit()
    rows = rows
    # print(rows)
    return render_template('home_insurance_view.html', rows=rows, comment_message=comment_message)


# ----------------------------------------------------------------------
@app.route('/viewmotorinsurance')
def view_motor_insurance():
    rows = []
    rows_1 = []
    yearly_pay = 0.0  # monthly pay for GoF bridge pattern
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    user_name = session["login_username"]
    # print('SELECT * FROM motor WHERE username=%s', user_name)
    cur.execute('SELECT * FROM motor WHERE username=%s', user_name)
    rows = cur.fetchall()
    con.commit()
    rows = rows
    for row in rows:
        premium = row[8]
    cur.execute('SELECT price FROM premium WHERE name=%s', premium)
    rows_1 = cur.fetchall()
    con.commit()
    rows_1 = rows_1
    for row1 in rows_1:
        price = float(row1[0])
    print(price)

    homeinsurance = HomeInsurance()
    homeinsurance.set_contract(price)  # composition
    contract = Contract()
    contract.set_username(user_name)
    contract.set_pay(price)

    #---------------GoF Bridge pattern -----------------------------

    yearly_pay_api = YearlyPayment()  # yearly payment api
    bank_yearly = BankTransfer(price, yearly_pay_api)
    yearly_pay = bank_yearly.pay_out()
    print("calculate Yearly Payment For premiums")

    #---------------GoF Bridge pattern -----------------------------

    # print(rows)
    return render_template('motor_insurance_view.html', rows=rows, yearly_pay=yearly_pay)


@app.route('/homenewinsurance')
def homenewinsurance():
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    cur.execute('SELECT policy_name FROM policy WHERE policy_type="Home"')
    policies = cur.fetchall()
    # con.commit()
    cur.execute('SELECT * FROM premium')
    premiums = cur.fetchall()
    # print(premiums)
    return render_template('new_home_insurance.html', policies=policies, premiums=premiums)


@app.route('/homeupdateinsurance')
def update_homeinsurance():
    rows = []
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    user_name = session["login_username"]
    # print('SELECT * FROM home WHERE username=%s', user_name)
    cur.execute('SELECT * FROM home WHERE username=%s', user_name)
    rows = cur.fetchall()

    for row in rows:
        print("username: ", row[1])
        print("policy_name: ", row[2])
        print("address: ", row[3])
        print("built_date: ", row[4])
        print("home_type: ", row[5])
        print("home_age: ", row[6])
        print("membership_type: ", row[7])
        print("premium_selected: ", row[8])

    con.commit()
    rows = rows
    print(rows)

    cur.execute('SELECT policy_name FROM policy WHERE policy_type="Home"')
    policies = cur.fetchall()
    # con.commit()
    cur.execute('SELECT * FROM premium')
    premiums = cur.fetchall()
    print(premiums)
    housetypes = []
    housetypes = {"Single Floor", "Double Floor", "Flat"}
    housetypes = housetypes
    print(housetypes)
    membershiptypes = []
    membershiptypes = {"Individual", "Family"}
    membershiptypes = membershiptypes
    return render_template('update_home_insurance.html', rows=rows, policies=policies, premiums=premiums,
                           housetypes=housetypes, membershiptypes=membershiptypes)


@app.route('/motorupdateinsurance')
def update_motorinsurance():
    rows = []
    con = mysql.connect()  # set up database connection
    cur = con.cursor()
    user_name = session["login_username"]
    # print('SELECT * FROM motor WHERE username=%s', user_name)
    cur.execute('SELECT * FROM motor WHERE username=%s', user_name)
    rows = cur.fetchall()

    for row in rows:
        print("username: ", row[1])
        print("policy_name: ", row[2])

    con.commit()
    rows = rows
    # print(rows)

    cur.execute('SELECT policy_name FROM policy WHERE policy_type="Motor"')
    policies = cur.fetchall()
    # con.commit()
    cur.execute('SELECT * FROM premium')
    premiums = cur.fetchall()
    # print(premiums)

    return render_template('update_motor_insurance.html', rows=rows, policies=policies, premiums=premiums)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/checknewuser')
def check_newuser():
    return render_template("home.html")


# return render_template('home.html')


@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        rows = []
        user_info = ""
        try:
            print("--------------------------Demo Start----------------------------------------")
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            username = request.form['username']  # retrieve form data
            email = request.form['email']
            password1 = request.form['password1']
            password2 = request.form['password2']
            mobile = request.form['mobile']

            #----------------------  GoF composite pattern ------------

            user = User()
            user.set_user_name("Welcome New Insurance User !!!  " + username + "  Please login")
            user.add_subordinate(user)
            user_info = user.get_subordinate_names()

            # ----------------------  GoF composite pattern ------------

            print("to register a user")
            print(username)
            print(email)
            print(password1)
            print(mobile)
            print('INSERT INTO member (username, email, password, phone)'
                  'VALUES',
                  (username, email, password1, mobile))
            # user = User()
            user.set_user_name(username)
            user.set_email(email)
            user.set_pass_word(password1)
            user.set_mobile_number(mobile)

            cur.execute('SELECT * FROM user WHERE email=%s', email)
            r1 = cur.fetchall()
            r1_num = len(r1)
            print(r1_num)
            con.commit()

            insert_stmt = (
                "INSERT INTO member (username, email, password, phone)"
                "VALUES (%s, %s, %s, %s)"
            )
            data = (username, email, password1, mobile)
            cur.execute(insert_stmt, data)

            con.commit()
            print("write to the member table")

            # return render_template("login.html")

        except:
            con.rollback()

        finally:
            rows = rows
            return render_template("login.html", rows=rows, user_info=user_info)
            con.close()


@app.route('/register_home_insurance', methods=['POST', 'GET'])
def register_home_insurance():
    if request.method == 'POST':
        rows = []
        try:
            print("--------------------------Demo Start----------------------------------------")
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            username = request.form['username']  # retrieve form data
            policy = request.form['policy']
            address = request.form['address']
            built_date = request.form['built_date']
            home_type = request.form['home_type']
            home_age = request.form['home_age']
            membership_type = request.form['membership_type']
            premium_selected = request.form['premium_selected']

            print("to register a new home insurane")

            homeinsurance = HomeInsurance()
            homeinsurance.set_user_name(username)
            homeinsurance.set_policy_name(policy)
            homeinsurance.set_address(address)
            homeinsurance.set_built_date(built_date)
            homeinsurance.set_home_type(home_type)
            homeinsurance.set_home_age(home_age)
            homeinsurance.set_membership_type(membership_type)
            homeinsurance.set_premium_selected(premium_selected)

            insert_stmt = (
                "INSERT INTO home (username, policy_name, address, built_date, home_type, home_age, "
                "membership_type, premium_selected) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            data = (username, policy, address, built_date, home_type, home_age, membership_type, premium_selected)
            cur.execute(insert_stmt, data)

            con.commit()
            # print("write to the home table")
            if session["login_username"] != None:
                return redirect('checknewuser')
            else:
                return redirect('homedashboard')
            # return render_template("/home_dashboard.html")
        except:
            con.rollback()

        # finally:
        #     rows = rows
        #     return render_template("home.html", rows=rows)
        #     con.close()


@app.route('/register_motor_insurance', methods=['POST', 'GET'])
def register_motor_insurance():
    if request.method == 'POST':
        rows = []
        try:
            print("--------------------------Start----------------------------------------")
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            username = request.form['username']  # retrieve form data
            policy = request.form['policy']
            manufacturer = request.form['manufacturer']
            model = request.form['model']
            colour = request.form['colour']
            registration_year = request.form['registration_year']
            registration_number = request.form['registration_number']
            premium_selected = request.form['premium_selected']

            print("to register a motor insurance")
            print(username)
            print(policy)

            motorinsurance = MotorInsurance()
            motorinsurance.set_user_name(username)
            motorinsurance.set_policy_name(policy)
            motorinsurance.set_manufacturer(manufacturer)
            motorinsurance.set_model(model)
            motorinsurance.set_colour(colour)
            motorinsurance.set_registration_year(registration_year)
            motorinsurance.set_registration_number(registration_number)
            motorinsurance.set_premium_selected(premium_selected)

            insert_stmt = (
                "INSERT INTO motor (username, policy_name, manufacturer, model, colour, registration_year, "
                "registration_number, premium_selected) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            data = (
                username, policy, manufacturer, model, colour, registration_year, registration_number, premium_selected)
            cur.execute(insert_stmt, data)

            con.commit()
            # print("write to the motor table")
            if session["login_username"] is not None:
                return redirect('checknewuser')
            else:
                return redirect('homedashboard')


        except:
            con.rollback()

        # finally:
        #     rows = rows
        #     return render_template("home.html", rows=rows)
        #     con.close()


@app.route('/update_home_insurance', methods=['POST', 'GET'])
def update_home_insurance():
    if request.method == 'POST':
        rows = []
        try:
            print("-------------------------- Start----------------------------------------")
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            username = request.form['username']  # retrieve form data
            policy = request.form['policy']
            address = request.form['address']
            built_date = request.form['built_date']
            home_type = request.form['home_type']
            home_age = request.form['home_age']
            membership_type = request.form['membership_type']
            premium_selected = request.form['premium_selected']

            print("to update home insurance")
            print(username)
            print(policy)

            update_stmt = (
                "UPDATE home SET policy_name=%s, address=%s, built_date=%s, home_type=%s, home_age=%s, "
                "membership_type=%s, premium_selected=%s WHERE username=%s "
            )
            print(update_stmt)
            data = (policy, address, built_date, home_type, home_age, membership_type, premium_selected, username)
            cur.execute(update_stmt, data)
            rows = cur.fetchall()
            con.commit()
            # print("Updated the home table")
            return redirect('homedashboard')

        except:
            con.rollback()


@app.route('/update_motor_insurance', methods=['POST', 'GET'])
def update_motor_insurance():
    if request.method == 'POST':
        rows = []
        try:
            print("-------------------------- Start----------------------------------------")
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            username = request.form['username']  # retrieve form data
            policy = request.form['policy']
            manufacturer = request.form['manufacturer']
            model = request.form['model']
            colour = request.form['colour']
            registration_year = request.form['registration_year']
            registration_number = request.form['registration_number']
            premium_selected = request.form['premium_selected']

            print("to register a user")
            print(username)
            print(policy)

            update_stmt = (
                "UPDATE motor SET policy_name=%s, manufacturer=%s, model=%s, colour=%s, registration_year=%s, "
                "registration_number=%s, premium_selected=%s WHERE username=%s "
            )
            print(update_stmt)
            data = (
                policy, manufacturer, model, colour, registration_year, registration_number, premium_selected, username)
            cur.execute(update_stmt, data)
            rows = cur.fetchall()
            con.commit()
            print("Updated the motor table")
            return redirect('motordashboard')

        except:
            con.rollback()


@app.route('/homedelete')
def home_delete():
    username = session["login_username"]
    con = mysql.connect()
    cur = con.cursor()

    cur.execute('DELETE FROM home WHERE username=%s', username)
    con.commit()
    print("delete the user from the home table")
    return redirect('homedashboard')


@app.route('/motordelete')
def motor_delete():
    username = session["login_username"]
    con = mysql.connect()
    cur = con.cursor()

    cur.execute('DELETE FROM motor WHERE username=%s', username)
    con.commit()
    print("delete the user from the motor table")
    return redirect('motordashboard')


if __name__ == "__main__":
    app.run()
