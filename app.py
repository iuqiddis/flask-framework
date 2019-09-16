from flask import Flask, render_template, request, redirect
import bokeh
import quandl
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.embed import components
import jinja2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_quand():

    if request.method == 'GET':
        return render_template('userinfo_lulu.html')
    else:
        # request was a POST
        wk = 'WIKI/'
        stk = request.form['name_lulu']
        wkstk = wk + stk

        # Get the data for Coca-cola
        data = quandl.get(wkstk, start_date="2016-01-01", end_date="2018-01-01", api_key="ykWz-sF54JasM3SZyA5h")
        source = ColumnDataSource(data)

        #output_file("test.html")
        p = figure(x_axis_type="datetime")
        p.line(x='Date', y='Close', source=source)
        script, div = components(p)
        #show(p)

        template = jinja2.Template("""
	<!DOCTYPE html>
	<html lang="en-US">
	
	<link
    	href="https://cdn.pydata.org/bokeh/dev/bokeh-1.1.1.min.css"
    	rel="stylesheet" type="text/css"
	>
	<script 
    	src="https://cdn.pydata.org/bokeh/release/bokeh-1.3.4.min.js"
	></script>

	<body>

    	<h1>Hello Bokeh!</h1>
    
    	<p> Below is a simple plot of stock closing prices </p>
    
    	{{ script }}
    
    	{{ div }}

	</body>

	</html>
	""")










        #return redirect('/')
        return template.render(script = script, div = div)



if __name__ == "__main__":
    app.run(port=33507)



###########################



#app = Flask(__name__)

#@app.route('/')
#def index():
# return render_template('index.html')

#@app.route('/about')
#def about():
# return render_template('about.html')

#if __name__ == '__main__':
# app.run(port=33507)
