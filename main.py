from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/highlighted-data", methods=["POST"])
def highlighted_data():
    print(request)
    text = request.get_data()

    return text, 201

if __name__ == "__main__":
    app.run(debug=True)