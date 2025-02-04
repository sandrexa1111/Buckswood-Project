from flask import Flask, render_template, request
import random
import string

app=Flask(__name__)

# Function passwordis sizliere
def check_password_strength(password):
    if len(password)<8:
        return "Weak", "text-weak"
    elif any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return "Medium", "text-medium"
    elif len(password)>= 12 and any(char in string.punctuation for char in password):
        return "Strong, nice", "text-strong"
    else:
        return "Medium, nice", "text-medium"


#funcia passwordis generaciistvis gamoviyene strings module romelic moicavs ascii digits
def generate_password(length):
    chars=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    generated_password=None
    password_strength=None
    strength_class=None

    if request.method =="POST":
        if "password" in request.form:
            # Password strenght
            password = request.form["password"]
            password_strength, strength_class = check_password_strength(password)
        elif "length" in request.form:
            # generator
            length=request.form["length"]
            if length.isdigit() and int(length) >0:
                generated_password = generate_password(int(length))
            else:
                generated_password = "Invalid length"

    return render_template(
        "index.html",
        generated_password=generated_password,
        password_strength=password_strength,
        strength_class=strength_class,
    )

if __name__ == "__main__":
    app.run(debug=True)
