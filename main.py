from flask import Flask, redirect, url_for, render_template, request
import baybot
import rankbot

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        searched_name = request.form["nm"]
        return redirect(url_for("name_result", bbnm=searched_name))
    else:
        return render_template("baybot_index.html")


@app.route("/<bbnm>", methods=["POST", "GET"])
def name_result(bbnm):
    total_names = baybot.search_name(bbnm)
    names_ranks = rankbot.search_name(bbnm)

    return render_template("name_result.html", requested_name=bbnm,
                           boycount=total_names[0], girlcount=total_names[1],
                           mostpop_boy_year=names_ranks[0], mostpop_boy_rank=names_ranks[1],
                           leastpop_boy_year=names_ranks[2], leastpop_boy_rank=names_ranks[3],
                           mostpop_girl_year=names_ranks[4], mostpop_girl_rank=names_ranks[5],
                           leastpop_girl_year=names_ranks[6], leastpop_girl_rank=names_ranks[7])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # For localhost testing only
    # app.run()
