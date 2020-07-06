from ifscApi.getDetailsLambda import FetchData
import json

def lambda_handler(event,context):
  ifsc=event["ifsc"]
  parser=FetchData()
  dbfile='ifsc2.db'
  res=parser.getdata(event['ifsc'],dbfilePath=dbfile)
  return{
    'statusCode':200,
    "body":json.dumps({
      "message":res
    }),
  }
