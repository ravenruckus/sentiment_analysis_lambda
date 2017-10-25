### Steps to create AWS Lambda sentiment analysis api.
1. npm install -g serverless
2. Create director & cd into directory
3. serverless create -t aws-python
4. virtualenv -p /usr/bin/python2.7 venv  
  -python2.7 is needed to avoid splite errors  
  ```Unable to import module 'handler: No module named _splite3
  ```
5. source venv/bin/activate
6. pip install textblob
7. pip freeze > requirements.txt
8. npm init
9. npm install --save serverless-python-requirements
10. export PATH=~/.local/bin:$PATH
11. export AWS_ACCESS_KEY_ID= (your-key-here)
12. export AWS_SECRET_ACCESS_KEY= (your-secret-key-here)
13. configure serverless.yml
14. create handler
15. optional - create test data in data.json file
15. test function locally - ```serverless invoke local -f analyze --path data.json```
16. serverless deploy
16. ```curl -d @data.json -X POST https://<your-api-address>.amazonaws.com/dev/ping```

### What's next
1. Integrate with React.js application
2. Error handling
3. More advanced sentiment analysis
