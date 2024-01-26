from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def comment_click(self, **event_args):
    """Display a pop up to say you clicked the button"""
    alert("You clicked the button")
    
  

  def submit_button_click(self,**event_args):
    #set name to the text in the "name_box"
    name=self.name_box.text
    #set email to the text in the "email_box"
    email=self.email_box.text
    #set contact_no to the text in the "contact_box"
    contact_no=self.contact_box.text
    #set feedback to the text in the "feedback_box"
    feedback=self.feed_box.text
    anvil.server.call('add_feedback',name,email,contact_no,feedback)
    Notification("Feedback submitted").show()
    self.clear_input()

  def clear_inputs(self):
    self.name_box.text=" "
    self.email_box.text=" "
    self.contact_no.text=" "
    self.feed_box.text=" "




 

  
    