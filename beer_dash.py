{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import dash\n",
    "import dash_html_components as html\n",
    "import dash_core_components as dcc\n",
    "from dash.dependencies import Input, Output\n",
    "from jupyter_dash import JupyterDash\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.9.7\n"
     ]
    }
   ],
   "source": [
    "from platform import python_version\n",
    "\n",
    "print(python_version())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Running in Jupyter, call the following function to detect the proxy configuration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_loc = r\"C:\\Users\\barbj\\OneDrive\\Desktop\\last_four_months.csv\"\n",
    "\n",
    "df = pd.read_csv(file_loc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Global Category</th>\n",
       "      <th>Major Category</th>\n",
       "      <th>Minor Category</th>\n",
       "      <th>Item Quantity</th>\n",
       "      <th>Item/Cover %</th>\n",
       "      <th>Average Item Price</th>\n",
       "      <th>Gross Sales</th>\n",
       "      <th>Net Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>do what's in your heart (10oz)</td>\n",
       "      <td>BEVERAGE</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>10OZ DRAUGHT</td>\n",
       "      <td>91.0</td>\n",
       "      <td>4.80</td>\n",
       "      <td>7.00</td>\n",
       "      <td>637.0</td>\n",
       "      <td>637.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>kitty paws sour ipa 10oz</td>\n",
       "      <td>BEVERAGE</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>10OZ DRAUGHT</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0.47</td>\n",
       "      <td>7.00</td>\n",
       "      <td>63.0</td>\n",
       "      <td>63.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>field artillery</td>\n",
       "      <td>BEVERAGE</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>64OZ GROWLER FILLS</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0.47</td>\n",
       "      <td>24.33</td>\n",
       "      <td>219.0</td>\n",
       "      <td>200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>brute squad 4oz</td>\n",
       "      <td>BEVERAGE</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>4OZ DRAUGHT</td>\n",
       "      <td>9.0</td>\n",
       "      <td>0.47</td>\n",
       "      <td>4.00</td>\n",
       "      <td>36.0</td>\n",
       "      <td>36.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>socially acceptable</td>\n",
       "      <td>BEVERAGE</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>10OZ DRAUGHT</td>\n",
       "      <td>8.0</td>\n",
       "      <td>0.42</td>\n",
       "      <td>6.00</td>\n",
       "      <td>48.0</td>\n",
       "      <td>48.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        Item Name Global Category Major Category  \\\n",
       "0  do what's in your heart (10oz)        BEVERAGE        ALCOHOL   \n",
       "1        kitty paws sour ipa 10oz        BEVERAGE        ALCOHOL   \n",
       "2                 field artillery        BEVERAGE        ALCOHOL   \n",
       "3                 brute squad 4oz        BEVERAGE        ALCOHOL   \n",
       "4             socially acceptable        BEVERAGE        ALCOHOL   \n",
       "\n",
       "       Minor Category  Item Quantity  Item/Cover %  Average Item Price  \\\n",
       "0        10OZ DRAUGHT           91.0          4.80                7.00   \n",
       "1        10OZ DRAUGHT            9.0          0.47                7.00   \n",
       "2  64OZ GROWLER FILLS            9.0          0.47               24.33   \n",
       "3         4OZ DRAUGHT            9.0          0.47                4.00   \n",
       "4        10OZ DRAUGHT            8.0          0.42                6.00   \n",
       "\n",
       "   Gross Sales  Net Sales  \n",
       "0        637.0      637.0  \n",
       "1         63.0       63.0  \n",
       "2        219.0      200.0  \n",
       "3         36.0       36.0  \n",
       "4         48.0       48.0  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Explore dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Net Sales</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Minor Category</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10OZ DRAUGHT</th>\n",
       "      <td>509.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16OZ DRAUGHT</th>\n",
       "      <td>1371.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32OZ GROWLER FILLS</th>\n",
       "      <td>31.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4OZ DRAUGHT</th>\n",
       "      <td>33.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64OZ GROWLER FILLS</th>\n",
       "      <td>173.17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BEER FLIGHTS</th>\n",
       "      <td>2242.29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CLOTHING</th>\n",
       "      <td>50.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FOOD</th>\n",
       "      <td>65.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GIFT CARDS</th>\n",
       "      <td>991.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KEGS</th>\n",
       "      <td>163.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MERCHANDISE</th>\n",
       "      <td>78.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PACKAGED GOODS</th>\n",
       "      <td>631.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PRIVATE EVENTS</th>\n",
       "      <td>2400.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Net Sales\n",
       "Minor Category               \n",
       "10OZ DRAUGHT           509.93\n",
       "16OZ DRAUGHT          1371.83\n",
       "32OZ GROWLER FILLS      31.89\n",
       "4OZ DRAUGHT             33.22\n",
       "64OZ GROWLER FILLS     173.17\n",
       "BEER FLIGHTS          2242.29\n",
       "CLOTHING                50.40\n",
       "FOOD                    65.67\n",
       "GIFT CARDS             991.00\n",
       "KEGS                   163.50\n",
       "MERCHANDISE             78.50\n",
       "PACKAGED GOODS         631.67\n",
       "PRIVATE EVENTS        2400.00"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_avgs = pd.DataFrame(round(df.groupby(['Minor Category'])['Net Sales'].mean(), 2))\n",
    "df_avgs"
   ]
  },
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
    "    app.run_server(debug=True)\n",
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