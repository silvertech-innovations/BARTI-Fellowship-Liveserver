from datetime import datetime
from flask import request
from fpdf import FPDF


def get_base_url():
    base_url = request.url_root
    return base_url


def generate_award_letter_2023(data, filename):
    class PDF(FPDF):
        header_added = False  # To track whether the header is added to the first page

        def header(self):
            if not self.header_added:
                var = get_base_url()
                print(var)
                # Add a header
                self.set_font("Arial", "B", 12)
                # self.image('/static/Images/satya.png', 94, 10, 20)  # Replace with the path to your small imag
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/satya.png', 94, 10,
                           20)  # Replace with the path to your small imag
                # Calculate the width of the image
                image_width = 100  # Assuming the width of the image is 100 (adjust if different)
                # Calculate the position for "Government of Maharashtra" text
                text_x_position = self.get_x()  # Get current X position
                text_y_position = self.get_y() + 20  # Set Y position below the image
                # Set cursor position
                self.set_xy(text_x_position, text_y_position)
                # self.image('/static/Images/newtrtiImage.png', 10, 10, 45)  # Replace with the path to your symbol image
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/newtrtiImage.png', 10, 10,
                           45)  # Replace with the path to your symbol image
                # self.image('/static/Images/mahashasn_new.png', 155, 10, 45)  # Replace with the path to your symbol image
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/mahashasn_new.png', 155, 10,
                           45)  # Replace with the path to your symbol image
                self.ln(5)
                self.ln(0)  # Reduce the space below the address
                self.cell(0, 5, "Government of Maharashtra", align="C", ln=True)

                self.cell(0, 5, "Tribal Research & Training Institute", align="C", ln=True)
                self.cell(0, 10, "28, Queens Garden, Pune - 411001", align="C", ln=True)
                self.dashed_line(10, self.get_y(), 200, self.get_y(), dash_length=3, space_length=1)

                self.ln(5)  # Adjust this value to control the space after the line
                self.set_font("Arial", size=10)
                self.cell(0, 10, "No.: Research-2024/Case.No 9/Desk-4/1832",
                          ln=False)  # Add the number on the left without a line break

                # Move to the right for the date
                self.cell(0, 10, "Date: 04-07-2024", align="R",
                          ln=True)  # Add the date on the right with a line break

                self.set_font("Arial", "B", size=10)
                self.cell(0, 10,
                          " Fellowship Award Letter",
                          align="C", ln=True)
                self.ln(2)  # Adjust this value to control the space after the line

                self.rotate(45)  # Rotate the text by 45 degrees
                self.set_font('Arial', '', 45)
                self.set_text_color(192, 192, 192)
                self.text(-30, 195, "STRF FELLOWSHIP")  # Use text instead of rotated_text
                self.rotate(0)  # Reset the rotation to 0 degrees

                self.header_added = True  # Set to True after adding the header

        def to_name(self, data):
            # AWARD LETTER in the center

            # To, and Dear Candidate aligned to the left
            self.set_font("Arial", "", size=10)
            self.cell(0, 10, "To,", ln=True)
            self.set_font("Arial", "B", size=11)
            self.cell(0, 10, data['first_name'] + ' ' + data['middle_name'] + ' ' + data['last_name'], ln=True)

        def insert_static_data(self, data):
            # Insert your static data here
            self.set_font("Arial", "B", size=10)
            self.cell(0, 10, "Dear Candidate,", ln=True)
            self.set_font("Arial", "", 10)
            registration_year = data['phd_registration_year']
            fiscal_year = f"{registration_year} - {registration_year + 1}"
            self.multi_cell(0, 7,
                            "         We are delighted to inform you that you have been selected for the award of "
                            "a Fellowship for the year " + fiscal_year +
                            " for Ph.D. The Fellowship amount will be effective from the date of registration for Ph.D. Congratulations! "
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       TRTI reserves all the rights to add terms and conditions as and when required, and "
                            "candidates are required to accept any changes in the terms and conditions of the fellowship."
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       Attached with this letter is an undertaking stating that all the information provided "
                            "for the document verification is true to the best of my knowledge. Any discrepancy found "
                            "may result in the cancellation of the Fellowship. Please note that failure to submit the "
                            "undertaking will be assumed as non-acceptance of this offer, and the Fellowship will not "
                            "be  processed. "
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       We believe this Fellowship will not only provide financial support but also contribute"
                            " to your academic growth. It will enable you to conduct research on your subject and "
                            "foster excellence in academia. Moreover, it will empower you to become an advocate for"
                            " equality, social justice, a contributor to peace, harmony and happiness within various"
                            " disadvantaged sections of society. "
                            )
            self.multi_cell(0, 20, "Wish you all the best. ")
            self.set_x(150)  # Adjust the x-coordinate as needed
            # self.image('/static/Images/signature_awardletter.png', 20, 230, 30)
            # self.image('/static/Images/chanchalamam_signature.png', 125, 210, 50)
            self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/chanchalamam_signature.png', 125, 210, 50)
            self.ln(5)  # Adjust this value to control the space after static data

        def footer(self):
            # Add a footer
            self.set_y(-15)
            self.set_font("arial", "B", 8)
            self.cell(0, 10, f" {self.page_no()} ", align="C")

            # Center-align the "TRTI" text
            self.cell(0, 10, " TRTI  |  Fellowship | 2023 - 2024 ", align="R")

    pdf = PDF()
    pdf.add_page()
    pdf.header()
    pdf.to_name(data)
    # Insert static data
    pdf.insert_static_data(data)
    # Save the PDF to a file
    pdf.output(filename)


def generate_award_letter_2022(data, filename):
    class PDF(FPDF):
        header_added = False  # To track whether the header is added to the first page

        def header(self):
            if not self.header_added:
                var = get_base_url()
                print(var)
                # Add a header
                self.set_font("Arial", "B", 12)
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/satya.png', 94, 10,
                           20)  # Replace with the path to your small imag
                # Calculate the width of the image
                image_width = 100  # Assuming the width of the image is 100 (adjust if different)
                # Calculate the position for "Government of Maharashtra" text
                text_x_position = self.get_x()  # Get current X position
                text_y_position = self.get_y() + 20  # Set Y position below the image
                # Set cursor position
                self.set_xy(text_x_position, text_y_position)
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/newtrtiImage.png', 10, 10,
                           45)  # Replace with the path to your symbol image
                self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/mahashasn_new.png', 155, 10,
                           45)  # Replace with the path to your symbol image
                self.ln(5)
                self.ln(0)  # Reduce the space below the address
                self.cell(0, 5, "Government of Maharashtra", align="C", ln=True)

                self.cell(0, 5, "Tribal Research & Training Institute", align="C", ln=True)
                self.cell(0, 10, "28, Queens Garden, Pune - 411001", align="C", ln=True)
                self.dashed_line(10, self.get_y(), 200, self.get_y(), dash_length=3, space_length=1)

                self.ln(5)  # Adjust this value to control the space after the line
                self.set_font("Arial", "B", size=10)
                self.cell(0, 10,
                          " Fellowship Award Letter",
                          align="C", ln=True)
                self.ln(2)  # Adjust this value to control the space after the line

                self.rotate(45)  # Rotate the text by 45 degrees
                self.set_font('Arial', '', 45)
                self.set_text_color(192, 192, 192)
                self.text(-30, 195, "STRF FELLOWSHIP")  # Use text instead of rotated_text
                self.rotate(0)  # Reset the rotation to 0 degrees

                self.header_added = True  # Set to True after adding the header

        def to_name(self, data):
            # AWARD LETTER in the center

            # To, and Dear Candidate aligned to the left
            self.set_font("Arial", "", size=10)
            self.cell(0, 10, "To,", ln=True)
            self.set_font("Arial", "B", size=11)
            self.cell(0, 10, data['first_name'] + ' ' + data['middle_name'] + ' ' + data['last_name'], ln=True)

        def insert_static_data(self, data):
            # Insert your static data here
            self.set_font("Arial", "B", size=10)
            self.cell(0, 10, "Dear Candidate,", ln=True)
            self.set_font("Arial", "", 10)
            registration_year = data['phd_registration_year']
            fiscal_year = f"{registration_year} - {registration_year + 1}"
            self.multi_cell(0, 7,
                            "         We are delighted to inform you that you have been selected for the award of "
                            "a Fellowship for the year " + fiscal_year +
                            " for Ph.D. The Fellowship amount will be effective from the date of registration for Ph.D. Congratulations! "
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       TRTI reserves all the rights to add terms and conditions as and when required, and "
                            "candidates are required to accept any changes in the terms and conditions of the fellowship."
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       Attached with this letter is an undertaking stating that all the information provided "
                            "for the document verification is true to the best of my knowledge. Any discrepancy found "
                            "may result in the cancellation of the Fellowship. Please note that failure to submit the "
                            "undertaking will be assumed as non-acceptance of this offer, and the Fellowship will not "
                            "be  processed. "
                            )
            self.ln(3)  # Adjust this value to control the space before static data
            self.multi_cell(0, 7,
                            "       We believe this Fellowship will not only provide financial support but also contribute"
                            " to your academic growth. It will enable you to conduct research on your subject and "
                            "foster excellence in academia. Moreover, it will empower you to become an advocate for"
                            " equality, social justice, a contributor to peace, harmony and happiness within various"
                            " disadvantaged sections of society. "
                            )
            self.multi_cell(0, 20, "Wish you all the best. ")
            self.set_x(150)  # Adjust the x-coordinate as needed
            # self.image('/static/Images/signature_awardletter.png', 20, 230, 30)
            self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/sonanwanesir_signature.png', 125, 210, 50)
            self.ln(5)  # Adjust this value to control the space after static data

        def footer(self):
            # Add a footer
            self.set_y(-15)
            self.set_font("arial", "B", 8)
            self.cell(0, 10, f" {self.page_no()} ", align="C")

            # Center-align the "TRTI" text
            self.cell(0, 10, " TRTI  |  Fellowship | 2023 - 2024 ", align="R")

    pdf = PDF()
    pdf.add_page()
    pdf.header()
    pdf.to_name(data)
    # Insert static data
    pdf.insert_static_data(data)
    # Save the PDF to a file
    pdf.output(filename)


# This below function (generate_pdf_with_styling) is used on fellowship_awarded.html Page
def generate_pdf_with_styling(data, filename):
        class PDF(FPDF):
            header_added = False  # To track whether the header is added to the first page

            def header(self):
                if not self.header_added:
                    # //var/www/icswebapp/icswebapp/
                    self.set_font("Arial", "B", 12)
                    self.cell(0, 10, "Fellowship ", align="C",
                              ln=True)  # Add space by changing the second parameter (e.g., 20)
                    # Insert an image (symbol) at the center of the header
                    self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/trti.jpeg', 10, 10,
                               20)  # Replace with the path to your symbol image
                    # Insert an image (symbol) at the right of the header
                    self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/satya.png', 155, 10,
                               20)  # Replace with the path to your small image
                    self.image('/var/www/fellowship/fellowship/FellowshipPreServer/static/Images/maharashtra_shasn.png', 175, 10,
                               20)  # Replace with the path to your symbol image
                    self.cell(0, 10, "Tribal Research & Training Institute, Pune ", align="C", ln=True)
                    self.cell(0, 1, "Government of Maharashtra ", align="C", ln=True)
                    self.set_font("Arial", "B", size=8)
                    self.cell(0, 10,
                              "28, Queen's Garden, Bund Garden Rd, near Old Circuit House, Camp, Pune, Maharashtra 411001 ",
                              align="C", ln=True)
                    self.set_font("Arial", "B", 13)
                    self.cell(0, 10,
                              " Fellowship Application Form 2023 - 2024",
                              align="C", ln=True)
                    self.ln(2)  # Adjust this value to control the space after the line
                    self.line(10, self.get_y(), 200, self.get_y())  # Draw a line from left (10) to right (200)
                    self.header_added = True  # Set to True after adding the header

            def image_and_date(self, data):
                # Date and Applicant ID
                self.set_font("Arial", "B", size=11)
                current_date = datetime.now().strftime("%Y-%m-%d")  # You can change the date format as needed
                self.cell(50, 10, "Applicant ID: " + data['applicant_id'], ln=False)
                self.cell(108)  # Add space between cells
                # self.cell(50, 10, "Date: " + current_date, ln=True)
                self.set_font("Arial", size=10)
                full_name = data['first_name'] + ' ' + data['middle_name'] + ' ' + data['last_name']
                self.cell(50, 10, "Full Name: " + str(full_name), ln=True)

                if 'applicant_id' and 'application_date' in data:
                    data['applicant_id'] = 'TRTI' + '/' + str(data['phd_registration_year']) + '/' + str(data['id'])
                    self.cell(50, 10, "Submitted Date: " + str(data['application_date']), ln=True)
                    self.cell(50, 10, "Submitted Time: " + str(data['application_time']), ln=True)

                if 'applicant_photo' in data:
                    # photo = '/static/Images/trti.jpeg'
                    photo = '/var/www/fellowship/fellowship/FellowshipPreServer' + data['applicant_photo']
                    print(photo)
                    # Insert the applicant photo (adjust the coordinates and size as needed)
                    self.image(photo, 165, 65, 30, 35)  # Adjust the Y-coordinate from 60 to 65
                    self.rect(165, 65, 30, 35)  # Adjust the Y-coordinate accordingly
                    self.ln(10)  # Space between Date/Applicant ID and the main content

            def footer(self):
                # Add a footer
                self.set_y(-15)
                self.set_font("Arial", "B", 8)
                self.cell(0, 10, f" {self.page_no()} ", align="C")

                # Center-align the "TRTI" text
                self.cell(0, 10, " TRTI  |  Fellowship | 2023 - 2024 ", align="R")

        personal_details = {
            "Adhaar Number": data['adhaar_number'],
            "First Name": data['first_name'],
            "Middle Name": data['middle_name'],
            "Last Name": data['last_name'],
            "Mobile Number": data['mobile_number'],
            "Email": data['email'],
            "Date of Birth": data['date_of_birth'],
            "Gender": data['gender'],
            "Age": data['age'],
            "Category": data['caste'],
            "Caste/Tribe ": data['your_caste'],
            "Sub Caste/Tribe": data['subcaste'],
            "Do you belong to PVTG?": data['pvtg'],
            "Which caste/tribe you belong in PVTG?": data['pvtg_caste']

            # Add more fields as needed
        }

        address_details = {
            "Main Address": data['add_1'],
            "Postal Address": data['add_2'],
            "Pincode": data['pincode'],
            "Village": data['village'],
            "Taluka": data['taluka'],
            "District": data['district'],
            "City": data['city'],
            "State": data['state']
        }

        # qualification_details = {
        # SSC
        ssc = {
            "SSC Passing Year": data['ssc_passing_year'],
            "SSC School Name": data['ssc_school_name'],
            "SSC Stream": data['ssc_stream'],
            "SSC Attempts": data['ssc_attempts'],
            "SSC Total Marks": data['ssc_total'],
            "SSC Percentage": data['ssc_percentage']
        }

        hsc = {
            "HSC Passing Year": data['hsc_passing_year'],
            "HSC School Name": data['hsc_school_name'],
            "HSC Stream": data['hsc_stream'],
            "HSC Attempts": data['hsc_attempts'],
            "HSC Total Marks": data['hsc_total'],
            "HSC Percentage": data['hsc_percentage']
        }

        grad = {
            "Graduation Passing Year": data['graduation_passing_year'],
            "Graduation College Name": data['graduation_school_name'],
            "Graduation Stream": data['grad_stream'],
            "Graduation Attempts": data['grad_attempts'],
            "Graduation Total Marks": data['grad_total'],
            "Graduation Percentage": data['graduation_percentage']
        }

        postgrad = {
            "Post Graduation Passing Year": data['phd_passing_year'],
            "Post Graduation College Name": data['phd_school_name'],
            "Post Graduation Stream": data['pg_stream'],
            "Post Graduation Attempts": data['pg_attempts'],
            "Post Graduation Total Marks": data['pg_total'],
            "Post Graduation Percentage": data['phd_percentage'],

            "What have you Qualified?": data['have_you_qualified']
            # Add more fields as needed
        }

        phd_details = {
            "P.H.D Registration Date": data['phd_registration_date'],
            "P.H.D Registration Year": data['phd_registration_year'],
            "Age at Ph.D. Registration": data['phd_registration_age'],
            "University Name": data['concerned_university'],
            "Name of College": data['name_of_college'],
            "Department Name": data['department_name'],
            "Topic of Ph.D.": data['topic_of_phd'],
            "Name of Guide": data['name_of_guide'],
            "Faculty/Stream": data['faculty']
            # Add more fields as needed
        }

        income_details = {
            "Family Annual Income": data['family_annual_income'],
            "Income Certificate Number": data['income_certificate_number'],
            "Income Certificate Issuing Authority": data['issuing_authority'],
            "Income Certificate Issuing District": data['income_issuing_district'],
            "Income Certificate Issuing Taluka": data['income_issuing_taluka']
        }

        caste = {
            "Are you Domicile of Maharashtra": data['domicile'],
            "Domicile Certificate": data['domicile_certificate'],
            "Domicile Certificate Number": data['domicile_number'],
            "Do you have Caste/Tribe Certificate": data['caste_certf'],
            "Caste | Tribe": data['your_caste'],
            "Sub Caste/Tribe": data['subcaste'],
            "Caste Certificate Number": data['caste_certf_number'],
            "Caste Certificate Issuing District": data['issuing_district'],
            "Caste Certificate Issuing Authority": data['caste_issuing_authority'],
            "Validity Certificate": data['validity_certificate'],
            "Validity Certificate Number": data['validity_cert_number'],
            "Validity Certificate Issuing District": data['validity_issuing_district'],
            "Validity Certificate Issuing Taluka": data['validity_issuing_taluka'],
            "Validity Certificate Issuing Authority": data['validity_issuing_authority']
        }

        parent_details = {
            "Salaried": data['salaried'],
            "Disability": data['disability'],
            "Type of Disability": data['type_of_disability'],
            "Father Name": data['father_name'],
            "Mother Name": data['mother_name'],
            "Anyone Work in Government": data['work_in_government'],
            "Department in Government": data['gov_department'],
            "Post in Government": data['gov_position']
        }

        bank_details = {
            "IFSC Code": data['ifsc_code'],
            "Account Number": data['account_number'],
            "Bank Name": data['bank_name'],
            "Account Holder Name": data['account_holder_name'],
            "MICR Code": data['micr']
        }

        pdf = PDF(orientation='P', format='A4')
        pdf.add_page()
        pdf.header()
        pdf.image_and_date(data)

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Personal Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in personal_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(15)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Address Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in address_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(10)  # Adjust this value to control the space after each section

        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Qualification Details", ln=True)

        pdf.ln(10)  # Increase this value to shift the content further down

        # SSC Details
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(0, 10, "S.S.C Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in ssc.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # HSC Details
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(0, 10, "H.S.C Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in hsc.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # Graduation Details
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(0, 10, "Graduation Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in grad.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # Post Graduation Details
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(0, 10, "Post Graduation Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in postgrad.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "P.H.D Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in phd_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.multi_cell(0, 10, str(value), border=0)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Income Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in income_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(5)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Caste/Tribe Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in caste.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(10)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Parent Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in parent_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(10)  # Adjust this value to control the space after each section

        # Personal Details
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(0, 10, "Bank Details", ln=True)
        pdf.ln(2)  # Adjust this value to control the space after the line
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        pdf.header_added = True  # Set to True after adding the header
        pdf.set_font("Arial", size=10)
        for field, value in bank_details.items():
            pdf.cell(70, 10, str(field), border=0)
            pdf.cell(0, 10, str(value), border=0, ln=True)
        pdf.ln(10)  # Adjust this value to control the space after each section
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line from left (10) to right (200)
        # Applicant's Signature
        text = (
            "I hereby declare by signing below that the above particulars are true and correct to the best of my knowledge "
            "and belief and nothing has been concealed therein")
        # Define the width for text wrapping
        width = 400  # Adjust this width according to your requirement
        # Draw the text with wrapping
        pdf.cell(width, 10, txt=text, ln=True)
        pdf.set_font("Arial", size=12)
        # Assuming data['signature'] contains the path to the image file
        signature_path = data['signature']
        # Determine the current position
        x = pdf.get_x()
        y = pdf.get_y()
        # Set position for the image
        pdf.set_xy(x + 10, y + 5)  # Adjust position as needed
        # Add the image
        pdf.image(signature_path, x + 50, y + 10, 50)  # Adjust width (50) as needed
        # Move to a new line
        pdf.ln(15)  # Adjust as needed
        pdf.cell(0, 10, "Applicant's Signature:", ln=True)
        pdf.ln(15)  # Adjust this value to control the space after the line
        current_date = datetime.now().strftime("%Y-%m-%d")  # You can change the date format as needed
        pdf.cell(0, 10, "Date:" + ' ' + current_date, ln=True)
        pdf.cell(0, 10, "Place:" + ' ' + data['city'] + ', ' + data['state'], ln=True)

        # Save the PDF to a file
        pdf.output(filename)