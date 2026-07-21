from flask import Blueprint, request, jsonify

assistant = Blueprint("assistant", __name__)

def generate_response(question):
    q = question.lower()

    if "error" in q:
        return "It seems your system is facing errors. Check API limits or database connection."

    elif "slow" in q:
        return "Your system might be slow due to high traffic or backend delay."

    elif "health" in q:
        return "System health depends on success rate and error frequency."

    else:
        return "I'm your AI assistant. Ask me about logs, errors, or performance."

@assistant.route("/ask_ai", methods=["POST"])
def ask_ai():
    data = request.json
    question = data.get("question", "")

    answer = generate_response(question)

    return jsonify({"answer": answer})
