# Body Measurements Tracker

Flask based web application that allows users to track their body measurements over time.

Created primarily as a way for me to practice and expand my skills with Python and various data concepts.

## Features

- Input and tracking of weight progress over 10 weeks
- Visualization (line graph) of measurement trends spanning the 10 weeks
- Allows for incomplete data in the submitted form (excludes leading and trailing null or 0, uses interpolation for missing middle values)

## Potential features

- User registration and authentication
- Input and tracking of various body measurements (e.g., height, waist circumference, etc.)
- Personalized dashboard for each user to view their progress

## Techniques

- Flask
- PostgreSQL with SQLAlchemy (ORM) and flask migrate
- Matplotlib
- Data handling with pandas

Beyond the techniques mentioned above, I've during the project improved my skills with:

- Working with environment variables
- The file- and folder structure of a Flask application
