from imageai.Prediction import ImagePrediction
import os
execution_path=os.getcwd() #gets current working directory
inputimage= input ("enter name of image you want to predict :")
count=input ("enter the number of predictions you want :")

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet() #you can use different models
prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5")) #instead of this input the filename of your model
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, inputimage), count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)