# Josiah Groux
# this is my web program for Seminar. It makes toasters where the user can choose the size and color

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# this is the home page function
@app.route('/', methods = ["GET", "POST"])
def homePage():
    # this is used in the other pages to return to the beginning page as
    # well as where the program starts
    return render_template('homePage.html')

# This function is to find the results
@app.route("/toasterResults", methods=["GET", "POST"])
def toasterResults():
    # these take the results from the drop down boxes so that they can be used below
    colorToasts = str(request.form('colorToaster'))
    sizeToasts = str(request.form('sizeToaster'))

    # the following if statements will check to see what the color and size were when then
    # the submit button was clicked so that it can call the correct html form
    if colorToasts == "red" and sizeToasts == "small":
        return render_template('redSmallToaster.html')
    elif colorToasts == "red" and sizeToasts == "medium":
        return render_template('redMediumToaster.html')
    elif colorToasts == "red" and sizeToasts == "large":
        return render_template('redLargeToaster.html')
    elif colorToasts == "blue" and sizeToasts == "small":
        return render_template('blueSmallToaster.html')
    elif colorToasts == "blue" and sizeToasts == "medium":
        return render_template('blueMediumToaster.html')
    elif colorToasts == "blue" and sizeToasts == "large":
        return render_template('blueLargeToaster.html')
    elif colorToasts == "green" and sizeToasts == "small":
        return render_template('greenSmallToaster.html')
    elif colorToasts == "green" and sizeToasts == "medium":
        return render_template('greenMediumToaster.html')
    elif colorToasts == "green" and sizeToasts == "large":
        return render_template('greenLargeToaster.html')
    else:
        ''

if __name__ == "__main__":
    app.run(debug=True)