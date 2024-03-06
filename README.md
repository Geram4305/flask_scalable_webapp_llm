### Flask application for sentiment analysis using LLM 
1. Application includes server components to support multiple parallel incoming requests.
2. Flask is used to develop the web application logic. Gunicorn is used as wsgi server and Nginx as web server specifically for load balancing. 
3. Docker is used to containerize the application. 
4. While creating docker container, python 3.9-slim used to keep size to minimum. 
5. A separate user and group for running applications is created in docker. It helps to isolate the application's permissions and resources from the rest of the system, reducing security related risks.
6. Both Nginx and Flask run from non-privileged ports.

## Please follow the following instrcutions to run the app successfully.

1. Install Docker desktop if not available from https://docs.docker.com/desktop/release-notes/
2. Keep the docker daemon running (in simpler terms keep docker desktop open).
3. Clone the git repo into a folder of choice, and navigate to the root folder in cmd. 
4. Run "docker-compose up --build". It will take a few minutes to start up the application.
5. Once application is started up, it will be hosted in localhost. Open a browser, type in http://localhost to access the application.

## Scale up and down

1. Kill all containers that are running currently by hitting ctrl+C. Run "docker-compose down" to remove and clear all.
2. Run "docker-compose up --build --scale app=3". This will churn up 3 instances of the application. 
3. Once application is started up, Open a browser type in http://localhost . You will see container ID that that request hit. Everytime you refresh the page, it may hit a different container (among the three created). 
4. THis is to show how multiple instances are running, but this is abstracted away from the user who still hits the same url.

## Get inference from LLM (Huggingface - DistilBert) for sentiment analysis

1. Kill all containers that are running currently by hitting ctrl+C. Run "docker-compose down" to remove and clear all.
2. Run "docker-compose up --build". This will churn up an instances of the application. 
3. Run test_app.py, which makes request to http://localhost/ with post method.
The script has texts like "It is worth it", "It is a waste of time and money" already in it. This will be used to get inference from DistilBert. The returned result is a label identifying the sentiment of the text and its condidence score. 

## Reasons for choosing the model - DistilBERT (distilbert-base-uncased-finetuned-sst-2-english)

1. "distilbert-base-uncased-finetuned-sst-2-english" is the model chosen for sentiment analysis. Assuming only English sentences are used by the end-user. It is a specialized variant of the DistilBERT model that has been fine-tuned specifically for sentiment analysis on English text using the SST-2 dataset. It can be readily used for English sentences.This is also the default model used for sentiment analysis in hugging face transformers. 
2. DistilBERT is a distilled version of the BERT (Bidirectional Encoder Representations from Transformers) model. It retains much of the performance of BERT while being smaller and faster.
3. Bidirectional models like DistilBERT process text in both directions (left-to-right and right-to-left), allowing them to capture contextual information from both preceding and succeeding words in a sentence. This bidirectional context understanding helps the model to better comprehend the meaning of each word in the context of the whole sentence, which is essential for sentiment analysis.
4. Capture long-range dependencies in sentences which is necessary to understanding the relationships between words that are far apart in the text
5. Restrictions: Only two classes - positive & negative.

### Reasons for choosing DistilBERT for this demo
1. It has faster inference, resource-efficient compared to a lot of other LLMs, while maintaining a high accuracy on sentiment analysis tasks.
2. Ideal for real-time applications where quick responses are needed.
3. Hence chose this model for demo purposes.