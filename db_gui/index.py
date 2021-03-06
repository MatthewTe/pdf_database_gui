# Importing the main Dash and Plotly Packages:
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import database_gui

# Assigning an empty Div tag to be formatted based on the url:
app.layout = html.Div([

        # Url that specifies page via callback return (Url bar, does not render anything):
        dcc.Location(id='url', refresh=False),

        # Creating a Main Navbar that remains constant to every page:
        dbc.Navbar(
            [
            # Main Navbar link to the main navigation page:
            dbc.NavbarBrand('PDF Database GUI', href = '/', style={'font-size':'20px'}),

            # Button Link to the database summary information page:
            dbc.Button('PDF Database', href='/apps/database_gui', style={'font-size':'10px'}),

            # User input to store path to sqlite database nested in formatting div tag:
            html.Div(
                id = 'database_path_string_div',
                children = [
                    dcc.Input(
                        id='database_path_string',
                        type='text',
                        style = {'height':'auto', 'margin-bottom':'auto',
                            'margin-left':'1.5em', 'width':'150%', 'height':'150%'},
                        placeholder = 'Database Path String',
                        debounce = True)
                    ]
                )

            ],
            color = 'dark',
            dark = True
        ),

        # Main Div tag that is formatted to create the page based on app.layouts:
        html.Div(id='main_content_div')
        ]
    )

# Callback that formats the Dash app based on the layouts from the apps/:
@app.callback(
    Output(component_id='main_content_div', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    '''
    Function returns an app.layout of a specific dash app page based on an
    input url.

    These dash application pages are located in python files in the db_gui/apps/
    sub folder.

    Parameters
    ----------
    pathname : str
        A string representing a url to the respective application page

    Returns
    -------
    app.layout : dash.app.layout object
        The layout of the dash app that will be used to format the page associated
        with the url input.
    '''
    # Conditional that selects the layout to be returned based on url pathname:
    if pathname == '/apps/database_gui':
        return database_gui.layout


if __name__ == "__main__":
    app.run_server(debug=True)
