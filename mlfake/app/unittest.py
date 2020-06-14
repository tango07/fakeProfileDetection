# from urllib import request

from app.model import Predict
def setUp(self):
	self.featureReal=[120,14000,140,11,12,1,1]
	# self.featureFake=[12,140,14000,11,0,1,5]
	# self.name = "akash"

def tearDown(self):
	del self

#Test case for real profiles prediction
def forRealProfile(self):
	expected_result="Real"
	self.assertEqual(Predict().prediction(self.featureReal),expected_result)


# Test case for fake profile prediction
# def forFakeProfile(self):
# 	expected_result="Fake"
# 	self.assertEqual(Predict().prediction(self.featureFake),expected_result)
#
# #Test case for api check
# def apiCheck(self):
# 	api_url="http://127.0.0.1:5000/predict"
# 	response = request.post(url=api_url,data=self.featureReal)
# 	status_code = response.status_code
# 	self.assertEqual(status_code,200)

#test case for gender prediction
# def genderPredict():
# 	expected_result = 1
# 	self.assertEqual(predict_sex(name),expected_result)
#
# #test case for successfully reading the dataset i.e., empty or not
# def readDataset():
# 	assertNotEqual(read_datasets(),[])
#
# #test case for extracting features
# def successfullyExtractFeature():
# 	assertNotEqual(extract_features(),[])
#
# #test case to check whether the output is coming or not
# def CheckOutput():
# 	api_url="http://127.0.0.1:5000/predict"
# 	response = request.post(url=api_url,data=self.featureReal)
# 	self.assertNotEqual(index(),"some error occured!")