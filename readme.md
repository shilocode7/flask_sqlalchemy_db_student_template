# Good flask template
## contains:
### sqlalchemy
### CORS


# Update DB create 
    with app.app_context():
        db.create_all()
        app.run(debug=True)

# Run:
    create a virtual enviroment
    pip install -r .\requirements.txt
    flask run
