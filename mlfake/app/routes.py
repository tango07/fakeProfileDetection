from flask import request, render_template, Flask
# from app import app
from app.model import Predict
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data= request.form.to_dict()
        int_feature = list(data.keys())
        features_values =list(data.values())
        int_features_values = [int(data) for data in features_values]
        list_int_features_values =[int_features_values]
        output = Predict().prediction(list_int_features_values)
        # print(int_features_values)
        # statuses = int(request.form["statuses"])
        # friends = int(request.form["friends"])
        # favourites = int(request.form["favourites"])
        # listed = int(request.form["listed"])
        # statuses = int(request.form["statuses"])
        # sex = int(request.form["sex"])
        # lang = int(request.form["lang"])
        # name = request.form["foo"]
        # lorem = request.form["lorem"]
        print(output)
        return output
    return "some error occured!!!"


# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/hello-world', methods=['PUT', 'GET', 'POST', 'DELETE'])
# #     sex_code_dict = {'female': -2, 'mostly_female': -1, 'unknown': 0, 'andy': 0, 'mostly_male': 1, 'male': 2}
#
# def predict():
#     int_feature = []
#     for x in request.form.values():
#          if x.isdigit():
#              int_feature.append(int(x))
#          else:
#              if x=="Male":
#                  x=2
#              elif x=="Female":
#                  x=-2
#              elif x=="Mostly Male":
#                  x=1
#              elif x=="Mostly Female":
#                  x=-1
#              elif x=="Unknown":
#                  x=0
#              int_feature.append(int(x))
#     list_int_features = [int_feature]
#     output = ""
#     if request.method == 'POST':
#     #     data = request.json
#     #     l = [[data['statuses_count'], data['followers_count'], data['friends_count'], data['favourites_count'],
#     #           data['listed_count'], data['sex_code'], data['lang_code']]]
#         print(int_feature)
#         output = Predict().prediction(list_int_features)
#         color="green"
#         if output == "FAKE":
#             color = "red"
#     return render_template('result.html', prediction_text=output, result_color=color)


if __name__ == "__main__":
    app.run(debug=True)
