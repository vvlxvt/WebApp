from .db import db

def add_sample_data():
    if len(db.all()) == 0:
        db.insert({"name": "Order Form",
                   "fields": {"email": "email",
                              "user_phone": "phone",
                              "order_date": "date",
                              "description":"text"}})
        db.insert({"name": "Lead Form",
                   "fields": {"lead_email": "email",
                              "lead_phone": "phone",
                              "message": "text"}})
        db.insert({"name": "Call Form",
                   "fields": {"new_phone": "phone",
                              "new_date": "date",
                              "new_text": "text"}})
        db.insert({"name": "Simply Form",
                   "fields": {"email": "email",
                              "adv": "text"}})
        db.insert({"name": "Bill Form",
                   "fields": {"email": "email",
                              "phone": "phone",
                              "date": "date",
                              "bill": "text"}})
        db.insert({"name": "Email Form",
                   "fields": {"email": "email"
                              }})



