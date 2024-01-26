import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add_feedback(name,email,contact_no,feedback):
  app_tables.feedback.add_row(
    Name=name,
    Email_id=email,
    contact_no=contact_no,
    feedback=feedback,
    created=datetime.now()
  )
  anvil.email.send(subject=f"Feedback form {name}",text=f"""
  A new person filled out the feedback form!
  Name: {name}
  Email address :{email}
  contact no:{contact}
  feedback:{feedback}
  """
  )
  