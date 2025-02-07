import mysql.connector
from classes.database import HostConfig, ConfigPaths, ConnectParam
import os
from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, flash
from flask_mail import Mail, Message
from authentication.middleware import auth

adminlevelone_blueprint = Blueprint('adminlevelone', __name__)


def adminlevelone_auth(app, mail):
    # ------ HOST Configs are in classes/connection.py
    host = HostConfig.host
    app_paths = ConfigPaths.paths.get(host)
    if app_paths:
        for key, value in app_paths.items():
            app.config[key] = value

    @adminlevelone_blueprint.route('/adminPage', methods=['GET', 'POST'])
    def admin_level_1():
        if not session.get('logged_in'):
            # Redirect to the admin login page if the user is not logged in
            return redirect(url_for('adminlogin.admin_login'))

        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)

        if request.method == 'POST':
            # Check if a form was submitted
            if 'accept' in request.form:
                # Handle accepting an application
                applicant_id = request.form['accept']
                update_status_admin(applicant_id, 'accepted')
            elif 'reject' in request.form:
                # Handle rejecting an application
                applicant_id = request.form['reject']
                update_status_admin(applicant_id, 'rejected')
                cursor.execute("SELECT email, first_name, status FROM application_page WHERE applicant_id = %s",
                               (applicant_id,))
                user_data = cursor.fetchone()

                if user_data:
                    email = user_data[0]
                    full_name = f"{user_data[1]} {user_data[2]}"

                    send_email_rejection(email, full_name, 'Rejected', applicant_id)
            # Commit the changes to the database
            cnx.commit()

        cursor.execute("SELECT * FROM application_page where form_filled='1' and phd_registration_year>='2023' ")
        data = cursor.fetchall()
        # print(data)
        cursor.close()
        cnx.close()
        return render_template('AdminPages/AdminLevels/LevelOne/admin_level_one.html', data=data)

    def update_status_admin(applicant_id, status):
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)

        # Update the status for the specified applicant ID
        update_query = "UPDATE application_page SET status = %s WHERE applicant_id = %s"
        cursor.execute(update_query, (status, applicant_id))

        # Commit the changes to the database
        cnx.commit()

        # Close the cursor and database connection
        cursor.close()
        cnx.close()

    def send_email_rejection(email, full_name, status, applicant_id):
        # Email content in HTML format
        msg = Message('Application Status Changed', sender='helpdesk@trti-maha.in', recipients=[email])
        # msg.body = msg.body = "Hi, " + full_name + "\n Your Status for Fellowship : " + status + \
        #                       "\n Unfortunately the status of your application has changed to Rejected!!" + \
        #                       "\n Please login to view the status as Accepted for Fellowship" + \
        #                       "\n Your Application ID = " + applicant_id

        msg_body = f''' 
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap');


        </style>
    </head>

    <body style="background: radial-gradient(rgb(235,236,240),rgb(235,236,240)); padding: 50px;  margin: 0;  font-family: 'Montserrat', sans-serif;">

        <table style="width: 90%; margin: auto; min-width: 480px; border-radius: 10px; overflow: hidden; width: 540px; border-spacing: 0;">
            <tr style="background: #F5F5F5; border-radius: 10px; ">
                <td style="text-align: center;">
                    <img src="https://fellowship.trti-maha.in/static/assets/img/logo/logo-new.png" style="width: 80px;"
                        alt="TRTI logo">

                </td>
                <td style="text-align: center;">
                    <img src="https://fellowship.trti-maha.in/static/assets/img/fellow_logo_1.png" style="width: 70px;"
                        alt="Fellowship Logo">
                </td>
                <td style="text-align: center;">
                    <h3 style="color: #175E97; font-weight: 700; ">FELLOWSHIP</h3>
                </td>
                <td style="text-align: center;">
                    <h3 style="color: #B71540; font-weight: 600; font-size: 15px;">HOME</h3>
                </td>
                <td style="text-align: center;">
                    <h3 style="color: #B71540; font-weight: 600; font-size: 15px;">CONTACT US</h3>
                </td>
            </tr>
            <tr>
                <td colspan="5"
                    style="background: linear-gradient(rgba(169,27,96,0.4), rgba(169,27,96,0.4)), url('https://fellowship.trti-maha.in/static/assets/img/banner_award.jpg'); width: 100%; height: 30vh; background-size: cover; background-repeat: no-repeat;">
                    <h2
                        style="text-transform: uppercase; text-align: center; font-size: 50px; color: #fff; width: 90%; letter-spacing: 5px; margin: auto; ">
                        Thanks For Applying
                    </h2>
                </td>
            </tr>
            <tr>
                <td colspan="5" style="background: #fff; padding: 40px;">
                    <h4
                        style="text-transform: uppercase; text-align: center; font-size: 20px; font-weight: 600; color: #A91B60;">
                        Hello, {full_name}</h4>
                    <h4
                        style="text-transform: uppercase; text-align: center; font-size: 18px; font-weight: 600; color: #A91B60; line-height: 28px;">
                        Your Status for Fellowship : {status}
                        Unfortunately the status of your application has changed to Rejected!!
                    </h4>
                    <h4
                        style="text-transform: uppercase; text-align: center; font-size: 18px; font-weight: 600; color: #A91B60; line-height: 28px;">
                        Please Login To View The Status As Rejected For Fellowship
                    </h4>
                    <h4
                        style="text-transform: uppercase; text-align: center; font-size: 18px; font-weight: 600; color: #A91B60; line-height: 28px;">
                        Your Application ID:</h4>
                    <p
                        style="text-align: center; padding: 25px; border: 3px solid #ECB322; color: #ECB322; font-weight: 700; letter-spacing: 10px; font-size: 20px;">{applicant_id}</p>
                </td>
            </tr>
            <tr>
                <td colspan="5" style="background: #fff; padding: 40px; border-top: 1px solid rgb(235,236,240);">
                    <h4
                        style="text-transform: uppercase; text-align: center; font-size: 12px; font-weight: 600; color: #A91B60; line-height: 18px;">
                        In case of any technical issue while filling online application form, please contact on toll free
                        helpline number 18002330444 (From 09:45 AM to 06:30 PM </h4>
                    <p style="color:#A91B60; font-size: 11px; font-weight: 600; text-align: center;">
                        This is a system generated mail. Please do not reply to this Email ID
                    </p>
                </td>
            </tr>
            <tr>
                <td colspan="5" style="background: #A91B60; padding: 10px 40px; ">
                    <span style="color: #fff; font-size: 11px; ">Visit us at <a href="https://trti.maharashtra.gov.in"
                            target="_blank" style="color: #fff;">https://trti.maharashtra.gov.in</a> </span>
                    <img src="https://static.vecteezy.com/system/resources/thumbnails/027/395/710/small/twitter-brand-new-logo-3-d-with-new-x-shaped-graphic-of-the-world-s-most-popular-social-media-free-png.png" style="width: 32px; height: 32px; float: right; " alt="Twitter Logo">
                    <img src="https://cdn3.iconfinder.com/data/icons/social-network-30/512/social-06-512.png"
                        style="width: 32px;  height: 32px;  float: right; margin-right: 12px; background: transparent;"
                        alt="Youtube Logo">
                    <img src="https://freelogopng.com/images/all_img/1658030214facebook-logo-hd.png"
                        style="width: 32px; height: 32px; float: right; margin-right: 12px; " alt="Facebok Logo">
                </td>
            </tr>
        </table>

    </body>

    </html> 
    '''
        msg = Message('Application Status Changed', sender='noreply_fellowship@trti-maha.in', recipients=[email])
        msg.html = msg_body
        mail.send(msg)

    @adminlevelone_blueprint.route('/disabled_students_level1')
    def disabled_students_level1():
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)
        cursor.execute(
            " SELECT * FROM application_page WHERE phd_registration_year>='2023' and disability='Yes' "
        )
        result = cursor.fetchall()
        return render_template('AdminPages/AdminLevels/LevelOne/disabled_students_level1.html', result=result)

    @adminlevelone_blueprint.route('/rejected_students_level1')
    def rejected_students_level1():
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)
        cursor.execute(" SELECT * FROM application_page WHERE phd_registration_year>='2023' and status='rejected' ")
        result = cursor.fetchall()

        return render_template('AdminPages/AdminLevels/LevelOne/rejected_students_level1.html', result=result)

    @adminlevelone_blueprint.route('/pvtg_students_level1')
    def pvtg_students_level1():
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)
        cursor.execute(
            " SELECT * FROM application_page WHERE phd_registration_year>='2023' and"
            " your_caste IN ('katkari', 'kolam', 'madia') "
        )
        result = cursor.fetchall()
        return render_template('AdminPages/AdminLevels/LevelOne/pvtg_students_level1.html', result=result)

    @adminlevelone_blueprint.route('/accepted_students_level1', methods=['GET', 'POST'])
    def accepted_students_level1():
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)

        cursor.execute(" SELECT * FROM application_page WHERE phd_registration_year>='2023' and status='accepted' ")
        result = cursor.fetchall()
        # print(result)
        return render_template('AdminPages/AdminLevels/LevelOne/accepted_students_level1.html', result=result)

    @adminlevelone_blueprint.route('/pending_students_level1', methods=['GET', 'POST'])
    def pending_students_level1():
        host = HostConfig.host
        connect_param = ConnectParam(host)
        cnx, cursor = connect_param.connect(use_dict=True)
        cursor.execute(" SELECT * FROM application_page WHERE phd_registration_year>='2023' and status='pending' ")
        result = cursor.fetchall()
        # print('Pending', result)
        return render_template('AdminPages/AdminLevels/LevelOne/pending_students_level1.html', result=result)