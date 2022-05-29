import os
import time
import inflect
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
doc = SimpleDocTemplate("leave_letter.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
p = inflect.engine()

page = []
receiver = input("Enter receiver post:")
college = input("Enter college name:")
address = input("Enter college address:")
salutation = None
choice1 = int(input(""""Choose a salutation
(1-Sir,2-Mam,3-Sir/Mam,0-Custom Salutation):"""))
if choice1 == 1:
    salutation = "Sir"
elif choice1 == 2:
    salutation = "Mam"
elif choice1 == 3:
    salutation = "Sir/Mam"
elif choice1 == 0:
    salutation = input("Enter custom salutation:")
else:
    salutation = "Sir"

classDetail = input("Enter class detail(Eg:bct 3rd sem, section A):")
reason = input("Enter the reason for leave(Eg:I am having high fever):")
leaveDays = int(input("Enter number of leave days:"))
name = input("Enter your full name:")
rollNo = input("Enter your roll number:")
subject = f"""Application for {p.number_to_words(leaveDays)} {p.plural("day",leaveDays)} leave"""
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='default', fontSize=14, leading=18))


def add_space():
    page.append(Spacer(1, 12))


def add_text(text, space=0):
    if type(text) == list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font>{text}</font>'
        page.append(Paragraph(ptext, style=styles["default"]))
        if space == 1:
            add_space()


# =============================== The content =======================
# ============================== of the document ====================
add_text([f"""To,
The {receiver.title().replace('Of','of')}
{college.title().replace('Of','of')}
{address.title()}""".splitlines()])
add_space()
add_text("Date : "+time.strftime("%d/%m/%Y"), 1)
add_text(f"Subject :- {subject.capitalize()}", 1)
add_text(f"Respected {salutation},", 1)
add_text(f"""I am a student of {classDetail} at your college.
 This is to inform you that, {reason}.""", 1)
add_text(f"""Therefore, I will not be able to come to school {"tomorrow" if leaveDays==1 else f"for {p.number_to_words(leaveDays)} days"}.
Kindly grant me the leave for {p.number_to_words(leaveDays)} {p.plural("day",leaveDays)}.
I shall be really grateful to you.""", 1)
add_text([f"""Thanking you,
{name.title()}
Roll No : {rollNo}""".splitlines()], 1)

# ===========================================================

doc.build(page)

os.startfile("leave_letter.pdf")
