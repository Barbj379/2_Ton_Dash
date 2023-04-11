{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Create a dash application"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash app running on http://127.0.0.1:8050/\n"
     ]
    }
   ],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import dash\n",
    "import dash_html_components as html\n",
    "import dash_core_components as dcc\n",
    "from dash.dependencies import Input, Output, State\n",
    "from jupyter_dash import JupyterDash\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go \n",
    "\n",
    "file_loc = \"https://raw.githubusercontent.com/Barbj379/2_Ton_Dash/main/last_four_months.csv\"\n",
    "#file_loc = \"https://www.pythonanywhere.com/user/Barbj3799/files/home/Barbj3799/mysite/last_four_months.csv?edit\"\n",
    "\n",
    "df = pd.read_csv(file_loc)\n",
    "\n",
    "# Create a dash application\n",
    "app = JupyterDash(__name__)\n",
    "server=app.server\n",
    "\n",
    "app.layout= html.Div(children=[\n",
    " # New Div for all elements in the new 'row' of the page\n",
    "    html.Div([ \n",
    "        html.H1(children='Two Ton Dash'),\n",
    "           html.Div(children='''\n",
    "            Sales report of last fiscal half.\n",
    "            \n",
    "        '''),\n",
    "    html.Div([dcc.Graph(id='graph0'),\n",
    "       html.Label([\"Category\",\n",
    "                dcc.Dropdown(\n",
    "                id='category-dropdown', clearable=False,\n",
    "                value='ALCOHOL', options=[\n",
    "                    {'label': c, 'value': c}\n",
    "                    for c in df['Major Category'].unique()])\n",
    "                ]),\n",
    "           \n",
    "        ]),\n",
    "    ])\n",
    "])\n",
    "\n",
    "\n",
    "# Callback function that automatically updates the tip-graph based on chosen colorscale\n",
    "@app.callback(\n",
    "    Output('graph0', 'figure'),\n",
    "    [Input(\"category-dropdown\", \"value\")]\n",
    ")\n",
    "def update_figure(Category):\n",
    "    new_df = df[df['Major Category']==Category]\n",
    "    new_df = new_df.groupby(['Minor Category', 'Item Name'])['Net Sales'].sum().reset_index()\n",
    "    new_df.reset_index()\n",
    "    fig=px.bar(\n",
    "        new_df, x=\"Minor Category\", y=\"Net Sales\",  color=\"Item Name\",\n",
    "        color_continuous_scale=Category,\n",
    "        title=\"Items\")\n",
    "    return fig\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    app.server(debug=True)\n",
    "# Create an app layout"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Build Dash application"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
