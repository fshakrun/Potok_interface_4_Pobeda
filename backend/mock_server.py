from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ego<int:clone>/billing/api/pending_comments_html')
def comments(clone):
    return """
    <div class='list-group-item'>
        <span class='text-content'>Негативный комментарий</span>
        <button class='edit-btn'>Edit</button>
    </div>
    """

@app.route('/ego<int:clone>/billing/api/pending_reviews_html')
def reviews(clone):
    return "<div class='list-group-item'>Отзыв MOCK</div>"

@app.route('/ego<int:clone>/billing/api/pending_all_html')
def all_items(clone):
    return "<div class='list-group-item'>Все элементы MOCK</div>"

@app.route('/ego<int:clone>/billing/api/pending_counts')
def counts(clone):
    return jsonify({
        "all_count": 10,
        "comments_count": 6,
        "reviews_count": 4
    })

@app.route('/ego<int:clone>/billing/api/filter_counts')
def filter_counts(clone):
    return jsonify({
        "comments": {"vk_count": 3, "telegram_count": 3},
        "reviews": {"gis2_count": 2, "yandex_count": 2}
    })

@app.route('/ego<int:clone>/cloner/stop/<path:bot>')
def stop_bot(clone, bot):
    return jsonify({"success": True, "bot": bot})

@app.route('/ego<int:clone>/cloner/start/<path:bot>')
def start_bot(clone, bot):
    return jsonify({"success": True, "bot": bot})

if __name__ == "__main__":
    app.run(port=5000)