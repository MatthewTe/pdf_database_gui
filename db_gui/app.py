# Importing the main dash app packages:
import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
